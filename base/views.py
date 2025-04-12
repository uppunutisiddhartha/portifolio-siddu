from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"index.html")
def succes(request):
    return render(request,"succes.html")
from django.core.mail import send_mail, BadHeaderError

from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import render, redirect

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        try:
            # Send email to admin
            send_mail(
                f"New Contact from {name}",
                f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
                "uppunutisiddhartha@gmail.com",
                ["uppunutisiddhartha@gmail.com"],  # admin email
            )

            # Render HTML confirmation template for user
            html_content = render_to_string("email_templates/contact_response.html", {
                "name": name,
                "user_message": message,
            })

            # Send confirmation email to user
            email_message = EmailMessage(
                "Thanks for contacting me!",
                html_content,
                "uppunutisiddhartha@gmail.com",
                [email],
            )
            email_message.content_subtype = "html"
            email_message.send()

            messages.success(request, "Your message was sent!")

        except Exception as e:
            print("EMAIL ERROR:", e)
            messages.error(request, "Something went wrong. Try again.")

        return redirect("succes")

    return render(request, "succes.html")

