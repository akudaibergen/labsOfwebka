from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=200)
    def take_category_json(self):
        return {
            'id':self.id,
            'name':self.name
        }

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    description=models.TextField(default='')
    count=models.IntegerField()
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE,default=None)

    def take_product_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'category_id': self.category_id.take_category_json()
        }
