from django.contrib import admin
from .models import Location,Department,Category,Sku,SubCategory

admin.site.register(Location)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Sku)
# Register your models here.
