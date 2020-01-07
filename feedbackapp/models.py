from django.db import models
class FeedbackData(models.Model):
    name=models.CharField(max_length=100)
    ratting=models.IntegerField()
    date=models.DateField(max_length=100)
    feedback=models.CharField(max_length=100)
