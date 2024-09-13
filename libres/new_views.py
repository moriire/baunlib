from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic

from .models import Category, SubCategory, FileUpload
context = {}
context["categories"] = Category.objects.all()

def index(request):
    return render(request, "new/landing.html")#redirect("/library/")
    
def about(request):
    return render(request, "about.html", {})
    
def contact(request):
    return render(request, "contact.html", {})

#For Open Roberta Lab
@method_decorator(login_required, name="dispatch")
class OpenRobertaView(generic.TemplateView):
    template_name = 'new/openroberta.html'

#For Kolibri
class KolibriView(generic.TemplateView):
    template_name = 'new/kolibri.html'

class CategoriesListView(generic.ListView):
    model = Category
    context_object_name = 'categories'
    queryset = Category.objects.order_by("pos")
    template_name = 'new/index.html'

def subcategory(request, subcat):
    context["tabs"] =  SubCategory.objects.all().filter(category__name_slug=subcat)
    context["title"] = " ".join(subcat.split("_"))
    return render(request, "new/subcategories.html", context=context)

#This
def files(request, cat, pk, media_type):
    q = SubCategory.objects.select_related('category').filter(category__name_slug=cat, title_slug=pk).first()
    q_all =  q.sub_cat.filter(media_type = media_type)
    context['medias'], context['count'] =  q_all, q_all.count()
    context['title'] = " ".join(pk.split("_"))
    context["link"] = "/".join(("library", cat, pk, media_type))
    context['pk'] = pk
    context['cat'] = cat 
    context['media_type'] = media_type.upper()
    return render(request, "new/media.html", context)

#@login_required
def media(request, cat, pk):
    context['media_type'] = media_type.upper()
    context['files'] =  FileUpload.objects.select_related('sub_category').filter(sub_category__title_slug=pk, media_type=media_type.upper())#.filter(media_type=media_type.upper())
    context['title'] = " ".join(pk.split("_"))
    context['pk'] = pk
    return render(request, "media.html", context)

class MediaDetail(generic.DetailView):
    context_object_name = 'file'
    template_name = "new/file.html"
    model = FileUpload
