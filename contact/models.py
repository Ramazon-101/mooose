from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=212)
    email = models.EmailField()
    subject = models.CharField(max_length=212, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

