from django.core.mail import BadHeaderError, send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
def send_email(request):
    subject = "Contact Me From Website"
    message = request.data.get("message")
    from_email = request.data.get("sender_email")
    if message and from_email:
        try:
            send_mail(subject, message, from_email, ["nickduunn@gmail.com"])
            return Response(
                {"message": "Email sent successfully"}, status=status.HTTP_200_OK
            )
        except BadHeaderError:
            return Response(
                {"error": "Invalid header found"}, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            print(e)
            return Response(
                {"error": "An unexpected error occurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    else:
        return Response(
            {"error": "Make sure all fields are entered and valid"},
            status=status.HTTP_400_BAD_REQUEST,
        )
