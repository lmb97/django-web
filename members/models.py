from django.contrib.auth.models import User
from django.db import models
from django.core.validators import *



class Instrument(models.Model):
	id = models.AutoField(primary_key=True, db_column='id', editable=False) 
	name = models.CharField(max_length=30, db_column='name', unique=True)

	def __unicode__(self):
	        return self.name

	class Meta:
		db_table = 'instruments'


class Post(models.Model):
	id = models.AutoField(primary_key=True, db_column='id', editable=False)
	name = models.CharField(db_column='name',max_length=45, unique=True)

	class Meta:
		db_table = 'posts'

	def __unicode__(self):
	        return self.name


class Email(models.Model):
	id = models.AutoField(primary_key=True, db_column='id', editable=False)
	name = models.CharField(db_column='name', max_length=40, unique=True)
	active = models.BooleanField(db_column='active', default=True)

	class Meta:
		db_table = 'emails'

	def __unicode__(self):
	        return self.name


class Person(models.Model):
	id = models.AutoField(primary_key=True, db_column='id', editable=False)
	name = models.CharField(max_length=25, db_column='name')
	surname = models.CharField(max_length=45, db_column='surname')
	birth = models.DateField(db_column='birth')
	phone_mobile = models.CharField(db_column='phone_mobile', max_length=9, blank=True, null=True)
	dni_number = models.CharField(max_length=8, db_column='dni_number', blank=True, null=True)
	dni_letter = models.CharField(max_length=1, db_column='dni_letter', blank=True, null=True)
	phone_house = models.CharField(db_column='phone_house', max_length=9, blank=True, null=True)
	address = models.CharField(max_length=100, db_column='address')
	postcode = models.CharField(db_column='postcode', max_length=5)
	join_ref = models.ForeignKey('self', db_column='join_ref', blank=True, null=True)

	instruments = models.ManyToManyField(Instrument, through='PersonInstrumentRelationship')
	posts = models.ManyToManyField(Post, through='PersonPostRelationship')
	emails = models.ManyToManyField(Email, through='PersonEmailRelationship')
	user = models.OneToOneField(User, db_column='user', blank=True, null=True)

	class Meta:
		db_table = 'people'

	def __unicode__(self):
	        return self.name + ' ' + self.surname


class PersonInstrumentRelationship(models.Model):
	id = models.AutoField(primary_key=True, db_column='id', editable=False)
	person = models.ForeignKey(Person, db_column='person')
	instrument = models.ForeignKey(Instrument, db_column='instrument')

	class Meta:
		db_table = 'rel_people_instruments'
		unique_together=('person','instrument')


class PersonPostRelationship(models.Model):
	post = models.ForeignKey(Post,db_column='post')
	person = models.ForeignKey(Person,db_column='person')
	join_date = models.DateField(db_column='join_date')
	out_date = models.DateField(db_column='out_date', blank=True, null=True)

	class Meta:
		db_table = 'rel_people_posts'


class PersonEmailRelationship(models.Model):
	person = models.ForeignKey(Person,db_column='person')
	email = models.ForeignKey(Email,db_column='email')

	class Meta:
		db_table = 'rel_people_emails'
		unique_together=('person','email')

