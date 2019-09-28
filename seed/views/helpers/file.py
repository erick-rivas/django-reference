"""
__Seed builder__v1.0
  (Read_only) Builder helper
"""

import os
import uuid

from rest_framework import views
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from seed.domain.helpers.save_file import save_file
from seed.serializers.helpers.file import FileSerializer

class FileView(views.APIView):  #

    parser_classes = (MultiPartParser,)

    def post(self, request):  #
        f = request.data['file']
        model = save_file(f)
        serializer = FileSerializer(model, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
