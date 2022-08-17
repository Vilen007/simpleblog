from django.contrib import admin


from blog.models import post,blogs_comment
# Register your models here.
admin.site.register((blogs_comment))

@admin.register(post)


class postAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)