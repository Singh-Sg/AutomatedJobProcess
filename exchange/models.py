from django.db import models
from job_apply.models import User, Vacancy

class Report(models.Model):
    """
    """
    user = models.ForeignKey(User, related_name='user_report', on_delete=models.CASCADE)
    vacancy = models.ForeignKey(Vacancy, related_name='vacancy_in_reports', on_delete=models.CASCADE)
    result = models.BooleanField(default=False, verbose_name="Result")
    report = models.CharField(max_length=300, verbose_name="Report")
    def __str__(self):
        return str(self.user)