from .serializers import ExecursionSerializer
from .models import Execursion
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class ExecursionList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Execursion.objects.all()
    serializer_class = ExecursionSerializer

class ExecursionDetial(generics.RetrieveDetroyAPIView):
    pemission_classes = (IsAuthenticated)
    queryset = Execursion.objects.all()
    serializer_class = ExecursionSerializer



    