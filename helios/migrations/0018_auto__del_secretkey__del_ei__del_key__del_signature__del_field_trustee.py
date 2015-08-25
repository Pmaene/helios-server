# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'SecretKey'
        db.delete_table(u'helios_secretkey')

        # Deleting model 'Ei'
        db.delete_table(u'helios_ei')

        # Deleting model 'Key'
        db.delete_table(u'helios_key')

        # Deleting model 'Signature'
        db.delete_table(u'helios_signature')

        # Deleting field 'Trustee.original_id'
        db.delete_column(u'helios_trustee', 'original_id')

        # Deleting field 'Trustee.key'
        db.delete_column(u'helios_trustee', 'key_id')

        # Adding field 'Trustee.threshold_id'
        db.add_column(u'helios_trustee', 'threshold_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Trustee.public_key_commit_hash'
        db.add_column(u'helios_trustee', 'public_key_commit_hash',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Trustee.public_key_commit'
        db.add_column(u'helios_trustee', 'public_key_commit',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Adding field 'Trustee.communication_keys'
        db.add_column(u'helios_trustee', 'communication_keys',
                      self.gf('helios.datatypes.djangofield.LDObjectField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'SecretKey'
        db.create_table(u'helios_secretkey', (
            ('public_key', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['helios.Key'])),
            ('secret_key_encrypt', self.gf('django.db.models.fields.CharField')(max_length=10000, null=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('secret_key_signing', self.gf('django.db.models.fields.CharField')(max_length=10000, null=True)),
        ))
        db.send_create_signal(u'helios', ['SecretKey'])

        # Adding model 'Ei'
        db.create_table(u'helios_ei', (
            ('value', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('signer', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('election_id', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('signer_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'helios', ['Ei'])

        # Adding model 'Key'
        db.create_table(u'helios_key', (
            ('pok_signing', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('public_key_encrypt_hash', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('public_key_encrypt', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('public_key_signing_hash', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('public_key_signing', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('pok_encrypt', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=60)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'helios', ['Key'])

        # Adding model 'Signature'
        db.create_table(u'helios_signature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('signature', self.gf('django.db.models.fields.CharField')(max_length=10000)),
        ))
        db.send_create_signal(u'helios', ['Signature'])

        # Adding field 'Trustee.original_id'
        db.add_column(u'helios_trustee', 'original_id',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Trustee.key'
        db.add_column(u'helios_trustee', 'key',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['helios.Key'], null=True),
                      keep_default=False)

        # Deleting field 'Trustee.threshold_id'
        db.delete_column(u'helios_trustee', 'threshold_id')

        # Deleting field 'Trustee.public_key_commit_hash'
        db.delete_column(u'helios_trustee', 'public_key_commit_hash')

        # Deleting field 'Trustee.public_key_commit'
        db.delete_column(u'helios_trustee', 'public_key_commit')

        # Deleting field 'Trustee.communication_keys'
        db.delete_column(u'helios_trustee', 'communication_keys')


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
            'election_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receiver': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'receiver_id': ('django.db.models.fields.IntegerField', [], {}),
            'share': ('django.db.models.fields.CharField', [], {'max_length': '10000000'}),
            'signer': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'signer_id': ('django.db.models.fields.IntegerField', [], {}),
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