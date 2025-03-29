from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# Create your models here.

class Notes(models.Model):
    
    CATEGORY = (
        ("BUSINESS", 'Business'),
        ('PERSONAL', 'personal'),
        ('IMPORTANT', 'important')
    )
    title = models.CharField(max_length=100)
    body = models.TextField()
    category = models.CharField(max_length=15, choices=CATEGORY)
    slug = models.SlugField(unique=True,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Notes'
        
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_base = slugify(self.title)
            slug = slug_base
            
            if Notes.objects.filter(slug=slug).exists():
                slug = f'{slug_base}-{get_random_string(5)}'
                
            self.slug = slug
                
        return super(Notes,self).save(*args,**kwargs)
    