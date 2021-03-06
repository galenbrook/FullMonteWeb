from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from application.tclGenerator import *

# Create your views here.

# homepage
def home(request):
    return render(request, "home.html")

# FullMonte Tutorial page
def fmTutorial(request):
    return render(request, "tutorial.html")

# FullMonte About page
def about(request):
    return render(request, "about.html")

# FullMonte Simulator start page
def fmSimulator(request):
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = tclInputForm(request.POST, request.FILES)
        
        # check whether it's valid:
        if form.is_valid():
            # process cleaned data from formsets
            #print(form.cleaned_data)
            
            form.save()

            request.session['kernelType'] = form.cleaned_data['kernelType']

            return HttpResponseRedirect('/application/simulator_material')

    # If this is a GET (or any other method) create the default form.
    else:
        form = tclInputForm(request.GET or None)
        
    context = {
        'form': form,
    }

    return render(request, "simulator.html", context)

# FullMonte Simulator material page
def fmSimulatorMaterial(request):
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        formset1 = materialSetSet(request.POST)
        
        # check whether it's valid:
        if formset1.is_valid():
            # process cleaned data from formsets
            
            request.session['material'] = []
            request.session['scatteringCoeff'] = []
            request.session['absorptionCoeff'] = []
            request.session['refractiveIndex'] = []
            request.session['anisotropy'] = []
            
            for form in formset1:
                request.session['material'].append(form.cleaned_data['material'])
                request.session['scatteringCoeff'].append(form.cleaned_data['scatteringCoeff'])
                request.session['absorptionCoeff'].append(form.cleaned_data['absorptionCoeff'])
                request.session['refractiveIndex'].append(form.cleaned_data['refractiveIndex'])
                request.session['anisotropy'].append(form.cleaned_data['anisotropy'])
            
            return HttpResponseRedirect('/application/simulator_source')

    # If this is a GET (or any other method) create the default form.
    else:
        formset1 = materialSetSet(request.GET or None)
        
    context = {
        'formset1': formset1,
    }
    
    return render(request, "simulator_material.html", context)

# FullMonte Simulator light source page
def fmSimulatorSource(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        formset2 = lightSourceSet(request.POST)
        
        # check whether it's valid:
        if formset2.is_valid():
            # process cleaned data from formsets
            
            request.session['sourceType'] = []
            request.session['xPos'] = []
            request.session['yPos'] = []
            request.session['zPos'] = []
            request.session['power'] = []
            
            for form in formset2:
                request.session['sourceType'].append(form.cleaned_data['sourceType'])
                request.session['xPos'].append(form.cleaned_data['xPos'])
                request.session['yPos'].append(form.cleaned_data['yPos'])
                request.session['zPos'].append(form.cleaned_data['zPos'])
                request.session['power'].append(form.cleaned_data['power'])
            
            mesh = tclInput.objects.latest('id')
            
            tclGenerator(request.session, mesh)
            
            
            
            #print(tclInput.objects.all())
            tclInput.objects.all().delete()
            #print(mesh.meshFile)
            #print(tclInput.objects.all())
            return HttpResponseRedirect('/application/visualization')

    # If this is a GET (or any other method) create the default form.
    else:
        formset2 = lightSourceSet(request.GET or None)
        
    context = {
        'formset2': formset2,
    }

    return render(request, "simulator_source.html", context)

# FullMonte Output page
def fmVisualization(request):
    return render(request, "visualization.html")
