import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializer import EmailSerializer
from api.services import save_email_db

logger = logging.getLogger("django")


class User_Subscribe(APIView):
    def post(self, request, format=None):
        try:
            email = request["email"]
            serializer = EmailSerializer(data={"email": email})
            if not serializer.is_valid():
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                )
            save_email_db(serializer.validated_data["email"])
            return Response(
                {"message": "Email has been saved."},
                status=status.HTTP_200_OK,
            )

        except Exception as ex:
            logger.error(f"An error occured: {str(ex)}")
            return Response(status=status.HTTP_400_BAD_REQUEST)
