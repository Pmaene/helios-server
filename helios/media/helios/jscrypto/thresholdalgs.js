thresholdalgs = {};

thresholdalgs.encode_string_to_decimal = function (s) {
    var tmp = '';
    for (var i = 0; i < s.length; i++) {
        var c = s[i];
        tmp = tmp + String(c.charCodeAt(0));
    }
    return BigInt.fromJSONObject(tmp)
}

thresholdalgs.Polynomial = Class.extend({
    init: function (c0, k, EG) {
        var p = EG.p;
        var q = EG.q;
        this.coeff = [];
        this.coeff.push(c0);
        this.EG = EG;
        this.degree = k - 1;

        for (var i = 0; i < this.degree; i++) {
            this.coeff.push(Random.getRandomInteger(q));
        }
    },

    set: function (coeff) {
        this.coeff = coeff;
        return null;
    },

    create_points: function (ids) {
        var points = [];
        for (var i = 0; i < ids.length; i++) {
            var point = create_point(ids[i]);
            points.push(point);
        }
        return points;

    },
    evaluate: function (x) {
        var q = this.EG.q;
        var x = BigInt.fromInt(x);
        var value = BigInt.ZERO;
        for (i = 0; i < this.degree + 1; i++) {
            var pow = BigInt.fromInt(i);
            value = (value.add(this.coeff[i].multiply(x.modPow(pow, q))));
            value = value.mod(q);
        }
        return value;

    },
    
    create_point: function (id) {
    	return new thresholdalgs.Point(BigInt.fromInt(id), this.evaluate(id));
    },
    
    toJSONObject: function () {
        var coefflist = [];
        for (var i = 0; i < this.coeff.length; i++) {
        	coefflist[i] = this.coeff[i].toJSONObject();
        }
        return {
            coeffs: coefflist,
            degree: this.degree,
        };
    }
});

thresholdalgs.Polynomial.fromJSONObject = function (d,EG) {
    var degree = d.degree;
   
    coefflist = [];
    for(var i = 0; i < d.coeffs.length; i++){
    	coefflist.push(BigInt.fromJSONObject(d.coeffs[i]));
    }
    
   
    var poly = new thresholdalgs.Polynomial(0, degree+1, EG);
    poly.coeff = coefflist;
    return poly;
};

thresholdalgs.Point = Class.extend({
    init: function (x, y) {
        this.x_value = x;
        this.y_value = y;
    },

    encrypt: function (public_key) {
        var plain_x = new ElGamal.Plaintext(this.x_value, public_key);
        var plain_y = new ElGamal.Plaintext(this.y_value, public_key);
        var ciph_x = ElGamal.encrypt(public_key, plain_x);
        var ciph_y = ElGamal.encrypt(public_key, plain_y);
        return new thresholdalgs.EncryptedPoint(ciph_x, ciph_y);
    },

    on_polynomial: function (polynom) {
        if (polynom.evaluate(this.x_value) == this.y_value)
            return true;
        else
            return false;
    },

    toJSONObject: function () {
        return {
            x_value: this.x_value.toJSONObject(),
            y_value: this.y_value.toJSONObject()
        };
    },

});

thresholdalgs.Point.fromJSONObject = function (d) {
    return new thresholdalgs.Point(d.x_value, d.y_value);
};

thresholdalgs.EncryptedPoint = Class.extend({
    init: function (ciph_x, ciph_y) {
        this.ciph_x = ciph_x;
        this.ciph_y = ciph_y;
    },

    decrypt: function (secret_key) {
        this.ciph_x.pk = secret_key.pk;
        this.ciph_y.pk = secret_key.pk;
        var x_val = secret_key.decrypt(this.ciph_x).m;
        var y_val = secret_key.decrypt(this.ciph_y).m;
        return new thresholdalgs.Point(x_val, y_val);
    },
    
    get_json_string: function () {
        return JSON.stringify(this.toJSONObject());
    },
    
    sign: function (secret_key, EG) {
        var sig = new thresholdalgs.Signature(null, null);
        sig.generate(this.get_json_string(), secret_key, EG.p, EG.q, EG.g);
        return sig;
    },

    toJSONObject: function () {
        return {
            ciph_x: this.ciph_x.toJSONObject(),
            ciph_y: this.ciph_y.toJSONObject()
        };

    }
});

