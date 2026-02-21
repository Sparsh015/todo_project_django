from django.db import models

# Create your models here.
class Task(models.Model):
    priority_choices = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank = True)
    completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=7, choices=priority_choices, default='Medium')
    due_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    