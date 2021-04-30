from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from rest_framework.views import APIView

from google_places.utils import *


class PlacesTextSearchView(APIView):
    parameters = [mappings.NAME, mappings.ADDRESS, mappings.RATING, mappings.PHOTOS]
    PAGE_SIZE = 5

    def get(self, request):

        if request.query_params.get('text', None):
            text = request.query_params.get('text', None)
            page = int(request.GET.get('page', None))
            results = retrieve_places_by_parameters(text, parameters=self.parameters)
            start = page * self.PAGE_SIZE
            stop = min(start + self.PAGE_SIZE, len(results))
            return JsonResponse({'results': results[start:stop]})

        else:
            return HttpResponse(status=204)
