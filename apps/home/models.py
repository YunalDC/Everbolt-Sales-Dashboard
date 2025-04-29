from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', default='profile_images/default-avatar.png')

    def __str__(self):
        return self.user.username

class CustomerOrder(models.Model):
    customer_name = models.CharField(max_length=255)
    order_count = models.PositiveIntegerField()
    revenue = models.DecimalField(max_digits=15, decimal_places=2)
    salesperson = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.salesperson.username}"


class Visit(models.Model):
    visit_date = models.DateField()
    sales_officer = models.CharField(max_length=100)
    company = models.CharField(max_length=255)
    visit_type = models.CharField(max_length=100)
    visit_details = models.TextField(blank=True)
    remarks = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company} - {self.visit_date}"


class Product(models.Model):
    part_number = models.CharField(max_length=100, unique=True)
    name = models.TextField()
    brand = models.CharField(max_length=100)
    quantity_on_hand = models.IntegerField(default=0)
    unit_of_measure = models.CharField(max_length=50, default="Units")
    sales_price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.part_number} - {self.name}"


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100)
    client = models.CharField(max_length=255)
    invoice_date = models.DateField()
    due_date = models.DateField()
    salesperson = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.invoice_number

class InvoiceItem(models.Model):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, related_name='items')
    product_name = models.CharField(max_length=255, default="Unknown Product")  # Store the product name directly
    brand = models.CharField(max_length=100, blank=True, default=0)
    part_number = models.CharField(max_length=100, blank=True, default=0)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField()
    line_total = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Calculate the line_total based on the unit price and quantity
        self.line_total = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_name} - {self.invoice.invoice_number}"

class AgedReceivable(models.Model):
    customer_name = models.CharField(max_length=255)
    salesperson = models.CharField(max_length=100)

    days_1_30 = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    days_31_60 = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    days_61_90 = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    days_91_120 = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    older = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    last_invoice_date = models.DateField(null=True, blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.salesperson}"

    

