from django.db import models
from django.urls import reverse

# products in the database.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # returns the canonical URL for a single product.
        return reverse('shop:product_detail', args=[str(self.id)])