from django.contrib import admin

from .models import Post , comment

class commendInline(admin.TabularInline):
    model = comment
    fields = ['text',]
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_enable','publish_date','created_time']
    inlines = [commendInline,]


#class commendAdmin(admin.ModelAdmin):
#    list_display = ['post','text','created_time']

admin.site.register(Post,PostAdmin)
#admin.site.register(comment,commendInline)
