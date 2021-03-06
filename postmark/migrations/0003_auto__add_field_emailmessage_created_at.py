# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'EmailMessage.created_at'
        db.add_column('postmark_emailmessage', 'created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2012, 2, 15, 17, 23, 16, 935068), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'EmailMessage.created_at'
        db.delete_column('postmark_emailmessage', 'created_at')


    models = {
        'postmark.emailbounce': {
            'Meta': {'ordering': "('_order',)", 'object_name': 'EmailBounce'},
            '_order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bounced_at': ('django.db.models.fields.DateTimeField', [], {}),
            'can_activate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'details': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'inactive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bounces'", 'to': "orm['postmark.EmailMessage']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'postmark.emailmessage': {
            'Meta': {'ordering': "['-submitted_at']", 'object_name': 'EmailMessage'},
            'attachments': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'headers': ('django.db.models.fields.TextField', [], {}),
            'html_body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_id': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'reply_to': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'submitted_at': ('django.db.models.fields.DateTimeField', [], {}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'text_body': ('django.db.models.fields.TextField', [], {}),
            'to': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'to_type': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['postmark']
