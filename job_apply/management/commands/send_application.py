from django.core.management.base import BaseCommand, CommandError
from job_apply.tasks import submit_job_application

class Command(BaseCommand):
    help = 'Submit Application Form'

    def add_arguments(self, parser):
        parser.add_argument('--user_id', type=int, help='Indicates the user ID')
        parser.add_argument('--link', type=str, help='Indicates the taget Link')

    def handle(self, *args, **kwargs):
        userID = kwargs['user_id']
        link = kwargs['link']
        submit_job_application.delay(userID, link)

