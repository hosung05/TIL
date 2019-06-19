from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "posts"

urlpatterns = [
    # Read - 전체글보기
    path('', views.index, name="index"),
    # Create - 포스트 작성하기
    path('create/', views.create, name="create"),
    # Update - 포스트 수정하기
    path('<int:post_id>/update/', views.update, name="update"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)