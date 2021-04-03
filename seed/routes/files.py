"""
__Seed builder__v0.2.0
  (Read_only) Builder helper
"""

from rest_framework import views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from seed.helpers.save_file import save_file_obj
from seed.serializers.file import FileSerializer

class FileView(views.APIView):  #

    parser_classes = (MultiPartParser,)

    def post(self, request):  #
        files = request.FILES.getlist('file')
        if len(files) == 0: return Response(status=status.HTTP_400_BAD_REQUEST)
        if len(files) > 1:
            models = []
            for file in files:
                model = save_file_obj(file)
                models.append(model)
            serializer = FileSerializer(models, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            model = save_file_obj(files[0])
            serializer = FileSerializer(model, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)