import uuid
from rest_framework import views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from models.helpers.file import File
from serializers.helpers.file import FileSerializer


class FileView(views.APIView):  #

    parser_classes = (MultiPartParser,)

    def post(self, request):  #
        f = request.data['file']
        filename = uuid.uuid4().hex + "_" + f.name
        model = File.objects.create()
        model.file.save(filename, f, save=True)

        serializer = FileSerializer(model, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)