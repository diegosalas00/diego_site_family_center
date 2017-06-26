from django.db import models


# Create your models here.

snacks = (
    ('-- please select --', '- Please Select -'),
    ('pizzas', 'Pizzas'),
    ('chips', 'Chips'),
    ('ice cream', 'Ice Cream'),
    ('donuts', 'Donuts'),
    ('candies', 'Candies'),
    ('cookies', 'Cookies'),
    ('hot dogs', 'Hot Dogs'),
    ('hamburgers', 'Hamburgers')
)

drinks = (
    ('-- please select --', '- Please Select -'),
    ('coca cola', 'Coca Cola'),
    ('dr. pepper', 'Dr. Pepper'),
    ('pepsi', 'Pepsi'),
    ('fanta', 'Fanta'),
    ('sprite', 'Sprite'),
    ('apple juice', 'Apple Juice'),
    ('capri sun', 'Capri Sun')
)

activities = (
    ('-- please select --', '- Please Select -'),
    ('movie night', 'Movie Night'),
    ('laser tag', 'Laser Tag'),
    ('get lit', 'Get Lit'),
    ('family skating center', 'Family Skating Center'),
)


class Activity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', ]
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.title


class PartyPackage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0)
    activity = models.ForeignKey(Activity)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.title


class Snack(models.Model):
    snack = models.CharField(choices=snacks, max_length=255)


class Available(models.Model):
    name = models.CharField(max_length=250)
    activity = models.CharField(choices=activities, max_length=255)
    package = models.CharField(max_length=255)
    date_start = models.DateTimeField(auto_created=False)
    date_end = models.DateTimeField(auto_created=False)
    description = models.TextField(default="None")
    snack = models.CharField(max_length=255, choices=snacks, default="Not Shown")
    drink = models.CharField(max_length=255, choices=drinks, default="Not Shown")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', ]
        verbose_name_plural = 'Availabilities'

    def __str__(self):
        return self.name