thresholdalgs.EncryptedPoint.fromJSONObject = function (d) {
    return new thresholdalgs.EncryptedPoint(ElGamal.Ciphertext.fromJSONObject(d.ciph_x), ElGamal.Ciphertext.fromJSONObject(d.ciph_y));
};

thresholdalgs.Share = Class.extend({
    init: function (point_s, Ei) {
        this.point_s = point_s;
        this.Ei = Ei;
    },

    add: function (addedshare, p, q, g, scheme) {
        if (this.point_s.x_value.equals(addedshare.point_s.x_value)) {
            x = this.point_s.x_value;
            var new_point_s = new thresholdalgs.Point(x, (this.point_s.y_value.add(addedshare.point_s.y_value)).mod(q));
            
            new_Ei = [];
            var overall_succes = true;
            for (var i = 0; i < this.Ei.length; i++) {
                Ei_now = this.Ei[i];
                var succes = Ei_now.add(addedshare.Ei[i], p, q, g, scheme);
                if (!succes)
                    overall_succes = false;

                new_Ei.push(Ei_now);
            }
            this.point_s = new_point_s;
            this.Ei = new_Ei;

            if (this.verify_share(scheme, p, q, g)) {
                if (overall_succes) {
                    return true;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        } else {
            return false;
        }
    },

    encrypt: function (public_key) {
        var encry_point_s = this.point_s.encrypt(public_key);
        var encry_share = new thresholdalgs.EncryptedShare(encry_point_s, this.Ei);
        return encry_share;
    },

    get_json_string: function () {
        return JSON.stringify(this.toJSONObject());

    },
    sign: function (secret_key, p, q, g) {
        var sig = new thresholdalgs.Signature(null, null);
        sig.generate(this.get_json_string(), secret_key, p, q, g);
        return sig;
    },

    verify_share: function (scheme, p, q, g) {
        var k = scheme.k;
        var n = scheme.n;
        var E = new thresholdalgs.CommitmentE(null, null, null)
        E.generate(this.point_s.y_value, p, q, g);
        var point_number = this.point_s.x_value;
        var result = BigInt.ONE;
        if (this.Ei.length != k)
            return false;
        for (var j = 0; j < this.Ei.length; j++) {
            var i = point_number;
            var pow = BigInt.fromInt(j);
            var interm = i.modPow(pow, p).mod(p);
            result = (result.multiply(BigInt.fromInt(this.Ei[j].value).modPow(interm, p))).mod(p);
        }
        if (!result.equals(E.value)) {
            return false;
        } else {
            return true;
        }
    },

    toJSONObject: function () {
        var com_dict = {};
        for (var i = 0; i < this.Ei.length; i++) {
            com_dict[String(i)] = this.Ei[i].toJSONObject();
        }
        return {
            Ei: com_dict,
            point_s: this.point_s.toJSONObject(),
        };
    }
});

thresholdalgs.Share.fromJSONObject = function (d) {
    var point_s = Point.fromJSONObject(d.point_s);
   
    var Ei_dict = d.Ei;
    var Ei = [];
    var i = 0;
    while (String(i) in Ei_dict) {
        var dict = Ei_dict[String(i)];
        var com = new thresholdalgs.CommitmentE.fromJSONObject(dict);
        Ei.push(com);
        i++;
    }
    var share = new thresholdalgs.Share(point_s, Ei);
    return share;
};


thresholdalgs.SignedEncryptedShare = Class.extend({
    init: function (sig, encr_share, receiver) {
        this.sig = sig;
        this.encr_share = encr_share;
        this.receiver = receiver;

    },

    toJSONObject: function () {

        return {
            'encr_share': this.encr_share.toJSONObject(),
            'sig': this.sig.toJSONObject(),
            'receiver': this.receiver
        };
    },
});

thresholdalgs.SignedEncryptedShare.fromJSONObject = function (d,receiver) {
    var encr_share = thresholdalgs.EncryptedPoint.fromJSONObject(d['encr_share']);
    var sig = thresholdalgs.Signature.fromJSONObject(d['sig']);
    var sig_encr_share = new thresholdalgs.SignedEncryptedShare(sig, encr_share,receiver);

    return sig_encr_share;
};

thresholdalgs.CommitmentE = Class.extend({
    init: function (EG, value) {
        this.value = value;
        this.EG = EG;
    },

    generate: function (poly) {
    	this.value = [];
    	for(var i=0;i<poly.coeff.length;i++){
    		this.value[i] = this.EG.g.modPow(poly.coeff[i], this.EG.p);
    	}
    },
    
    gethash : function(){
    	var valuesjson = [];
    	for(var i = 0; i < this.value.length; i++){
    		valuesjson[i] = this.value[i].toJSONObject();
    	}
    	return b64_sha256(JSON.stringify(valuesjson));
    },
    
    evaluate: function (x) {
        var q = this.EG.q;
        var p = this.EG.p;
        var x = BigInt.fromInt(x);
        var ret = this.value[0];
        for (i = 1; i < this.degree + 1; i++) {
            var pow = BigInt.fromInt(i);
            ret = (ret.mul(this.value[i].modPow(x.modPow(pow,q),p)));
            ret = ret.mod(p);
        }
        return ret;

    },
    
    validate: function (x,s) {
    	return 0 == this.evaluate(x).compareTo(this.EG.g.modPow(s,this.EG.p));
    },
    
    toJSONObject: function () {
    	var valuesjson = [];
    	for(var i = 0; i < this.value.length; i++){
    		valuesjson[i] = this.value[i].toJSONObject();
    	}
    	
        return valuesjson;

    },
});

thresholdalgs.CommitmentE.fromJSONObject = function (d,EG) {
	var valuelist = [];
	for(var i = 0; i < d.length; i++){
    	valuelist.push(BigInt.fromJSONObject(d[i]));
    }
    var com = new thresholdalgs.CommitmentE(EG,valuelist);

    return com;
};

thresholdalgs.Signature = Class.extend({
    init: function (r, s) {
        this.r = r;
        this.s = s;
    },

    generate: function (m, secret_key, p, q, g) {
        while (true) {
            var p_1 = p.add(BigInt.ONE.negate());
            var hash = hex_sha256(m);

            var hash_dec = new BigInt(hash,16);

            var k = Random.random_k_relative_prime_p_1(p);
            var k_inv = k.modInverse(p_1);
            var x = secret_key.x;
            var r = g.modPow(k, p).mod(p);
            var s = (hash_dec.add(x.multiply(r).negate()).multiply(k_inv)).mod(p_1);
            if (!s.equals(BigInt.ONE)) {
                this.s = s;
                this.r = r;
                return null;
            }
        }
    },

    verify: function (m, public_key, EG) {
    	var p = EG.p; var q = EG.q; var g = EG.g;
        var correct = true;
        var y = public_key.y;
        var hash = hex_sha256(m);
        var hash_dec = new BigInt(hash,16);

        var val = (y.modPow(this.r, p).multiply(this.r.modPow(this.s, p))).mod(p);
        if (!g.modPow(hash_dec, p).mod(p).equals(val))
            correct = false;

        return correct;
    },

    toJSONObject: function () {
        return {
            'r': this.r.toJSONObject(),
            's': this.s.toJSONObject()
        };
    },
});

thresholdalgs.Signature.fromJSONObject = function (d) {
    var r = BigInt.fromJSONObject(d['r']);
    var s = BigInt.fromJSONObject(d['s']);
    return new thresholdalgs.Signature(r, s);
};



thresholdalgs.ThresholdScheme = Class.extend({
    init: function (election_id, n, k) {
        this.election_id = election_id;
        this.n = n;
        this.k = k;
    },
    

    share_verifiably: function (s, EG, ids) {
        var F = new thresholdalgs.Polynomial(s, this, EG);

        var points_F = F.create_points(ids);

        var shares = [];
        for (var i = 1; i < this.n + 1; i++) {
            var share = new thresholdalgs.Share(points_F[i - 1], Ei);
            if (share.verify_share(this, EG.p, EG.q, EG.g)) {
                shares.push(share);
            } else {
                return null;
            }
        }

        return shares;
    }
});

thresholdalgs.ThresholdScheme.fromJSONObject = function (d) {
    var election_id = parseInt(d.election_id);
    var n = parseInt(d.n);
    var k = parseInt(d.k);
    
    return new thresholdalgs.ThresholdScheme(election_id, n, k);
};

function storage_encrypt(key,data){
	window.console.log("Encrypting "+data);
	p = {mode:"ccm", ts:128, ks:256 };
	return sjcl.encrypt(sjcl.codec.base64.toBits(key), data, p);
}

function storage_decrypt(key,data){
	p = {mode:"ccm", ts:128, ks:256 };
	return sjcl.decrypt(sjcl.codec.base64.toBits(key),data,p);
}
