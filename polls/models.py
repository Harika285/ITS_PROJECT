from django.db import models
from django.utils.encoding import python_2_unicode_compatible
<<<<<<< HEAD
#from geoposition.fields import GeopositionField



#class PointOfInterest(models.Model):
 #   name = models.CharField(max_length=100)
  #  position = GeopositionField()
=======


>>>>>>> 06383a7ea820e0cbefd0cb199e365aa1ead6f5b9
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class MonthlyWeatherByCity(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)

