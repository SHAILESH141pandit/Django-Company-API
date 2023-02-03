
from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("Home page requested.")
    '''friends = [
            "ankit",
            "raju",
            "ravi",
            "uttam"
            ]'''
        #JsonResponse(friends, safe = False)
    return HttpResponse('''<h1> Welcome to , </h1>
                                                <h3>This is a simple Company Details API built using Python's Advance Django REST framework.</h3>''')
