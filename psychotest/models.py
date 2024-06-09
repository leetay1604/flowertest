from django.db import models

class UserResponse(models.Model):
    session_key = models.CharField(max_length=40)
    question = models.IntegerField()
    answer = models.CharField(max_length=255)

    def __str__(self):
        return f"Q{self.question}: {self.answer}"
