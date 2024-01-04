from django.db import models


# Create your models here.

class MeasureUnits(models.Model):
    name = models.CharField(max_length=255)

    objects = models.Manager()


class Groups(models.Model):
    name = models.CharField(max_length=255)


class Ingredients(models.Model):
    measurement_unit = models.ForeignKey(MeasureUnits, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    price = models.FloatField()

    def format(self):
        add_table = self.additionaltableci_set.first()
        return {
                'measurement_unit': self.measurement_unit.name,
                'name': self.name,
                'price': self.price,
                'add_table': add_table.format()

        }


class CompoundIngredients(models.Model):
    title = models.CharField(max_length=255)
    measurement_unit = models.ForeignKey(MeasureUnits, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredients)


class AdditionalTableCI(models.Model):
    ingredients = models.ManyToManyField(Ingredients)
    compound_ingredients = models.ManyToManyField(CompoundIngredients)
    calculation_qty = models.FloatField()
    sum = models.FloatField()
    quantity = models.FloatField()


    def format(self):
        return {
                'calculation_qty': self.calculation_qty,
                'sum': self.sum,
                'quantity': self.quantity,

        }

