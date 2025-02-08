from django.db import models

# Create your models here.

class CarModel(models.Model):
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField() 

    class Meta:
        unique_together = ('manufacturer', 'model', 'year')

    def __str__(self):
        return f"{self.manufacturer} {self.model} {self.year}"

class SparePart(models.Model):

    part_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    part_number = models.CharField(max_length=100, unique=True)
    manufacturer = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    min_stock = models.PositiveIntegerField(default=1)
    
    # car_model = models.CharField(max_length=200, null=False, blank=False, default='Toyota Camry 2020')
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="spare_parts")

    supplier = models.CharField(max_length=200, null=False, blank=False, default='Abdullah Zubair') 
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.part_name} {self.part_number}"

    def needs_restocking(self):
        return self.quantity <= self.min_stock

    def save(self, *args, **kwargs):
        self.is_available = self.quantity > 0
        super().save(*args, **kwargs)

    class Meta:

        ordering = ['added_on']
