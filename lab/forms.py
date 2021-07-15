"""lab app forms"""

from django.forms import ModelForm
from django_json_widget.widgets import JSONEditorWidget

from .models import Sample


class SampleForm(ModelForm): # pylint: disable=too-few-public-methods
    """Sample create/update model form."""
    class Meta: # pylint: disable=too-few-public-methods
        """Model form meta."""
        model = Sample
        fields = ['properties']
        widgets = {
            'properties': JSONEditorWidget(width="100%")
        }
