from django.db import models
from django.db.models import Manager
from mptt.models import MPTTModel
from mptt.managers import TreeManager
# Create your models here.

class Category(MPTTModel):
    name = models.CharField(max_length=128, verbose_name="分类名称")
    description = models.CharField(max_length=128, verbose_name="描述")
    parent = models.ForeignKey('self', null=True, blank=True, related_name="children", verbose_name="父类", on_delete='CASCADE')
    objects = Manager()
    tree = TreeManager()

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=128, verbose_name="品牌名称")
    index = models.IntegerField(default=1, verbose_name="排序")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name
        ordering = ['index', ]

    def __str__(self):
        return self.name


class Size(models.Model):
    SIZE_S = 'S'
    SIZE_M = 'M'
    SIZE_L = 'L'
    SIZE_CHOICES = (
        (0, SIZE_S),
        (1, SIZE_M),
        (2, SIZE_L),
    )
    name = models.IntegerField(verbose_name="尺寸", choices=SIZE_CHOICES)
    index = models.IntegerField(default=1, verbose_name="排序")

    class Meta:
        verbose_name = "尺寸"
        verbose_name_plural = verbose_name
        ordering = ['index', ]

    def __str__(self):
        if self.name == 0:
            return self.SIZE_S
        elif self.name == 1:
            return self.SIZE_M
        else:
            return self.SIZE_L


class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name="名称")
    index = models.IntegerField(default=1, verbose_name="排序")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="名称")
    brand = models.ForeignKey(Brand, verbose_name="品牌", on_delete="CASCADE")
    size = models.ManyToManyField(Size, verbose_name="尺寸大小")
    price = models.FloatField(default=0, verbose_name="原价")
    newprice = models.FloatField(default=0, verbose_name="折扣价")
    discount = models.FloatField(default=0, verbose_name="折扣")
    sales = models.IntegerField(default=0, verbose_name="销量")
    desc = models.CharField(max_length=128, verbose_name="描述")
    tag = models.ManyToManyField(Tag, verbose_name="标签")
    num = models.IntegerField(default=0, verbose_name="库存")
    image = models.ImageField(upload_to="product/%Y%m", verbose_name="图片")
    categories = models.ManyToManyField(Category, verbose_name="分类")
    active = models.BooleanField(default=True, verbose_name="是否有效")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name
        ordering = ['id', ]


    def get_first_category(self):
        for category in self.categories.all():
            return category
        return None


    def __str__(self):
        return self.name
