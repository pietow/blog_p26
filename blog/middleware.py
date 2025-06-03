from django.http import HttpResponseForbidden

class ExampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('req from middleware: ', request)
        print(request.method)
        if request.method == 'POST':
            return HttpResponseForbidden('Not Allowed') 
        response = self.get_response(request)
        return response