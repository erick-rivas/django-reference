"""
__Seed builder__v0.1.8
  (Read_only) Builder helper
"""

from rest_framework import views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from seed.domain.helpers.save_file import save_file
from seed.serializers.helpers.file import FileSerializer

class FileView(views.APIView):  #

    parser_classes = (MultiPartParser,)

    def post(self, request):  #
        fs = request.FILES.getlist('file')
        if len(fs) == 0: return Response(status=status.HTTP_400_BAD_REQUEST)
        if len(fs) > 1:
            models = []
            for f in fs:
                model = save_file(f)
                models.append(model)
            serializer = FileSerializer(models, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            model = save_file(fs[0])
            serializer = FileSerializer(model, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
