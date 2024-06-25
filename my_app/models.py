from django.db import models

# Create your models here.
class MonkeyBarMenuItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_title = models.CharField(max_length=225)
    product_description = models.TextField()
    product_cost = models.IntegerField()
    product_stock = models.IntegerField()
    amount_sold = models.IntegerField()

    def __str__(self):
        return self.product_title

class MonkeyBarEmployee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=225)
    salary = models.IntegerField()

    def __str__(self):
        return self.name