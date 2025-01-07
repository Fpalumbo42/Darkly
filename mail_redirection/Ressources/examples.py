from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import JsonResponse
import secrets

def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
            reset_token = generate_reset_token(user)
            reset_link = f"https://example.com/reset-password/{reset_token}"

            send_mail(
                subject="Password Reset Request",
                message=f"Click the link to reset your password: {reset_link}",
                from_email='admin@hotmail.com',
                recipient_list=[email],
            )
            return JsonResponse({"message": "Password reset email sent."}, status=200)

        except User.DoesNotExist:
            return JsonResponse({"message": "If this email exists, a reset link will be sent."}, status=200)

    return JsonResponse({"error": "Invalid request method."}, status=400)


def generate_reset_token(user):
    return secrets.token_urlsafe(32)