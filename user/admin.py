from django.contrib import admin
from .models import *
# Register your models here.
class tblgalleryAdmin(admin.ModelAdmin):
    list_display=("id", "title","image")
admin.site.register(tblgallery,tblgalleryAdmin)

class tblreservationAdmin(admin.ModelAdmin):
    list_display=("id", "Full_Name","Phone","email","guests","date","time","special_requests","status")
admin.site.register(tblreservation,tblreservationAdmin)

class tblContactAdmin(admin.ModelAdmin):
    list_display=("id", "Full_Name","Phone","email","Message")
admin.site.register(tblContact,tblContactAdmin)

class tblreviewAdmin(admin.ModelAdmin):
    list_display=("id", "Full_Name","Feedback","Image")
admin.site.register(tblreview,tblreviewAdmin)

class tblloginAdmin(admin.ModelAdmin):
     list_display=("id", "Email","password")
admin.site.register(tbllogin,tblloginAdmin)

class tblregisterAdmin(admin.ModelAdmin):
    list_display=("id", "Full_Name","mobile","Email","Password","Image","Address")
admin.site.register(tblregister,tblregisterAdmin)
