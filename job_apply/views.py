from django.shortcuts import redirect
from .models import User, Vacancy
from .tasks import submit_job_application
from django.shortcuts import get_object_or_404


def send_application(request, user_id):
    """
    """
    user = get_object_or_404(User, pk=user_id)
    vacancy = get_object_or_404(Vacancy, pk=1)
    submit_job_application.delay(user.id, vacancy.link)
    return redirect('user_list')
