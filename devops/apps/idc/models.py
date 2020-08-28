from django.db import models

# Create your models here.

class Idc(models.Model):
    name = models.CharField("idc名称", max_length=100, blank=False, null=True, help_text="IDC名称")
    address = models.CharField("idc的地址", max_length=200, default="", help_text="IDC地址")
    phone = models.CharField("idc的联系电话", max_length=20, null=True, help_text="IDC联系电话")
    email = models.CharField("IDC的email联系地址", max_length=50, help_text="IDC联系eamil")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "idc"