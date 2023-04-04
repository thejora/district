from django.db import models

class Street(models.Model):
    name = models.CharField(max_length=255, unique=True)
    district_2308 = models.CharField(max_length=10, blank=True)
    district_2309 = models.CharField(max_length=10, blank=True)
    district_2310 = models.CharField(max_length=10, blank=True)
    district_2311 = models.CharField(max_length=10, blank=True)
    district_2312 = models.CharField(max_length=10, blank=True)
    remark = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
