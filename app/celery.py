"""
__Seed builder__
  Custom tasks
  Example:
      @shared_task
      def task_name():
          print("hello word")

  Run in code with task_name.delay(args)

  Pre-build async tasks (seed.app.celery)
    - send_mail_async(subject, plain_text, from_email, to_email, **kwargs)
"""

# pylint: disable=W0401
from seed.app.celery import *
from celery import shared_task

## Include custom tasks after here ##