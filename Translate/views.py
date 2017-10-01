from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TranslatorSerializer
from rest_framework.response import Response


from googletrans import Translator
translator = Translator()


class TranslateView(APIView):
    def post(self, request):
        serializer = TranslatorSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data
            text = str(valid_data.get('text'))

            destination = valid_data.get('dest')
            if destination:
                org = str(translator.translate(text, dest=destination))
                org = org.split(',')
                org = org[2].split('=')
                org = org[1]
            else:
                org = str(translator.translate(text))
                org = org.split(',')
                org = org[2].split('=')
                org = org[1]
                
            message = { 'original message' : text, 'translated message' : org }

            #return Response({"original message = {} & translated message = {} ".format(request.data+text, org)})
            #return Response({"original message = {} & translated message = {} ".format(text, org)})
            #return Response({"message": "Hello {}, you are {} year old".format(name, age)})
            return Response(message)
        else:
            return Response({"error": serializer.errors})
