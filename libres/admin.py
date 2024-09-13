from django.contrib import admin
from libres.models import Category, FileUpload, SubCategory
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["icon_view", ]
    pass

@admin.register(FileUpload)
class FileUploadAdmin(admin.ModelAdmin):
    pass

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    pass
