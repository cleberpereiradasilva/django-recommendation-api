from django.contrib import admin
from .models import Post, PostView, Tag, User

class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)


class PostTagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tag, PostTagAdmin)


class PostViewAdmin(admin.ModelAdmin):
    pass
admin.site.register(PostView, PostViewAdmin)

class UserViewAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserViewAdmin)