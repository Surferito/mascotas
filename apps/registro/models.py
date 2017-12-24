from django.db import models

# Create your models here.
class Registro(models.Model):
    email = models.EmailField()

    def __str__(self):
        return '{} | {}'.format(self.id, self.email)