from django.db import models

from users.models import Department


class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    unit_load = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return self.code
