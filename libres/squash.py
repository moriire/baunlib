from django.db.models.signals import post_delete
from .models import Category, SubCategory, FileUpload
from django.dispatch import receiver
import os

@receiver(post_delete,sender=Category)
def delete_category(sender,instance,*args,**kwargs):
	to_be_deleted = instance.icon.path
	to_be_deleted_exists = os.path.isfile(to_be_deleted)
	if to_be_deleted_exists:
		os.remove(to_be_deleted)
		print("Category associated file(s) Deleted")
        
@receiver(post_delete,sender=SubCategory)
def delete_subCategory(sender,instance,*args,**kwargs):
	to_be_deleted = instance.thumb.path
	print(instance)
	to_be_deleted_exists = os.path.isfile(to_be_deleted)
	if to_be_deleted_exists:
		os.remove(to_be_deleted)
		print("Sub Category associated file(s) Deleted")
        

@receiver(post_delete,sender=FileUpload)
def delete_fileUpload(sender,instance,*args,**kwargs):
	to_be_deleted = instance.uploaded_file.path
	to_be_deleted_exists = os.path.isfile(to_be_deleted)
	if to_be_deleted_exists:
		os.remove(to_be_deleted)
		print("Sub Category associated file(s) Deleted")
        
