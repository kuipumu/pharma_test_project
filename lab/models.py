"""lab app models"""

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django_json_field_schema_validator.validators import \
    JSONFieldSchemaValidator

from .schemas import sample_schema


class Sample(models.Model):
    """Sample model."""
    properties = models.JSONField(
        null=False,
        blank=False,
        validators=[
            JSONFieldSchemaValidator(sample_schema)
        ]
    )

    def clean(self):
        """Sample clean method."""
        # Validate if sample number already exists for other samples.
        if self.properties:
            number = self.properties['SampleNumber']
            queryset = Sample.objects.filter(
                properties__SampleNumber=number
            )
            if self.id is not None:
                queryset = queryset.exclude(id=self.id)
            if queryset.exists():
                raise ValidationError('There is already a sample with number: %s' % number)

    def get_absolute_url(self):
        """Define URL to get to sample update view."""
        return reverse_lazy('sample_update', args=[str(self.id)])

    def __str__(self):
        return str(self.properties['SampleNumber'])
