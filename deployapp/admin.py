from django.contrib import admin
from .models import DeployModel

class DeployAdmin(admin.ModelAdmin):
    list_display =['name', 'email']
    
admin.site.register(DeployModel, DeployAdmin)    

# Register your models here.
