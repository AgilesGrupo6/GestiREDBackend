from django.http import HttpResponse
from django.core.mail import send_mail
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from GestiRED.models import User
from GestiRED.models import QualityControl, Phase, Resource, ResourceType,PhaseType
from django.core import serializers
from django.db.models import Q

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
                  'Recurso: ' + resource_name + '\n Observaciones: Se ha asignado para control de calidad a: ' + responsible_name,
                  'clipstaragil6@gmail.com',
                  [user.email],
                  fail_silently=False)

    res = {"status": "Ok", "Content:": "Email enviado"}
    return HttpResponse(json.dumps(res), content_type="application/json")

@csrf_exempt
def resources_filters(request):
    qs_json={}
    if request.method == 'GET':

        phaseType = request.GET.get('phaseType')
        if phaseType != None : phaseType= phaseType.split(',')

        resourceType = request.GET.get('resourceType')
        if resourceType != None : resourceType = resourceType.split(',')

        responsible = request.GET.get('responsible')
        if responsible != None: responsible = responsible.split(',')

        labels = request.GET.get('labels')

        my_dict = {'phase__phaseType__in':phaseType,
                   'resourceType__in': resourceType,
                   'responsibles__in':responsible,
                   'labels__icontains': labels}  # Your dict with fields
        or_condition = Q()
        for key, value in my_dict.items():
            if value != None:
                or_condition.add(Q(**{key: value}), Q.AND)
        lp = set()
        lp=Resource.objects.filter(or_condition).all().distinct()
        data = list([res.json() for res in lp])
        qs_json =json.dumps({'objects':data})
    return HttpResponse( qs_json, content_type='application/json')

