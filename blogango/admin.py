from django.contrib import admin

from blogango.models import Blog, BlogEntry, Comment, BlogRoll, Reaction, BlogCategory

class BlogEntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('created_by',)
    list_display = ('thumbnail_html_image','title', 'category', 'is_published', 'is_page', 'publish_date')
    list_editable = ('category',)

class BlogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog)
admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(Comment)
admin.site.register(BlogRoll)
admin.site.register(Reaction)
admin.site.register(BlogCategory,BlogCategoryAdmin)