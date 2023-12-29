from django.contrib import admin

from.models import Post, Comment, Category

class CommentItemInline(admin.TabularInline):
	model = Comment
	raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
	search_fields = ['title', 'intro', 'body']
	list_display = ['title', 'category', 'slug', 'created_at', 'status']
	list_filter = ['category', 'created_at', 'status']
	inlines = [CommentItemInline]
	prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ['title']
	prepopulated_fields = {'slug': ('title',)} #auto fill slug field

class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'post', 'created_at']
	search_fields = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
