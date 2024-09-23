from django.contrib import admin
from django.urls import path, include, re_path
from aitutor.views import router
admin.site.site_header = 'Baun Digital Library Admin'
admin.site.site_title = "Baun Lib"
admin.site.index_title = "Baun Digital Site administration"
admin.site.site_url = "/library/"

from django.conf import settings
from django.conf.urls.static import static
#from django.views.static import serve

from libres.views import index, categories, files, subcategory, media, about, contact
from libres import new_views  as new_views
urlpatterns = [
   path("", new_views.index, name="home"),
   path("robotics/", new_views.OpenRobertaView.as_view(), name="openroberta"),
   path("kolibri/", new_views.KolibriView.as_view(), name="kolibri"),
   path("library/<str:cat>/<str:pk>/<str:media_type>/", new_views.files, name="media"),
   re_path(r"^library/$", new_views.CategoriesListView.as_view(), name="categories"),
   path("library/<int:pk>/", new_views.MediaDetail.as_view(),  name="media_detail"),
   path('library/', include('django.contrib.auth.urls')),
   path("library/<str:subcat>/", new_views.subcategory, name="sub_categories"),
   path('admin/', admin.site.urls),
   path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
	path('ai/', include(router.urls)),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
