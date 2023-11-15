from django.contrib import admin
from .models import contactTable, Blog
@admin.register(contactTable)
class studentAdmin(admin.ModelAdmin):
    list_display=('id','name','email','phoneno','message')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('id','title','des')