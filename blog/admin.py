from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('title','status','date')
	list_filter = ('date',)
	search_fields = ['title','content']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'reply', 'post', 'date', 'active')
    list_filter = ('active', 'date')
    search_fields = ('author',  'reply')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
	
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)