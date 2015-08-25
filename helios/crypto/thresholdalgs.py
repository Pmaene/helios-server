import math
import hashlib
import logging
import sys

import randpool, number
import numtheory
import elgamal
from algs import Utils
import algs
import utils

from fractions import *

class ThresholdScheme():

    def __init__(self, n=None, k=None):
        self.n = n
        self.k = k


class CommunicationKeys():
    def __init__(self):
        self.public_key_encrypt = None
        self.public_key_signing = None
        self.pok_encrypt = None
        self.pok_signing = None

class EncryptedPoint():

    def __init__(self, ciph_x=None, ciph_y=None):
        self.ciph_x = ciph_x
        self.ciph_y = ciph_y

    @classmethod
    def from_dict(cls, d):
        """
        Deserialize from dictionary.
        """
        ciph_x = algs.EGCiphertext.from_dict(d['ciph_x'])
        ciph_y = algs.EGCiphertext.from_dict(d['ciph_y'])
        encr_point = EncryptedPoint(ciph_x, ciph_y)
        return encr_point

    def to_dict(self):
        """
        Serialize to dictionary.
        """
        return {'ciph_x': self.ciph_x.to_dict(), 'ciph_y': self.ciph_y.to_dict()}

class Share():

    def __init__(self, sig=None, encr_share=None):
        self.sig = sig
        self.encr_share = encr_share

    @classmethod
    def from_dict(cls, d):
        """
        Deserialize from dictionary.
        """
        encr_share = EncryptedPoint.from_dict(d['encr_share'])
        sig = Signature.from_dict(d['sig'])
        sig_encr_share = Share(sig, encr_share)

        return sig_encr_share

    def to_dict(self):
        """
        Serialize to dictionary.
        """
        return {'sig': self.sig.to_dict(), 'encr_share': self.encr_share.to_dict()}

class Feedback():

    def __init__(self, trustee_id, feedback):
        self.trustee_id = trustee_id
        self.feedback = feedback

    def set_feedback(self, feedback):
        self.feedback = feedback


class CommitmentE():

    def __init__(self, value=None):
        self.value = value

    def add(self, addedcommitment, p, q, g):
        self.value = (self.value * addedcommitment.value) % p

    def evaluate(self, x, EG):
        q = EG.q
        p = EG.p
        result = 1
        for j in range(len(self.value)):
            result = (result * pow(self.value[j], pow(x, j, q), p)) % p
        return result

    @classmethod
    def from_dict(cls, d):
        """
        Deserialize from dictionary.
        """
        vallist = utils.from_json(d)
        value = []
        for v in vallist:
                value.append(int(v))

        com = CommitmentE(value)

        return com

    @classmethod
    def array_from_dict(cls, d):
        i = 0
        while d.has_key(str(i)):
            dict = d[str(i)]
            com = CommitmentE().from_dict(dict)
            com = CommitmentE()
            i = i + 1

    def to_dict(self):
        """
        Serialize to dictionary.
        """
        return {'value': str(self.value)}


class Signature():

    def __init__(self, r=None, s=None):
        self.r = r
        self.s = s

    def generate(self, m, secret_key, p, q, g):
        while True:
            hash = utils.hash_b64(m)
            hash_dec = utils.encode_string_to_decimal(hash)
            k = algs.Utils.random_k_relative_prime_p_1(p)
            k_inv = algs.Utils.inverse(k, p - 1)
            x = secret_key.x
            r = pow(g, k, p)
            s = ((hash_dec - x * r) * k_inv) % (p - 1)
            if s != 1:
                self.s = s
                self.r = r
                return None

    def verify(self, m, public_key, p, q, g):
        correct = True
        y = public_key.y
        hash = utils.hash_b64(m)
        hash_dec = utils.encode_string_to_decimal(hash)
        if self.r >= p:
            correct = False
        if self.s >= p - 1:
            correct = False
        val = (pow(y, self.r, p) * pow(self.r, self.s, p)) % p
        if (pow(g, hash_dec, p) != val):
            correct = False

        return correct

    @classmethod
    def from_dict(cls, d):
        """
        Deserialize from dictionary.
        """
        r = int(d['r'])
        s = int(d['s'])

        return cls(r, s)

    def to_dict(self):
        """
        Serialize to dictionary.
        """
        return {'r': str(self.r), 's': str(self.s)}
