from rest_framework.response import Response
from rest_framework.decorators import api_view
import random
import os
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound

@api_view(['GET'])
def get_random_number(request):
    random_number = random.randint(0,100)

    return Response(random_number)


class Assets(View):

    def get(self, _request, filename):
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()
