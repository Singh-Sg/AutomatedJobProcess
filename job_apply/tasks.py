import uuid
import logging
from time import sleep
from splinter import Browser
from celery import shared_task
from django.conf import settings
from django.utils import timezone
from django.shortcuts import get_object_or_404
from job_apply.models import User, Experience, Training, Vacancy, Application
from exchange.models import Report

@shared_task
def submit_job_application(user_id, link): 
    """
    """
    if user_id:
        user = get_object_or_404(User, pk=user_id)
    try:
        with Browser() as browser:
            browser.visit(link)
            browser.find_by_id('st-apply').click()
            sleep(3)
            new_paze=browser.find_by_id('st-connect-manual').click()
            browser.fill('firstName', user.first_name)
            browser.fill('lastName', user.last_name)
            browser.fill('email', user.email)
            browser.fill('phone', user.phone_number.national_number)
            browser.find_by_id('js-avatar-upload').fill(user.avatar_url)
            browser.driver.save_screenshot('media/{filename}_screenshot_{uuid}.png'.format(filename=user.first_name, uuid=uuid.uuid4()))
            for exp in user.Experience_User.all():
                browser.find_by_id('js-work-show-form').click()
                sleep(2)
                browser.fill('workPosition', exp.work_experience_position)
                browser.fill('workCompany', exp.work_experience_employer)
                browser.fill('workLocation', exp.work_experience_location)
                if exp.work_experience_starts:
                    browser.select('workBeginMonth', exp.work_experience_starts.month)
                    browser.fill('workBeginYear', exp.work_experience_starts.year)
                if exp.work_experience_ends:
                    browser.fill('workEndYear', exp.work_experience_ends.year)
                    browser.select('workEndMonth', exp.work_experience_ends.month)
                browser.check('workCurrent')
                browser.fill('workDescription', exp.description)
                browser.driver.save_screenshot('media/{filename}_screenshot_{uuid}.png'.format(filename=user.first_name, uuid=uuid.uuid4()))
                browser.find_by_id('js-work-add').click()
            sleep(2)   
            for training in user.Training_User.all():
                browser.find_by_id('js-education-show-form').click()
                sleep(2)
                browser.fill('eduInstitution', training.training_institution)
                browser.fill('eduDegree', training.training_degree)
                browser.fill('eduMajor', training.training_degree)
                browser.fill('eduLocation', training.training_major)
                browser.select('eduBeginMonth', training.training_starts.month)
                browser.fill('eduBeginYear', training.training_starts.year)
                browser.select('eduEndMonth', training.training_ends.month)
                browser.fill('eduEndYear', training.training_ends.year)
                browser.check('eduCurrent')
                browser.fill('eduDescription', training.description)
                browser.driver.save_screenshot('media/{filename}_screenshot_{uuid}.png'.format(filename=user.first_name, uuid=uuid.uuid4()))
                browser.find_by_id('js-education-add').click()
            sleep(2)
            browser.find_by_id('js-resume-upload').fill(user.cv_path)
            browser.fill('messageToEmployer', user.message)
            browser.check('consent')
            browser.driver.save_screenshot('media/{filename}_screenshot_{uuid}.png'.format(filename=user.first_name, uuid=uuid.uuid4()))
            button = browser.find_by_id('js-full-submit').click()
            sleep(5)   
            browser.driver.save_screenshot('media/{filename}_screenshot_{uuid}.png'.format(filename=user.first_name, uuid=uuid.uuid4()))
            applyed_vacancy=Vacancy.objects.get(link=link)
            if browser.is_text_present('Jetzt sehen Sie bitte in Ihrem Postfach nach und klicken Sie auf den Link in der E-Mail, die wir Ihnen soeben gesendet haben.'):
                application = Application.objects.create(user=user, vacancy=applyed_vacancy)
                report = 'Jetzt sehen Sie bitte in Ihrem Postfach nach und klicken Sie auf den Link in der E-Mail, die wir Ihnen soeben gesendet haben.'
                Report.objects.create(user=user, vacancy=applyed_vacancy, result=True, report=report)
            else:
                Report.objects.create(user=user, vacancy=applyed_vacancy, report='No, it wasnt found')
                logger = logging.getLogger('root')
                logger.error('Browser Error', exc_info=True, extra={'error':'No, it wasnt found'})
        browser.quit()
    except Exception as e:
        logger = logging.getLogger('root')
        logger.error('Browser Error', exc_info=True, extra={'error':e})
