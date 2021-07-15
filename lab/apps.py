"""lab app configuration"""

from django.apps import AppConfig


class LabConfig(AppConfig): # pylint: disable=too-few-public-methods
    """Lab app config."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lab'
