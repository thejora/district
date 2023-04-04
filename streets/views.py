from django.shortcuts import render
from django.http import JsonResponse
from .models import Street

def index(request):
    return render(request, 'streets/index.html')

def search_streets(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', None)
        if search_query:
            streets = Street.objects.filter(name__icontains=search_query).order_by('name')
            data = {'streets': list(streets.values('id', 'name'))}
            print(data)
            return JsonResponse(data)
    return JsonResponse({'error': 'No search query found.'})
