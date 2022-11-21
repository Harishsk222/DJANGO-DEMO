from django.contrib import admin
from .models import Banglore,Mumbai,Chennai
# Register your models here.


# Admin Register page for Banglore
#_________________________________________________________________


class BangloreAdmin(admin.ModelAdmin):
    l=['Date','Bl1','Bl2','Bl3','Bl4','Bl5']
    
admin.site.register(Banglore,BangloreAdmin)


# Admin Register page for Mumbai
#_________________________________________________________________

class MumbaiAdmin(admin.ModelAdmin):
    l=['Date','Ml1','Ml2','Ml3','Ml4']
    
admin.site.register(Mumbai,MumbaiAdmin)




# Admin Register page for Mumbai
#_________________________________________________________________

class ChennaiAdmin(admin.ModelAdmin):
    l=['Date','Cl1','Cl2','Cl3']
    
admin.site.register(Chennai,ChennaiAdmin)