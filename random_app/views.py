from rest_framework.response import Response
from rest_framework.decorators import api_view
import random

@api_view(['GET'])
def get_random_number(request):
    random_number = random.randint(0,100)

    return Response(random_number)