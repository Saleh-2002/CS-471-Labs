from django.contrib import admin
from .models import Student, Address

# Register models in the admin interface
admin.site.register(Student)
admin.site.register(Address)
