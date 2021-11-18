from django.conf                                    import settings
from rest_framework                                 import generics, status, views, mixins
from rest_framework.response                        import Response
from rest_framework_simplejwt.serializers           import TokenObtainPairSerializer
from rest_framework.mixins import UpdateModelMixin
from libreriauserapp.models.user                    import User
from libreriauserapp.serializers.userserializer     import UserSerializer

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"email":request.data["email"],
                     "password":request.data["password"]}
        try:
            tokenSerializer = TokenObtainPairSerializer(data=tokenData)
            tokenSerializer.is_valid(raise_exception=True)
            return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response('Error in token generation', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
class UsersView(generics.ListAPIView):
  serializer_class   = UserSerializer
  queryset           = User.objects.all()

  def get(self, request, *args, **kwargs):
      return super().get(request, *args, **kwargs)

class UserDetailView(generics.RetrieveAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class UserUpdateView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class   = UserSerializer
    queryset           = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class UserDeleteView(generics.DestroyAPIView):
    serializer_class   = UserSerializer
    queryset           = User.objects.all()

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
