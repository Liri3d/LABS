from django.db import models

class GasReading(models.Model):
    meter_number = models.CharField('Номер счётчика', max_length=50)
    reading_date = models.DateField('Дата показания')
    value = models.DecimalField('Показание, м³', max_digits=10, decimal_places=2)
    comment = models.TextField('Комментарий', blank=True)

    def __str__(self):
        return f"{self.meter_number} — {self.reading_date}: {self.value} м³"

    class Meta:
        verbose_name = 'Показание счётчика'
        verbose_name_plural = 'Показания счётчиков'
        ordering = ['-reading_date']
