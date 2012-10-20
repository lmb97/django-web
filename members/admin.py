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
	inlines = (
		PersonInstrumentRelationshipInline,
		PersonPostRelationshipInline,
		PersonEmailRelationshipInline,
	)

class InstrumentAdmin(admin.ModelAdmin):
	inlines = (
		PersonInstrumentRelationshipInline,
	)

class PostAdmin(admin.ModelAdmin):
	inlines = (
		PersonPostRelationshipInline,
	)

class EmailAdmin(admin.ModelAdmin):
	inlines = (
		PersonEmailRelationshipInline,
	)

admin.site.register(Person, PersonAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Email, EmailAdmin)
