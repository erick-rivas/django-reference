import os
import dotenv

from django.core.wsgi import get_wsgi_application

env_file = '.env.dev'
if 'IS_PROD' in os.environ: env_file = '.env.prod'
dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), env_file))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

application = get_wsgi_application()
