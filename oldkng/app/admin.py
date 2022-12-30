from django.contrib import admin
from .models import Catogery,SubCatogery,AddData
# Register your models here.

@admin.register(SubCatogery)
class SubCatogeryAdmin(admin.ModelAdmin):
    list_display = ('cat','name','mrp')

@admin.register(AddData)
class SubCatogeryAdmin(admin.ModelAdmin):
    list_display = ('id','catogery','sub_catogery','mrp','quantity','total','date')

@admin.register(Catogery)
class CatogeryAdmin(admin.ModelAdmin):
    list_display = ('id','name')