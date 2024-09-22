from django.shortcuts import render

# Create your views here.
# myapp/views.py

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RequestDataSerializer

@api_view(['GET', 'POST'])
def bfhl(request):
    user_id = "john_doe_17091999"  # Replace with dynamic user ID logic
    email = "john@xyz.com"          # Replace with actual email logic
    roll_number = "ABCD123"         # Replace with actual roll number logic

    if request.method == 'POST':
        serializer = RequestDataSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data['data']
            numbers = [x for x in data if x.isdigit()]
            alphabets = [x for x in data if x.isalpha()]
            highest_lowercase_alphabet = [max(filter(str.islower, data), default="")]

            # File handling (pseudo logic, replace with actual logic)
            file_valid = bool(serializer.validated_data.get('file_b64'))
            file_mime_type = "image/png"  # Example, update as needed
            file_size_kb = 400             # Example, update as needed

            return Response({
                "is_success": True,
                "user_id": user_id,
                "email": email,
                "roll_number": roll_number,
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": highest_lowercase_alphabet,
                "file_valid": file_valid,
                "file_mime_type": file_mime_type,
                "file_size_kb": file_size_kb
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"operation_code": 1}, status=status.HTTP_200_OK)
