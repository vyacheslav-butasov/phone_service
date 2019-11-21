from .serializers import PhoneNumberSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Phone_number


class PhoneNumberList(generics.ListCreateAPIView):
    queryset = Phone_number.objects.all()
    serializer_class = PhoneNumberSerializer


class PhoneNumberDetail(APIView):
    def get(self, request, full_phone_number):
        # phone_number = request.data.get('phone_number')
        print(type(full_phone_number))
        if not full_phone_number.isdigit():
            content = {'data type error': 'please enter only numbers'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        if len(full_phone_number) != 11 or full_phone_number[0] != '7':
            content = {'data type error': 'please enter number in MSISDN format(only Russia)'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        code = full_phone_number[1:4]
        phone_number = full_phone_number[4:]
        result = get_object_or_404(
            Phone_number, code=code,
            start_number__lte=phone_number,
            end_number__gte=phone_number
        )
        data = PhoneNumberSerializer(result).data
        print(full_phone_number)
        return Response(data)
