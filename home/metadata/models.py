from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='locations')
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name



class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name


class Sku(models.Model):
    sku = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='location')
    department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='department')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name='subcategory')

    def save(self, *args, **kwargs):
        if not self.sku:
            last_sku = Sku.objects.order_by('-sku').first()
            self.sku = (last_sku.sku + 1) if last_sku else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
