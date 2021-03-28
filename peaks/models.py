from django.contrib.gis.db import models

class Peak(models.Model):
	peak_name = models.CharField(max_length=255)
	coordinates = models.PointField()
	altitude = models.FloatField()
	def __str__(self):
		return self.peak_name

class Record(models.Model):
	forecasted_at = models.DateTimeField()
	peak = models.ForeignKey(Peak, on_delete=models.CASCADE)
	temperature = models.FloatField()
	def __str__(self):
		return str(self.forecasted_at) + ' - '+self.peak.peak_name
