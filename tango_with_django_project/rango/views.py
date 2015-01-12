from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as
    # it's context. Note the key 'boldmessage' is the same as
    # {{ boldmessage }} in the HTML template.
    
    context_dictionary = {'boldmessage' : "I am bold font from the context."}
    return render(request, 'rango/index.html', context_dictionary)

def about(request):
    context_dictionary = {'italicmessage' : 'I am in italic font.'}
    return render(request, 'rango/about.html', context_dictionary)
