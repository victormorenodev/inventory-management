from django.db import models
from cloudinary.models import CloudinaryField
from Django.contrib.auth.models import Permission

# company model
class company(models.Model):
    idCompany = models.AutoField(primary_key=True)
    nameCompany = models.TextField(max_length=255)
    logo = CloudinaryField('Image', overwrite = True, format="jpg")
    email = models.EmailField(max_length=254, unique=True)
    document = models.CharField(max_length = 18)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-idCompany',)
    def __str__(self):
        return self.nameCompany

# Suplliers model
class suplliers(models.Model):
    idsupllier = models.AutoField(primary_key=True)
    namesupllier = models.TextField(max_length=255)
    logo = CloudinaryField('Image', overwrite = True, format="jpg")
    email = models.EmailField(max_length=254, unique=True)
    tel = models.CharField(max_length = 15)
    document = models.CharField(max_length = 18)

    def __str__(self):
        return self.namesupllier

# Categories model
class categories(models.Model):
    idcategories = models.AutoField(primary_key=True)
    name = models.TextField(max_lentgh=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# users model
class users(models.Model):
    id_user = models.AutoField(primary_key=True)
    name_user = models.TextField(max_lentgh=255)
    email = models.EmailField(max_length=254, unique=True)
    document = models.EmailField(max_lentgh=55, unique=True)
    password = models.CharField(max_length=128)
    permission = models.ManyToManyField(Permission, related_name='users', blank=True) # usa a classe Permission, pro controle de permissões de um usuario

    def __str__O(self):
        return self.name_user

# products model
class products(models.Model):
    idProduct = models.AutoField(primary_key=True)
    nameProduct = models.TextField(max_length=255)
    amount = models.IntegerField(default=0)
    supplier = models.ForeignKey(suplliers, on_delete=models.CASCADE)
    categorie = models.ForeignKey(categories, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    last_change_by = models.ForeignKey(users, on_delete=models.SET_NULL, null = True, blank= True) # no futuro ver a utiliação do on_delete, deleção do usuario

    def save_last_user_change(self, user): # Recebe um user e salva no ultimo que alterou
        self.last_change_by = user
        self.save()
    
    def __str__(self): 
        return self.nameProduct
    