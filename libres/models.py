from django.db import models
from .checker import validate_file_extension
import os
from django.utils.html import mark_safe
     
class Category(models.Model):
    pos = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    name_slug = models.SlugField(max_length=50, blank=True, null=True, editable=False, unique=True)
    icon = models.ImageField(upload_to="categories/")
    
    def icon_view(self):
        return mark_safe(f'<img src="{self.icon.url}" width="300"')

    def __str__(self):
        return self.name
        
    def subcategory_count(self):
        return self.cat_subcat.count()#.filter(id = self.id)
        
    def get_thumb(self):
        return self.thumb.url
        
    
    def save(self, *a, **b):
        self.name_slug = "_".join(self.name.lower().split())
        super(Category, self).save(*a, **b)

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("Categories")
    
class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name="cat_subcat", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    #desc = models.TextField(blank=True)
    title_slug = models.SlugField(max_length=50, blank=True, null=True, editable=False, unique=True)
    thumb = models.ImageField(default="static/img/default.jpg", upload_to="sub_categories/", null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.category.name}"
    
    def save(self, *a, **b):
        self.title_slug = "_".join(self.title.lower().split())
        super(SubCategory, self).save(*a, **b)

    def file_url(self):
        return f"/library/{self.pk}"

    class Meta:
        verbose_name = ("Sub category")
        verbose_name_plural = ("Sub Categories")
        
        
def upload_file_to(instance, filename):
     return os.path.join('%s/' % instance.sub_category.title_slug, filename)

class FileUpload(models.Model):
    class MediaType(models.TextChoices):
        PDF = ("PDF", "pdf")
        VIDEO = ("VIDEO", "video")
        WORD = ("WORD", "word")
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="sub_cat", )
    title = models.CharField(max_length=60)
    uploaded_file = models.FileField(
        upload_to= upload_file_to,
        validators=[validate_file_extension]
        #max_upload_size=10485760
    )
    #uploaded_file = models.FileField()
    media_type = models.CharField(max_length=8, choices= MediaType.choices, default=MediaType.PDF)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}-{self.sub_category}"
    
    def save(self, *a, **b):
        self.title_slug = "_".join(self.title.lower().split())
        super(FileUpload, self).save(*a, **b)

    def file_url(self):
        return f"/library/{self.pk}"
    
    class Meta:
        verbose_name = ("file upload")
        verbose_name_plural = ("File Uploads")
