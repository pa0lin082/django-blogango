# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blog'
        db.create_table(u'blogango_blog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tag_line', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('entries_per_page', self.gf('django.db.models.fields.IntegerField')(default=10)),
            ('recents', self.gf('django.db.models.fields.IntegerField')(default=5)),
            ('recent_comments', self.gf('django.db.models.fields.IntegerField')(default=5)),
        ))
        db.send_create_signal(u'blogango', ['Blog'])

        # Adding model 'BlogEntry'
        db.create_table(u'blogango_blogentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('text', self.gf('markupfield.fields.MarkupField')(rendered_field=True)),
            ('text_markup_type', self.gf('django.db.models.fields.CharField')(default='plain', max_length=30)),
            ('summary', self.gf('django.db.models.fields.TextField')()),
            ('_text_rendered', self.gf('django.db.models.fields.TextField')()),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.max.replace(tzinfo=datetime.timezone.utc))),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('is_page', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('comments_allowed', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_rte', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'blogango', ['BlogEntry'])

        # Adding model 'Comment'
        db.create_table(u'blogango_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('comment_for', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogango.BlogEntry'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('email_id', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('is_spam', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_public', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('user_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal(u'blogango', ['Comment'])

        # Adding model 'Reaction'
        db.create_table(u'blogango_reaction', (
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('comment_for', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogango.BlogEntry'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('user_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('reaction_id', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('profile_image', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'blogango', ['Reaction'])

        # Adding model 'BlogRoll'
        db.create_table(u'blogango_blogroll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(unique=True, max_length=200)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'blogango', ['BlogRoll'])


    def backwards(self, orm):
        # Deleting model 'Blog'
        db.delete_table(u'blogango_blog')

        # Deleting model 'BlogEntry'
        db.delete_table(u'blogango_blogentry')

        # Deleting model 'Comment'
        db.delete_table(u'blogango_comment')

        # Deleting model 'Reaction'
        db.delete_table(u'blogango_reaction')

        # Deleting model 'BlogRoll'
        db.delete_table(u'blogango_blogroll')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'blogango.blog': {
            'Meta': {'object_name': 'Blog'},
            'entries_per_page': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recent_comments': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'recents': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'tag_line': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'blogango.blogentry': {
            'Meta': {'ordering': "['-created_on']", 'object_name': 'BlogEntry'},
            '_text_rendered': ('django.db.models.fields.TextField', [], {}),
            'comments_allowed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.max.replace(tzinfo=datetime.timezone.utc)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_rte': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'text': ('markupfield.fields.MarkupField', [], {'rendered_field': 'True'}),
            'text_markup_type': ('django.db.models.fields.CharField', [], {'default': "'plain'", 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'blogango.blogroll': {
            'Meta': {'object_name': 'BlogRoll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'blogango.comment': {
            'Meta': {'ordering': "['created_on']", 'object_name': 'Comment'},
            'comment_for': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blogango.BlogEntry']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email_id': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_spam': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user_agent': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'user_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'blogango.reaction': {
            'Meta': {'ordering': "['created_on']", 'object_name': 'Reaction'},
            'comment_for': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blogango.BlogEntry']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'profile_image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'reaction_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blogango']