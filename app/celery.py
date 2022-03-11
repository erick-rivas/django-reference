# pylint: disable=W0401
from seed.app.celery import *
from celery import shared_task

#  Include custom tasks
#  Example:
#     @shared_task
#     def task_name():
#         print("hello word")
#
#  Run in code with task_name.delay(args)

# Pre-build async tasks
# - send_mail_async(**kwargs)