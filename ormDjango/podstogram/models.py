from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=20000, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Promotion(models.Model):
    id = models.AutoField(primary_key=True)
    name_prom = models.CharField(max_length=255)
    price = models.IntegerField()

    class Meta:
        db_table = 'promotion'
        managed = False


class Advertising_services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cost = models.IntegerField()

    class Meta:
        db_table = 'advertising_services'
        managed = False