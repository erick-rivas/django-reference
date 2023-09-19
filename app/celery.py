"""
__Seed builder__
  Custom tasks
  Example:
      @shared_task
      def task_name():
          print("hello word")

  Run in code with task_name.delay(args)

  To include beat tasks, create a shared_task and schedule with
        app.conf.beat_schedule['<TASK_ID>'] = {
            'task': 'app.celery.<SHARED_TASK_NAME>',
            'schedule': timedelta(hours=1) # Modify it, default 1hr
        }

  Pre-build async tasks (seed.app.celery)
    - send_mail_async(**kwargs) # See django send_mail docs https://docs.djangoproject.com/en/4.2/topics/email/
    - clean_files_async(dir_path, min_file_age)
"""

# pylint: disable=W0401
from seed.app.celery import *
from celery import shared_task

## Include custom tasks after here ##