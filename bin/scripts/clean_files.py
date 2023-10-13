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

    print(f"TOTAL FILES: {num_original_files}")
    print(f"CLEANED FILES: {len(removed_files)}")
    print(f"PRESERVED FILES: {num_original_files-len(removed_files)}")
    if num_original_files > 0:
        print(f"CLEANING %: {len(removed_files)/num_original_files}%")
    else:
        print(f"CLEANING %: {0}%")