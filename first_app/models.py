from django.db import models

# Create your models here.
class Reciter(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name + " " + self.last_name+ " (" + self.country+ ")"
 

class Album(models.Model):
    # id = models.AutoField(primary_key=True)
    artist = models.ForeignKey(Reciter, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField(default=0)
    def __str__(self):
        return self.name + " (" + str(self.release_date) + ") >> " + str(self.num_stars)