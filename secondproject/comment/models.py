from django.db import models
from listelement.models import Element


# Create your models here.
class Comment(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    element = models.ForeignKey(Element, on_delete=models.CASCADE, null=True, related_name='comments')

    def __str__(self):
        return 'Comment #{}'.format(self.id)


class TypeContact(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=13)
    birth_date = models.DateField()
    type_contact = models.ForeignKey(TypeContact, on_delete=models.CASCADE, default=1)
    document = models.FileField(upload_to='uploads/contact')
