from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        upload_to='posts/images',   # 올리는 위치 설정
        processors=[ResizeToFill(600, 600)],
        format='JPEG',
        options={'quality': 90}     # 원본 대비 품질 설정
    )