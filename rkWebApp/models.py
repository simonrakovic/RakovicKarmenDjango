from django.db import models

# Create your models here.
from rkspletna.settings import BASE_DIR


class Novica(models.Model):
    title = models.CharField(max_length=60)
    creation_date = models.DateField()

    short_description = models.CharField(max_length=300)
    short_text = models.TextField()
    text = models.TextField()

    image = models.ImageField(upload_to='images/')

    def __unicode__(self):
        return u'%s ' % self.title

class Files(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)

    novica = models.ForeignKey('Novica')

    path = models.FileField(upload_to='files/')

    def __unicode__(self):
        return u'%s ' % self.name