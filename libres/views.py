from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Category, SubCategory, FileUpload
context = {}
context["categories"] = Category.objects.all()
def index(request):
    return render(request, "index.html")#redirect("/library/")
    
def about(request):
    return render(request, "about.html", {})
    
def contact(request):
    return render(request, "contact.html", {})

def categories(request):
    categories =  Category.objects.all().order_by("pos")
    return render(request, "categories.html", {"categories": categories})

def subcategory(request, subcat):
    context["tabs"] =  SubCategory.objects.all().filter(category__name_slug=subcat)
    context["cat_title"] = " ".join(subcat.split("_"))
    return render(request, "subcategory.html", context=context)


def files(request, cat, pk):
    context['files'] =  FileUpload.objects.select_related('sub_category').filter(sub_category__title_slug=pk)
    context['title'] = " ".join(pk.split("_"))
    context['formats'] = ('pdf', 'word', 'video')
    context["link"] = "/".join(("library", cat, pk))
    #links = map(lambda f: context.get("link")/f, formats)
    return render(request, "files.html", context)

@login_required
def media(request, cat, pk, media_type):
    context['media_type'] = media_type.upper()
    context['files'] =  FileUpload.objects.select_related('sub_category').filter(sub_category__title_slug=pk, media_type=media_type.upper())#.filter(media_type=media_type.upper())
    context['title'] = " ".join(pk.split("_"))
    return render(request, "media.html", context)
