# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlogCategory'
        db.create_table(u'blogango_blogcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogango.BlogCategory'], null=True, blank=True)),
        ))
        db.send_create_signal(u'blogango', ['BlogCategory'])


        # Changing field 'Comment.created_by'
        db.alter_column(u'blogango_comment', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'], null=True))
        # Adding field 'BlogEntry.category'
        db.add_column(u'blogango_blogentry', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blogango.BlogCategory'], null=True, blank=True),
                      keep_default=False)


        # Changing field 'BlogEntry.created_by'
        db.alter_column(u'blogango_blogentry', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User']))

    def backwards(self, orm):
        # Deleting model 'BlogCategory'
        db.delete_table(u'blogango_blogcategory')


        # Changing field 'Comment.created_by'
        db.alter_column(u'blogango_comment', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.User'], null=True))
        # Deleting field 'BlogEntry.category'
        db.delete_column(u'blogango_blogentry', 'category_id')


        # Changing field 'BlogEntry.created_by'
        db.alter_column(u'blogango_blogentry', 'created_by_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.User']))

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
        u'blogango.blog': {
            'Meta': {'object_name': 'Blog'},
            'entries_per_page': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recent_comments': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'recents': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'tag_line': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'blogango.blogcategory': {
            'Meta': {'object_name': 'BlogCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blogango.BlogCategory']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'blogango.blogentry': {
            'Meta': {'ordering': "['-created_on']", 'object_name': 'BlogEntry'},
            '_text_rendered': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blogango.BlogCategory']", 'null': 'True', 'blank': 'True'}),
            'comments_allowed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']", 'null': 'True', 'blank': 'True'}),
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
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'children': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'child_of'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['users.User']"}),
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
        }
    }

    complete_apps = ['blogango']