from django.urls import path

from .views import (
    news_list, 
    news_detail, 
    create, 
    remove, 
    my_create,
    my_news,
    my_update,
    my_detail,
)

app_name = "new"
urlpatterns =[
    path('', news_list, name="list"),
    path('<int:id>/', news_detail, name="detail"),
    path('Yaratish/', create, name="create"),
    path('remove/<int:id>/', remove, name="remove"),
    path('my-news/', my_news, name="my_news"),
    path('my-create/', my_create, name="my_create"),
    path('my-update/<int:id>/', my_update, name="my_update"),
    path('my-detail/<int:id>/', my_detail, name="my_detail"),
]