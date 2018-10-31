from django.http import HttpResponse
from django.core.mail import send_mail
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from GestiRED.models import User

# Create your views here.

def index(request):
    return HttpResponse("GestiRED app UP")


@csrf_exempt
def quality_review_notification(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data["id"]
        resource = data["resource"]
        obs = data["observation"]
        user = User.objects.get(pk=id)

        send_mail('Revision Calidad',
                  'Recurso: ' + resource + 'Observaciones: ' + obs,
                  'clipstaragil6@gmail.com',
                  [user.email],
                  fail_silently=False)

    res = {"status": "Ok", "Content:": "Email enviado"}
    return HttpResponse(json.dumps(res), content_type="application/json")









