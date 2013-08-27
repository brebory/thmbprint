# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'profiles_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'profiles', ['UserProfile'])

        # Adding model 'StudentUser'
        db.create_table(u'profiles_studentuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='student_profile', unique=True, null=True, to=orm['profiles.UserProfile'])),
        ))
        db.send_create_signal(u'profiles', ['StudentUser'])

        # Adding model 'MentorUser'
        db.create_table(u'profiles_mentoruser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='mentor_profile', unique=True, null=True, to=orm['profiles.UserProfile'])),
        ))
        db.send_create_signal(u'profiles', ['MentorUser'])

        # Adding model 'Project'
        db.create_table(u'profiles_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.UserProfile'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'profiles', ['Project'])

        # Adding model 'ProjectItem'
        db.create_table(u'profiles_projectitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.Project'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'profiles', ['ProjectItem'])

        # Adding model 'ProjectItemImage'
        db.create_table(u'profiles_projectitemimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.ProjectItem'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('image_data', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'profiles', ['ProjectItemImage'])

        # Adding model 'ProjectItemFile'
        db.create_table(u'profiles_projectitemfile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.ProjectItem'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('file_data', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'profiles', ['ProjectItemFile'])

        # Adding model 'Recommendation'
        db.create_table(u'profiles_recommendation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.StudentUser'])),
            ('mentor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.MentorUser'])),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'profiles', ['Recommendation'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'profiles_userprofile')

        # Deleting model 'StudentUser'
        db.delete_table(u'profiles_studentuser')

        # Deleting model 'MentorUser'
        db.delete_table(u'profiles_mentoruser')

        # Deleting model 'Project'
        db.delete_table(u'profiles_project')

        # Deleting model 'ProjectItem'
        db.delete_table(u'profiles_projectitem')

        # Deleting model 'ProjectItemImage'
        db.delete_table(u'profiles_projectitemimage')

        # Deleting model 'ProjectItemFile'
        db.delete_table(u'profiles_projectitemfile')

        # Deleting model 'Recommendation'
        db.delete_table(u'profiles_recommendation')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profiles.mentoruser': {
            'Meta': {'object_name': 'MentorUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'mentor_profile'", 'unique': 'True', 'null': 'True', 'to': u"orm['profiles.UserProfile']"})
        },
        u'profiles.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.UserProfile']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True'})
        },
        u'profiles.projectitem': {
            'Meta': {'object_name': 'ProjectItem'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.Project']"})
        },
        u'profiles.projectitemfile': {
            'Meta': {'object_name': 'ProjectItemFile'},
            'file_data': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.ProjectItem']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'profiles.projectitemimage': {
            'Meta': {'object_name': 'ProjectItemImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_data': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'project_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.ProjectItem']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'profiles.recommendation': {
            'Meta': {'object_name': 'Recommendation'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mentor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.MentorUser']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.StudentUser']"}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'profiles.studentuser': {
            'Meta': {'object_name': 'StudentUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'student_profile'", 'unique': 'True', 'null': 'True', 'to': u"orm['profiles.UserProfile']"})
        },
        u'profiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['profiles']