from django.db import models
from django.conf import settings
# settings.AUTH_USER_MODEL
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    #Foreingnkey = 1:N 의 관계를 맺게 해줌(인자로 1의 관계를 넣어줌)


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # CASCADE = 폭포(1 : N의 관계에서 위의 1인 게시물이 삭제되면 같이 삭제)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

