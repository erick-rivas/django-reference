"""
__Seed builder__
  Custom tasks
  Example:
      @shared_task
      def task_name():
          print("hello word")

  Run in code with task_name.delay(args)

  Pre-build async tasks (seed.app.celery)
    - send_mail_async(**kwargs) # See django send_mail docs https://docs.djangoproject.com/en/4.2/topics/email/
"""

# pylint: disable=W0401
from seed.app.celery import *
from celery import shared_task

## Include custom tasks after here ##