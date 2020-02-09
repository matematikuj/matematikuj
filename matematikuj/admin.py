from django.contrib import admin
from .models import Menu_bloky,Pocetni_priklady,Tema

class Tema_SS_Admin(admin.ModelAdmin):
    list_display = ('tema', 'podtema', 'kapitola')

class Pocetni_priklady_SS_Admin(admin.ModelAdmin):
    list_display = ('tema', 'zadani', 'reseni' ) 

admin.site.register(Menu_bloky) 
admin.site.register(Tema, Tema_SS_Admin)

admin.site.register(Pocetni_priklady, Pocetni_priklady_SS_Admin)


# Register your models here.
