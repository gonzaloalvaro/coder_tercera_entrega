from django.contrib import admin

# Register your models here.


from stock.models import remeras, buzos, pantalones 

admin.site.register(remeras)
admin.site.register(buzos)
admin.site.register(pantalones)