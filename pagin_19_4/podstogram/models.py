from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=20000, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title