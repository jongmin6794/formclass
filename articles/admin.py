from django.contrib import admin
from .models import Article, Comment
#import Article 이 Article은 models의 클래스 Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','created_at','updated_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content',)

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment, CommentAdmin)