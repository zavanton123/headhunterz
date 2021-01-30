from django.http import HttpResponse


# prevent the request to favicon.ico from returning 404 error
def favicon_placeholder(request):
    return HttpResponse("favicon")
