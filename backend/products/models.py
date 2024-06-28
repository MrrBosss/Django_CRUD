import random
from django.conf import settings 
from django.db import models
from django.db.models import Q

User = settings.AUTH_USER_MODEL #auth.user


TAGS_MODELS_VALUES = ['electronics', 'cars','boats','movies','cameras']

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs
    


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)
    

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class ProductWeight(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)


class FAQ(models.Model):
    question = models.CharField(max_length=500, null=True)
    answer = models.CharField(max_length=500, null=True)

    def __str__(self):
        return str(self.question)


# class ProductRetrieve(models.Model):
#     weights = models.IntegerField(null=True)


class Banner(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=500, null=True)
    subtitle = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=250, null=True)


class Brand(models.Model):
    brands = models.ImageField(upload_to="products", null=True)
    name = models.CharField(max_length=500, null=True)

    def __str__(self):
        return str(self.brands)
    

class Product(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120, null=True)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99) 
    public = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products", null=True, blank=True)
    objects = ProductManager()
    weight = models.ManyToManyField(ProductWeight)
    # faq = models.ManyToManyField(FAQ)
    # banner = models.ManyToManyField(Banner)
    # brand = models.ManyToManyField(Brand) Bula alohida turishi kere product ga taaluqli joyi yoq



    def get_absolute_url(self):
        return f"/api/products/{self.pk}/"

    
    def __str__(self) -> str:
        return str(self.title)
    
    
    @property
    def endpoint(self):
        return self.get_absolute_url()

    
    @property
    def path(self):
        return f"/products/{self.pk}/"

   
    @property
    def body(self):
        return self.content

    
    def is_public(self): # returns bool
        return self.public #True or False
    
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODELS_VALUES)]
        
    
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    

    def get_discount(self):
        return '123'


class ProductList(models.Model):
    title = models.CharField(max_length=120, null=True)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99) 
    public = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products", null=True, blank=True)
    objects = ProductManager()
    weight = models.ManyToManyField(ProductWeight)
    faq = models.ManyToManyField(FAQ)
    banner = models.ManyToManyField(Banner)
    brand = models.ManyToManyField(Brand)
