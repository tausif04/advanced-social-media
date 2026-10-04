from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'short_content', 'created_at', 'has_image')
    list_filter = ('created_at',)
    search_fields = ('content', 'author__username')

    @admin.display(description='Content')
    def short_content(self, obj):
        return obj.content[:60]

    @admin.display(boolean=True, description='Image')
    def has_image(self, obj):
        return obj.has_image
