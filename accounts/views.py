from django.shortcuts import render

# Create your views here.


from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "message": "Foydalanuvchi muvofaqiyatli royxatdan otdi!",
                "username": user.username,
                "email": user.email,
            },
            status=status.HTTP_201_CREATED
        )



