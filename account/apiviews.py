from .models import UserManager
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework import generics



class UserReg(generics.CreateAPIView):
    serlizlier_class = UserSerializer
    permission_classess = (AllowAny,)

    def post(self, request):
        serializer = self.serlizlier_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status.code = status.HTTP_201_CREATED
        response = {
            'success':'True',
            'status_code':status_code,
            'message':  'user Successfully Created'
        }
        return Response(response, status=status_code)