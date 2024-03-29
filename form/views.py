from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import FormDataSerializer
from .models import FormData
from django.views.generic import base as custom_views
import json
from django.http import JsonResponse
from .func import create_form_history
from os.path import join as join_path
from .email import send_user_email


def FormViewPage(request):
    context = {}
    return render(request, "index.html", context)


class SubmitFormDetails(GenericAPIView):
    serializer_class = FormDataSerializer

    def post(self, request, format=None):
        data = request.data

        first_name = data['firstName']
        last_name = data['lastName']
        age = data['age']
        email = data['email']
        phone_number = data['phoneNumber']
        state = data['state']
        lga = data['lga']
        category = data['category']
        shop_name = data['shopName']

        FormData.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            email=email,
            phone_number=phone_number,
            state=state,
            lga=lga,
            category=category,
            shop_name=shop_name
        )

        send_user_email(email, first_name)

        return Response({"success": "form submitted"}, status='200')


class FormRecord(custom_views.View):
    template_name = join_path('download.html')

    def get(self, request):
        response = create_form_history()
        url = response["downloadUrl"]
        return render(request, self.template_name, {"url": url})

    def post(self, request):
        # data = json.loads(request.body)
        # Retrieve Excel sheet
        response = create_form_history()
        return JsonResponse(response["downloadUrl"], safe=False)
