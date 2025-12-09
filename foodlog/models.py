from django.db import models
from django.urls import reverse

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"

    def get_delete_url(self):
        return reverse('food:delete', args=[self.pk])
