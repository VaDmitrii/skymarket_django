from django.db import models
from django.db.models import CASCADE

from users.models import User


class Ad(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=150, null=True)
    author = models.ForeignKey(User, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/")

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        return self.image.url if self.image else None


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=CASCADE)
    ad = models.ForeignKey(Ad, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:50]

    @property
    def first_name(self):
        return self.author.first_name

    @property
    def last_name(self):
        return self.author.last_name

    @property
    def avatar_image(self):
        return self.author.image.url if self.author.image else None
