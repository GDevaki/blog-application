from django.contrib import admin
from .models import Post,category,AboutUs

class PostAdmin(admin.ModelAdmin):
    list_display=('title','content')
    search_fields=('title','content')
    list_filter=('category','created_at')

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(category)
admin.site.register(AboutUs)


