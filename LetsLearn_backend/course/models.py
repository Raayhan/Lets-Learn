from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    name  = models.CharField(max_length=255)
    slug  = models.SlugField()
    image = models.ImageField(upload_to='uploads/categories',blank=True,null=True)

    class Meta:
        ordering = ('name',)
        db_table = 'course_categories'

    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

class Course(models.Model):
    
    category    = models.ForeignKey(Category,related_name='courses', on_delete=models.CASCADE)
    title       = models.CharField(max_length=100)
    summary     = models.CharField(max_length=255)
    slug        = models.SlugField()
    author      = models.ForeignKey(User,related_name='courses', on_delete=models.CASCADE)
    description = CKEditor5Field('Text', config_name='extends')
    date_added  = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-date_added',)

    
    def __str__(self):
        return self.title
    
    
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'