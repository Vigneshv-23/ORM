# Ex02 Django ORM Web Application
## Date: 29-02-2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![alt text](<WhatsApp Image 2024-03-01 at 08.15.22_7246cde5.jpg>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
## MODELS
```
from django.db import models
from django.contrib import admin
class books(models.Model):
	name=models.CharField(max_length=20);
	author=models.CharField(max_length=20);
	id=models.IntegerField(primary_key=True);
	copies=models.IntegerField();
	price=models.IntegerField();
class booksAdmin(admin.ModelAdmin):
	list_display=("name","author","id","copies","price");
```
## ADMIN
```
from django.contrib import admin
from .models import books,booksAdmin
admin.site.register(books,booksAdmin)
```

## OUTPUT

![alt text](<Screenshot 2024-02-27 193711.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
