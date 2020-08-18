from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price_32 = models.DecimalField(max_digits=4, decimal_places=2)
    price_42 = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')

    def __str__(self):
        return self.name