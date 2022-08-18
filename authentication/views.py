from rest_framework.generics import get_object_or_404
from authentication.models import User
from rest_framework.decorators import action, api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status, permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import MyTokenObtainPairSerializer, UserSerializer, RegisterSerializer
# https://www.codersarts.com/post/how-to-create-register-and-login-api-using-django-rest-framework-and-token-authentication
from .models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
#from knox.views import LoginView as KnoxLoginView
# Remember that authentication deals with recognizing the users that are connecting to your API,
# while permissions deals with giving access to some resources to the users.


class ObtainTokenPairWithColorView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                # user = User.objects.create_user(
                #     username=serializer.init_data['username'],
                #     password=serializer.init_data['password'],
                # )

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @detail_route(methods=['get'])
    # @action(methods=['get'], detail=True)
    # def retrieve_by_username(self, request, username=None):
    #     try:
    #         user = User.objects.get(userName=username)
    #         return Response(user)
    #     except User.DoesNotExist:
    #         return Response("No user with username found!", status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, url_path='username/(?P<username>\w+)')
    def getByUsername(self, request, username):
        user = get_object_or_404(User, username=username)
        #data = UserSerializer(user, context={'request': request}).data
        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_200_OK)
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getStockInfo(request):
#     #Get stock info from database
#     stock_info = Stock.objects.all()
#     # Using Serializer to convert data
#     # Set many=True to serializer queryset or list of objects instead of a single object instance
#     stock_serializer = StockSerializer(stock_info,many=True)

#     return Response(stock_serializer.data)

# Class based view to Get User Details using Token Authentication

# Profile


class ProfileView(generics.RetrieveAPIView):
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    # @api_view(['GET'])
    # @authentication_classes([])  # Add this
    # @permission_classes([])  # Maybe add this too
    # def post(self, request):
    #     # pass
    #     username = request.data['username']
    #     password = request.data['password']
    #     user = User.objects.filter('username')
    #     if user is None:
    #raise AuthenticationFailed('User not found')


class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

# Class based view to register user

# https://python.plainenglish.io/django-rest-framework-jwt-auth-with-login-and-register-77f830cd8789


class RegisterApi(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)

# https://www.youtube.com/watch?v=PUzgZrS_piQ


class LoginApi(APIView):
    permission_classes = (permissions.AllowAny,)

    @api_view(['GET'])
    # @authentication_classes([])  # Add this
    # @permission_classes([])  # Maybe add this too
    def post(self, request):
        # pass
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter('username')
        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
