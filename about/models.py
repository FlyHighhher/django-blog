from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class About(models.Model):
    """
    Model stores information about a particular section named "About".
    It includes a title, a profile image (which is hosted on Cloudinary),
    a timestamp for the last update, and the content or description of the
    "About" section. The title is set to be unique, ensuring that each "About"
    instance has a distinct title.
    """
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Model stores collaboration requests. Each request
    has a name, an email address, a message or details
    about the collaboration, and a flag (`read`) indicating
    whether the request has been read or not. The `__str__`
    method provides a user-friendly string representation for
    instances of this model.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"