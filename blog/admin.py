from django.contrib import admin
from .models import Blog
from .models import comment
admin.site.register(Blog)

# Register your models here.
@admin.register(comment)
class commentadmin(admin.ModelAdmin):
    list_display = ('id','body','author')
