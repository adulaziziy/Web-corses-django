from django.urls import URLPattern, path

from .views import my_view, gallery_view

app_name ="extra"
urlpatterns = [
    path('', my_view, name="my_view"),
    path("gallery/", gallery_view, name="gallery")
]