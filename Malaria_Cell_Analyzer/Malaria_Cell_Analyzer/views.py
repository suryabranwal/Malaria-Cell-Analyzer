# this is created by me

from django.http import HttpResponse
from django.shortcuts import render
from .gen_dataset_completed import Malaria_Cell_Analyzer
from  .malaria_classification_completed import malaria_classification_completed


def home(request):
    return render(request, 'home.html')

def image(request):
    output = []
    djimage = request.POST.get('image', 'default')
    url_check = request.POST.get('url_check', 'off')
    #if url_check == "on":
    output = Malaria_Cell_Analyzer(djimage)
    output_text = malaria_classification_completed()
    dicts = {'print_output': output, 'output_text': output_text}
    #else:
     #   return HttpResponse('Error')
    return render(request, 'output.html', dicts)
