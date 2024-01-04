from django.db import models

# blya

class Cashbox(models.Model):
    name = models.CharField(max_length=255)


class TransactionGroup(models.Model):
    TRANSACTION_GROUP_KIND_OF_ACTIVITY_CHOICES = [
        ('operating', 'Operating'),
        ('investment', 'Investment'),
        ('financial', 'Financial')
    ]

    name = models.CharField(max_length=255)
    kind_of_activity = models.CharField(max_length=50, choices=TRANSACTION_GROUP_KIND_OF_ACTIVITY_CHOICES)
    transaction_category = models.CharField(max_length=50)


class Customer(models.Model):
    id = models.IntegerField(primary_key=True)

class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('expense', 'Expense'),
        ('income', 'Income'),
        ('transfer', 'Transfer')
    ]
    date = models.DateTimeField()
    terminal = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=TRANSACTION_TYPE_CHOICES)
    sender_cashier_id = models.IntegerField()
    recepient_cashier_id = models.ForeignKey(Cashbox, on_delete=models.PROTECT, related_name='rec_cashier')
    transaction_group_id = models.ForeignKey(TransactionGroup, on_delete=models.PROTECT, related_name='trans_group')
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, related_name='customer')
    transaction_category = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=50)
    amount = models.FloatField()
    description = models.CharField(max_length=255)


class Promotion(models.Model):
    PROMOTION_BONUS_TYPE_CHOICES = [
        ('dish', 'Dish'),
        ('discount', 'Discount'),
        ('card_ball', 'Card Ball'),
        ('discount_to_card', 'Discount to Card'),
        ('deposite_to_card', 'Deposite to Card')
    ]
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()

    days = models.CharField(max_length=255)

    picture = models.TextField()
    order_type = models.CharField(max_length=30)
    only_for_customers = models.BooleanField(default=False)
    combine_with_other_promotions = models.BooleanField(default=False)
    bonus_type = models.CharField(max_length=130, choices=PROMOTION_BONUS_TYPE_CHOICES)
    condition = models.CharField(max_length=255)

class Restaurant(models.Model):
    pass


class Balance(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant')
    amount = models.FloatField(default=0.0)


class Tariff(models.Model):
    name = models.CharField(max_length=255)


class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    tariff_id = models.ForeignKey(Tariff, on_delete=models.CASCADE, related_name='service')


class PartnerRestaurants(models.Model):
    name = models.CharField(max_length=120)
    last_sync_date = models.DateTimeField()
    active_until = models.DateTimeField()
    last_payment_date = models.DateField()
    #??????
    payments = models.CharField(max_length=255)
    #??????





class Delivery(models.Model):
    DELIVERY_TYPE_CHOICES = [
        ('delivery', 'Delivery'),
        ('pickup', 'Pickup')
    ]

    DELIVERY_PAYMENT_TYPE_CHOICES = [
        ('cash', 'Cash'),
        ('online_payment', 'Online Payment')
    ]
    restaurant_id = models.IntegerField()
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='customer')
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    number_of_guests = models.IntegerField(default=1)
    discount_amount = models.FloatField(default=0)
    discount_measurement = models.CharField(max_length=255)
    items = models.ForeignKey('Item', on_delete=models.PROTECT, related_name='iten')
    _type = models.CharField(max_length=255, choices=DELIVERY_TYPE_CHOICES)
    payment_type = models.CharField(max_length=255, choices=DELIVERY_PAYMENT_TYPE_CHOICES)
    asap = models.BooleanField(default=False)
    delivery_time = models.TimeField()
    price = models.FloatField()
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        db_table = 'delivery'
        verbose_name_plural = 'deliveries'


class Relation(models.Model):
    pass
