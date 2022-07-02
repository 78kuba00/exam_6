from django.db import models


class Comment(models.Model):
    Statuses = (
        ('active', 'Активно'),
        ('blocked', 'Заблокировано'),
    )
    author = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=7, choices=Statuses, default='active')
