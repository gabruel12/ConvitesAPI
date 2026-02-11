from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserCadasterSerializer, LoginUserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class CadasterView(APIView):
    
    def post(self, request):
        serializer = UserCadasterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(TokenObtainPairView):
    serializer = LoginUserSerializer