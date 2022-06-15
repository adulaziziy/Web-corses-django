from django.urls import path
from .views import (
    savollar,
    savol_detail,
    check_answer,
    creat_question,
    create_group,
    group,
    remove_group,
    edit_group,
    create_choice,
) 
app_name = 'poll'
urlpatterns = [
    path('', savollar, name="savollar"),
    path('savol/<int:id>/', savol_detail, name="savol"),
    path('check/<int:variant_id>/', check_answer, name="check_answer"),
    path('creat_question/',creat_question, name="creat"),
    path('create_group/',create_group, name="create"),
    path('groups/', group, name="groups"),
    path('remove-group/<int:id>/', remove_group, name="remove_group"),
    path('edit-group/<int:id>/', edit_group, name="edit_group"),
    path('tanlov-yaratish/', create_choice, name="create_choice")
]

