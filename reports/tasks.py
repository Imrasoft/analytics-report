from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from celery import shared_task
from .models import Email, Message, Workspace, Run, Project


@shared_task
def get_workspace_data():
    Workspace.get_rapidpro_workspaces()
    return


@shared_task
def organise_data():
    Message.assign_foreignkey()
    Run.assign_foreignkey()
    return


@shared_task
def get_hiwa_data():
    Project.get_project_voice_data()
    return


@shared_task
def send_emails():
    Email.email_report()
    return

