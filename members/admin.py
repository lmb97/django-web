from members.models import *
from django.contrib import admin

class PersonInstrumentRelationshipInline(admin.TabularInline):
	model = PersonInstrumentRelationship
	extra = 1

class PersonPostRelationshipInline(admin.TabularInline):
	model = PersonPostRelationship
	extra = 1

class PersonEmailRelationshipInline(admin.TabularInline):
	model = PersonEmailRelationship
	extra = 1

class PersonAdmin(admin.ModelAdmin):
	filter_vertical = [
		'instruments',
		'posts',
		'emails',
    ]
	inlines = (
		PersonInstrumentRelationshipInline,
		PersonPostRelationshipInline,
		PersonEmailRelationshipInline,
	)
	fieldsets = (
		('Personal Information', {
			'fields':[
				'name',
				'surname',
				'dni_number',
				'dni_letter',
				'birth',
			]
		}),
		('Contact Information', {
			'fields':[
				'address',
				'postcode',
				'phone_mobile',
				'phone_house',
			]
		}),
		('Miscelaneous Information', {
			'fields':[
				'join_ref',
				'user',
			]
		}),
	)

class InstrumentAdmin(admin.ModelAdmin):
	filter_vertical = ['Person_set']
	inlines = (
		PersonInstrumentRelationshipInline,
	)

class PostAdmin(admin.ModelAdmin):
	filter_vertical = ['person']
	inlines = (
		PersonPostRelationshipInline,
	)

class EmailAdmin(admin.ModelAdmin):
	filter_vertical = ['person']
	inlines = (
		PersonEmailRelationshipInline,
	)

admin.site.register(Person, PersonAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Email, EmailAdmin)
