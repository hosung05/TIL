from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),

    # Create
    path('new/', views.new_article),   # /board/new
    path('create/', views.create_article),    # /board/create/

    # Read
    path('', views.article_list),   # /board/
    path('<int:article_id>/', views.article_detail),    # /board/1/

    # Update

    path('<int:article_id>/edit/', views.edit_article),  # /board/edit
    path('<int:article_id>/update/', views.update_article),   #/board/update


    # Delete
    path('<int:article_id>/delete/', views.delete_article),
]
