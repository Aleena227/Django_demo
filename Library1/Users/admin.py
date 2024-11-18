from django.contrib import admin

# Register your models here.


from Users.models import CustomUser
admin.site.register(CustomUser)
