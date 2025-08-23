import os
import sys

# pylint: disable=W0702
def handle(model_str, file_path="./dump.yaml"):
    from django.core import serializers
    try:
        models = __import__("app.models", globals(), locals(), [model_str, ], 0)
        model = getattr(models, model_str)
    except:
        print("Invalid model: " + model_str + ", execute with bin/dump MODEL_NAME")
        return
    data = serializers.serialize("yaml", model.objects.all().order_by("id"))
    with open(file_path, "w", encoding="utf-8") as out:
        out.write(data)
    print("Exported in " + file_path)

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.realpath(__file__)) + '/../../'
    sys.path.insert(0, base_dir)

    import dotenv
    from app.settings import get_dotenv_path
    dotenv.read_dotenv(os.path.join(base_dir, get_dotenv_path()))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

    import django
    django.setup()

    n = len(sys.argv)
    if n <= 1:
        print("Invalid input, execute with bin/dump MODEL_NAME")
    elif n == 2:
        handle(sys.argv[1])
    else:
        handle(sys.argv[1], sys.argv[2])