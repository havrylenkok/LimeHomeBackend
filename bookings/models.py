from django.db import models


class Booking(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_changed = models.DateTimeField(auto_now=True, editable=False)

    property_id = models.TextField()
