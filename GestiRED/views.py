from django.http import HttpResponse
from django.core.mail import send_mail
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from GestiRED.models import User
from GestiRED.models import QualityControl

# Create your views here.

def index(request):
    return HttpResponse("GestiRED app UP")


@csrf_exempt
def quality_review_notification(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        qualityControl_id = data["qualityControl_id"]
        resource_name = data["resource_name"]
        responsible_name = data["responsible_name"]
        qualityControl = QualityControl.objects.get(pk=qualityControl_id)
        user = qualityControl.responsible

        send_mail('Revision Calidad',
                  'Recurso: ' + resource_name + 'Observaciones: ' + qualityControl.observation,
                  'clipstaragil6@gmail.com',
                  [user.email],
                  fail_silently=False)

    res = {"status": "Ok", "Content:": "Email enviado"}
    return HttpResponse(json.dumps(res), content_type="application/json")









