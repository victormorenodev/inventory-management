from django.db import models
from cloudinary.models import CloudinaryField


# Company model
class company(models.Model):
    idCompany = models.AutoField(primary_key=True)
    nameCompany = models.TextField(max_length=255)
    logo = CloudinaryField('Image', overwrite = True, format="jpg")
    email = models.EmailField(max_length=254, unique=True)
    tel = models.CharField(max_length = 15)
    document = models.CharField(max_length = 18)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-idCompany',)
    def __str__(self):
        return self.nameCompany

#products model
class products(models.Model):
    idProduct = models.AutoField(primary_key=True)
    nameProduct = models.TextField(max_length=255)
    amount = models.IntegerField(default=0)
    #supplier = models.ForeignKey(suppliers, on_delete=models.CASCADE)
    #category = models.ForeignKey(categorys, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    #last_change_by = models.ForeignKey(users, on_delete=models.SET_NULL, null = True, blank= True) # no futuro ver a utiliação do on_delete, deleção do usuario

    def save_last_user_change(self, user): # Recebe um user e salva no ultimo que alterou
        self.last_change_by = user
        self.save()

    class Meta: # metadata for the model
        ordering = ('-updated_at',)
    
    def __str__(self): 
        return self.nameProduct