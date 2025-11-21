from django.db import models
#classe para criação de categorias de produtos

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) # URL amigável (ex: /camisetas)

    class Meta:
        ordering = ('name',) # Ordena por nome automaticamente
        verbose_name_plural = 'Categories' # Correção do plural no Admin

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField() 
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) # Sempre use Decimal para dinheiro!
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # Data de criação automática

    class Meta:
        ordering = ('-created_at',) # Os mais recentes aparecem primeiro
    
    def __str__(self):
        return self.name