from django.contrib import admin
from .models import CarMake, CarModel


# Inline model to display CarModels inside CarMake admin page
class CarModelInline(admin.StackedInline):  # You can use admin.TabularInline if preferred
    model = CarModel
    extra = 1  # Number of empty forms displayed


# Custom admin view for CarModel
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'dealer_id')
    list_filter = ('car_make', 'type', 'year')
    search_fields = ('name', 'car_make__name')


# Custom admin view for CarMake with inline CarModels
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [CarModelInline]


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
