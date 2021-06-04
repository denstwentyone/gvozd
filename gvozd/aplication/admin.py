from django.contrib import admin
from .models import Aplications, Favour

class FavourAdmin(admin.ModelAdmin):
    list_display = ('id','name','price')
    list_filter = ('id',)

class AplicationsAdmin(admin.ModelAdmin):
    def favour(obj):
        return obj.favour.name + ' ' + str(obj.favour.price)
    list_display = ('id','first_name','date','email',favour)
    list_filter = ('id',)


admin.site.register(Favour,FavourAdmin)
admin.site.register(Aplications,AplicationsAdmin)

