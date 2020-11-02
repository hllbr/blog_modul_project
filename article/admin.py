from django.contrib import admin

from . models import Article
# Register your models here.
#Decoreder herzaman fonkisyonlarla kullanılmıyor bazen classlarla da kullanılabiliyor
#python bir class içerisine bir başka class yazılmasına müsade edcek esnekliği yazılımcısına sunuyor Django bunu öneriyor
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"] 
    list_display_links = ["title","created_date"]
    search_fields = ["title"]
    list_filter = ["content","author","created_date"]
    class Meta:
        model= Article


