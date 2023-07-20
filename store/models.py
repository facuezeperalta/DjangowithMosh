from django.db import models

# Create your models here.
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    #in many to many relationship we need to define the relationship in the product that shows to the user and Django will automatically shows the discount to the user and also make the relationship between the producto class and the promotion class.
    #product_set returns all the productos that a particular promotion is applied to.

class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
class Product(models.Model):
    title = models.CharField(max_length=255,null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) #arguments required ALWAYS
    stock = models.IntegerField()
    last_update =models.DateTimeField(auto_now=True) # cada vez que acutalicemos el objeto se guaradará de manera automática
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT) #Protejemos en el caso de borrar una collection no perdemos todos los productos.
    promotions = models.ManyToManyField(Promotion) #now django creates the reverse relationship in the Promotion class. realted  related_name='products' changes the deafult value of the name of the field of the promotion class. Its better to keep it consistent in all the project to keep it clean.

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),
    ]
    
    firs_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    

class Order(models.Model):
    #order never be deleted cause they represent our sales.
    PENDING = 'P'
    COMPLETE = 'C'
    FAILED = 'F'
    PAYMENT_STATUS_CHOICES  = [
        (PENDING,'Pending'),
        (COMPLETE,'Complete'),
        (FAILED,'Failed'),
    ] 
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PENDING)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField() #prevent negative values store in this field
    unit_price = models.DecimalField(max_digits=6,decimal_places=2) #the price of the product should be store at the time of creating the order.

class Addres(models.Model): #Addres is the child of customer
    street= models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) #if a delete a custmer the addres will be deleted too.

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    #one to many relationship
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
















