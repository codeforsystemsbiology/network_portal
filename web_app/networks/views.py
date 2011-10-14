# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext 
from web_app.networks.models import Gene

def gene(request):
    #return HttpResponse("testing gene")
    return render_to_response('analysis/gene.html')

def network(request):
    return HttpResponse("testing network")

def motif(request):
    return HttpResponse("testing motif")

def function(request):
    return HttpResponse("testing function")
