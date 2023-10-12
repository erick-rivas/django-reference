import os
import sys
import dotenv
import django

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.realpath(__file__)) + '/../../'
    sys.path.append(base_dir)
    from app.settings import get_dotenv_path

    dotenv.read_dotenv(os.path.join(base_dir, get_dotenv_path()))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    django.setup()

    from seed.helpers.clean_files import clean_files

    removed_files, num_original_files = clean_files()

    print("TOTAL FILES: {}".format(num_original_files))
    print("CLEANED FILES: {}".format(len(removed_files)))
    print("PRESERVED FILES: {}".format(num_original_files-len(removed_files)))
    if num_original_files > 0:
        print("CLEANING %: {}%".format(len(removed_files)/num_original_files))
    else:
        print("CLEANING %: {}%".format(0))