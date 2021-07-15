"""lab app URL configuration"""

from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import (SampleCreateView, SampleDeleteView, SampleListView,
                    SampleUpdateView)

urlpatterns = [
    path(
        _(''),
        SampleListView.as_view(),
        name='sample_list'
    ),
    path(
        _('create'),
        SampleCreateView.as_view(),
        name='sample_create'
    ),
    path(
        _('update/<int:pk>'),
        SampleUpdateView.as_view(),
        name='sample_update'
    ),
    path(
        _('delete/<int:pk>'),
        SampleDeleteView.as_view(),
        name='sample_delete'
    )
]
