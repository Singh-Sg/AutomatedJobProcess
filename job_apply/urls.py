from django.urls import path

from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('send-application/<int:user_id>', views.send_application, name='send_application'),
    path('', RedirectView.as_view(url='admin/job_apply/user/'), name='user_list'),

]
