from django.contrib import admin
from .models import Post, PostWod

class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'created_at')
    search_fields = ('text', 'author__username')

    def save_model(self, request, obj, form, change):
        if not obj.author:  # Se o campo usuario não estiver preenchido
            obj.author = request.user  # Preenche com o usuário logado
        super().save_model(request, obj, form, change)




admin.site.site_header = "Administração CF4Time"
admin.site.register(Post, PostAdmin)
admin.site.register(PostWod)
