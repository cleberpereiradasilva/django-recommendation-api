from django.contrib import admin
from .models import Post, PostView, Tag

class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)


class PostTagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, PostTagAdmin)


class PostViewAdmin(admin.ModelAdmin):
    pass
admin.site.register(PostView, PostViewAdmin)