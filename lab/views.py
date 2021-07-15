"""lab app views"""

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import SampleForm
from .models import Sample


class SampleListView(ListView): # pylint: disable=too-few-public-methods
    """Sample list view."""
    model = Sample
    paginate_by = 100

    def get_context_data(self, **kwargs):
        """Add extra context data."""
        context = super().get_context_data(**kwargs)
        context['title'] = "All Samples"
        return context

class SampleCreateView(SuccessMessageMixin, CreateView): # pylint: disable=too-few-public-methods
    """Sample create view."""
    form_class = SampleForm
    model = Sample
    success_message = "Sample was created successfully"

    def get_context_data(self, **kwargs):
        """Add extra context data."""
        context = super().get_context_data(**kwargs)
        context['title'] = "Sample Create"
        return context

class SampleUpdateView(SuccessMessageMixin, UpdateView): # pylint: disable=too-few-public-methods
    """Sample update view."""
    form_class = SampleForm
    model = Sample
    success_message = "Sample was updated successfully"

    def get_context_data(self, **kwargs):
        """Add extra context data."""
        context = super().get_context_data(**kwargs)
        context['title'] = "Sample Update"
        return context

class SampleDeleteView(DeleteView): # pylint: disable=too-few-public-methods
    """Sample delete view."""
    model = Sample
    success_url = reverse_lazy('sample_list')

    def get_context_data(self, **kwargs):
        """Add extra context data."""
        context = super().get_context_data(**kwargs)
        context['title'] = "Delete Sample"
        return context
