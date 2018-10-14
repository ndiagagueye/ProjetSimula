from django.contrib import admin

from .models import *



# Register your models here.
titre = "Administrateur SumilaMath"
admin.AdminSite.site_header = titre



admin.site.register(Systeme)
admin.site.register(Architecture)
admin.site.register(Logiciel)
admin.site.register(Version)
