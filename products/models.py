from django.db import models
from django.utils import timezone


class Product(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=221)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=3, default=99.99)
    created_at = models.DateField(default=timezone.now, null=True)

    @property
    def sale_price(self):
        return "%.3f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "122"

