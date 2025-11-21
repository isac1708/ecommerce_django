from django.contrib import admin
from .models import Category, Product

#admin para categorias de produtos permitindo criar categorias e produtos no banco de dados

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # Preenche o slug automaticamente enquanto digita o nome

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    list_editable = ['price'] # Permite editar preço direto na lista
    prepopulated_fields = {'slug': ('name',)}