from django.http import JsonResponse


def api_simple(request, *args, **kwargs):
    body = request.body
    headers = request.headers
    print(request.GET)
    print(headers['content_type'])
    print(body)
    return JsonResponse({'message': 'API request recived'})
