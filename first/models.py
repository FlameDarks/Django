from django.db import models
class Book(models.Model):
    name=models.CharField(verbose_name="书名",max_length=100)
    price=models.IntegerField(verbose_name="价格",default=0)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="书籍"
        verbose_name_plural=verbose_name