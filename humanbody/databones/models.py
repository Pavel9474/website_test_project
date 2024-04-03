from django.db import models

# Create your models here.
class Bonedata(models.Model):
    first_author = models.CharField('Первый автор',max_length=100)
    title = models.CharField('Название работы',max_length=250)
    year_pub=models.CharField('Год публикации', max_length=4)
    # bone_sizes=models.CharField('Длина кости', max_length=40)
    # bone_volume_to_total_volume=models.FloatField('Длина кости', max_length=40)
    # trabecular_thickness=models.FloatField('Длина кости', max_length=40)
    # trabecular_separation=models.FloatField('Длина кости', max_length=40)
    
    # age_spicements_min
    # age_spicements_max дополнить поля
    def __str__(self):
        return f'Data: {self.title}'

    class Meta:
        verbose_name_plural = 'BoneData'
        verbose_name = 'BoneData'

    def get_absolute_url(self):
        return f'/databones/{self.id}'