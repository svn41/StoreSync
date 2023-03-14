from django.db import models

class MaterialMaster(models.Model):
    materialID = models.AutoField(primary_key=True)
    materialName = models.CharField(max_length=150, null=False, blank=False)
    specifications = models.CharField(max_length=150, null=False, blank=False)
    minimum_quantity = models.IntegerField(null=False, blank=False)
    CATEGORY_CHOICES = [
        ('category1', 'Product'),
        ('category2', 'Service'),
        ('category3', 'Tools'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=False, blank=False)
    UNIT_CHOICES = [
        ('unit1', 'Kg'),
        ('unit2', 'Liter'),
        ('unit3', 'Pcs'),
        ('unit4', 'Feet'),
        ('unit5', 'Inch'),
    ]
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES, null=False, blank=False)

    def __str__(self):
        return str(self.materialID) + " " + self.materialName + " " + self.specifications
