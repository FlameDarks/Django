from django.db import models
class Catalog(models.Model):
    name=models.CharField(verbose_name="书籍类别",max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    name=models.CharField(verbose_name="书名",max_length=100)
    price=models.IntegerField(verbose_name="价格",default=0)
    cataId=models.ForeignKey(to=Catalog,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="书籍"
        verbose_name_plural=verbose_name