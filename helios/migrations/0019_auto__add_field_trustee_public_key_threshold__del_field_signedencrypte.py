# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Trustee.public_key_threshold'
        db.add_column(u'helios_trustee', 'public_key_threshold',
                      self.gf('helios.datatypes.djangofield.LDObjectField')(null=True),
                      keep_default=False)

        # Deleting field 'SignedEncryptedShare.receiver_id'
        db.delete_column(u'helios_signedencryptedshare', 'receiver_id')

        # Deleting field 'SignedEncryptedShare.receiver'
        db.delete_column(u'helios_signedencryptedshare', 'receiver')

        # Deleting field 'SignedEncryptedShare.signer'
        db.delete_column(u'helios_signedencryptedshare', 'signer')

        # Deleting field 'SignedEncryptedShare.election_id'
        db.delete_column(u'helios_signedencryptedshare', 'election_id')

        # Deleting field 'SignedEncryptedShare.signer_id'
        db.delete_column(u'helios_signedencryptedshare', 'signer_id')

        # Adding field 'SignedEncryptedShare.election'
        db.add_column(u'helios_signedencryptedshare', 'election',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['helios.Election']),
                      keep_default=False)


        # Changing field 'SignedEncryptedShare.share'
        db.alter_column(u'helios_signedencryptedshare', 'share', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Trustee.public_key_threshold'
        db.delete_column(u'helios_trustee', 'public_key_threshold')


        # User chose to not deal with backwards NULL issues for 'SignedEncryptedShare.receiver_id'
        raise RuntimeError("Cannot reverse this migration. 'SignedEncryptedShare.receiver_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SignedEncryptedShare.receiver_id'
        db.add_column(u'helios_signedencryptedshare', 'receiver_id',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SignedEncryptedShare.receiver'
        raise RuntimeError("Cannot reverse this migration. 'SignedEncryptedShare.receiver' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SignedEncryptedShare.receiver'
        db.add_column(u'helios_signedencryptedshare', 'receiver',
                      self.gf('django.db.models.fields.CharField')(max_length=40),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SignedEncryptedShare.signer'
        raise RuntimeError("Cannot reverse this migration. 'SignedEncryptedShare.signer' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SignedEncryptedShare.signer'
        db.add_column(u'helios_signedencryptedshare', 'signer',
                      self.gf('django.db.models.fields.CharField')(max_length=40),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SignedEncryptedShare.election_id'
        raise RuntimeError("Cannot reverse this migration. 'SignedEncryptedShare.election_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SignedEncryptedShare.election_id'
        db.add_column(u'helios_signedencryptedshare', 'election_id',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'SignedEncryptedShare.signer_id'
        raise RuntimeError("Cannot reverse this migration. 'SignedEncryptedShare.signer_id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'SignedEncryptedShare.signer_id'
        db.add_column(u'helios_signedencryptedshare', 'signer_id',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)

        # Deleting field 'SignedEncryptedShare.election'
        db.delete_column(u'helios_signedencryptedshare', 'election_id')


        # User chose to not deal with backwards NULL issues for 'SignedEncryptedShare.share'
        raise RuntimeError("Cannot reverse this migration. 'SignedEncryptedShare.share' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'SignedEncryptedShare.share'
        db.alter_column(u'helios_signedencryptedshare', 'share', self.gf('django.db.models.fields.CharField')(max_length=10000000))

    models = {
        u'helios.auditedballot': {
            'Meta': {'object_name': 'AuditedBallot'},
            'added_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['helios.Election']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_vote': ('django.db.models.fields.TextField', [], {}),
            'vote_hash': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'helios.castvote': {
            'Meta': {'object_name': 'CastVote'},
            'cast_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invalidated_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'quarantined_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'released_from_quarantine_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'verified_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'vote': ('helios.datatypes.djangofield.LDObjectField', [], {}),
            'vote_hash': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'vote_tinyhash': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'}),
            'voter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['helios.Voter']"})
        },
        u'helios.election': {
            'Meta': {'object_name': 'Election'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['helios_auth.User']"}),
            'archived_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'cast_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'complaint_period_ends_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datatype': ('django.db.models.fields.CharField', [], {'default': "'legacy/Election'", 'max_length': '250'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'election_info_url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'}),
            'election_type': ('django.db.models.fields.CharField', [], {'default': "'election'", 'max_length': '250'}),
            'eligibility': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'encrypted_shares_uploaded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'encrypted_tally': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'featured_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frozen_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'frozen_trustee_list': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'help_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'openreg': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'private_key': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'private_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'public_key': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'questions': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'randomize_answer_order': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'registration_starts_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'result': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'result_proof': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'result_released_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tallies_combined_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'tallying_finished_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'tallying_started_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'tallying_starts_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'use_advanced_audit_features': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_threshold': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'use_voter_aliases': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'voters_hash': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'voting_ended_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'voting_ends_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'voting_extended_until': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'voting_started_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'voting_starts_at': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'})
        },
        u'helios.electionlog': {
            'Meta': {'object_name': 'ElectionLog'},
            'at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['helios.Election']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'log': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'helios.incorrectshare': {
            'Meta': {'object_name': 'IncorrectShare'},
            'election_id': ('django.db.models.fields.IntegerField', [], {}),
            'explanation': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receiver_id': ('django.db.models.fields.IntegerField', [], {}),
            'share': ('django.db.models.fields.CharField', [], {'max_length': '100000'}),
            'sig': ('django.db.models.fields.CharField', [], {'max_length': '100000'}),
            'signer_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'helios.signedencryptedshare': {
            'Meta': {'object_name': 'SignedEncryptedShare'},
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['helios.Election']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'share': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'trustee_receiver_id': ('django.db.models.fields.IntegerField', [], {}),
            'trustee_signer_id': ('django.db.models.fields.IntegerField', [], {})
        },
        u'helios.thresholdscheme': {
            'Meta': {'object_name': 'ThresholdScheme'},
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['helios.Election']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'k': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'n': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'helios.trustee': {
            'Meta': {'unique_together': "(('election', 'email'),)", 'object_name': 'Trustee'},
            'added_encrypted_shares': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'communication_keys': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'decryption_factors': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'decryption_proofs': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['helios.Election']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'helios_trustee': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pok': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'public_key': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'public_key_commit': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'public_key_commit_hash': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'public_key_hash': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'public_key_threshold': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'secret_key': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'storagespace': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'threshold_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['helios_auth.User']", 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'helios.voter': {
            'Meta': {'unique_together': "(('election', 'voter_login_id'),)", 'object_name': 'Voter'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'cast_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['helios.Election']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['helios_auth.User']", 'null': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vote': ('helios.datatypes.djangofield.LDObjectField', [], {'null': 'True'}),
            'vote_hash': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'voter_email': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'voter_login_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'voter_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'voter_password': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        },
        u'helios.voterfile': {
            'Meta': {'object_name': 'VoterFile'},
            'election': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['helios.Election']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_voters': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'processing_finished_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'processing_started_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'voter_file': ('django.db.models.fields.files.FileField', [], {'max_length': '250', 'null': 'True'}),
            'voter_file_content': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        u'helios_auth.user': {
            'Meta': {'unique_together': "(('user_type', 'user_id'),)", 'object_name': 'User'},
            'admin_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('helios_auth.jsonfield.JSONField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'token': ('helios_auth.jsonfield.JSONField', [], {'null': 'True'}),
            'user_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['helios']