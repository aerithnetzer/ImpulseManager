from django.db import models
from django_mongodb_backend.fields import ArrayField

class Workflow(models.Model):
    state: models.CharField = models.CharField(max_length=30)
    last_updated: models.DateTimeField = models.DateTimeField()
    class Meta:
        app_label = "JobViewer"
        db_table = "fireworks"

    pass

class Page(models.Model):
    id: models.CharField = models.CharField(max_length=120)
    block_type: models.CharField = models.CharField(max_length=20)
    html: models.TextField = models.TextField(null=True, blank=True)
    polygon: ArrayField = ArrayField(ArrayField(models.FloatField()), null=True, blank=True)
    bbox: ArrayField = ArrayField(ArrayField(models.FloatField()), null=True, blank=True)
    accession_number: models.CharField = models.CharField(max_length=120, null=True, blank=True)
    page_number: models.IntegerField = models.IntegerField(default=0, null=True, blank=True)
    JPG: models.BinaryField = models.BinaryField(null=True, blank=True)
    children: ArrayField = ArrayField(models.JSONField(), null=True, blank=True)

    class Meta:
        app_label = "JobViewer"
        db_table = "pages"

class UploadedDocument(models.Model):
    SOURCE_FILE: models.CharField = models.CharField(max_length=500)
    uploaded_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = "JobViewer"
        db_table = "pages"
