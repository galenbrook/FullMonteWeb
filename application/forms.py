from django import forms
from django.forms import formset_factory
from django.forms import BaseFormSet
from .models import *

class tclInputForm(forms.ModelForm):
    class Meta:
        model = tclInput
        fields = ('meshFile', 'kernelType')
        kernel_choices = (('TetraSVKernal','TetraSVKernel'),
                         ('TetraSurfaceKernal','TetraSurfaceKernel'),
                         ('TetraVolumeKernal','TetraVolumeKernel'),
                         ('TetraInternalKernal','TetraInternalKernel'))
        widgets = {
            'kernelType': forms.Select(choices=kernel_choices),
        }

class materialSet(forms.Form):
    custom = custom = forms.ModelChoiceField(queryset=Material.objects.all())
    material = forms.CharField(label='Material',
                               widget=forms.TextInput(attrs={
                                                      'class': 'form-control',
                                                      'placeholder': 'Enter Material Name here'
                                                      }),
                               max_length=255)
    scatteringCoeff = forms.FloatField(label='Scattering Coefficient', min_value=0)
    absorptionCoeff = forms.FloatField(label='Absorption Coefficient', min_value=0)
    refractiveIndex = forms.FloatField(label='Refractive Index', min_value=0)
    anisotropy = forms.FloatField(label='Anisotropy', min_value=0)

class lightSource(forms.Form):
    sourceType = forms.ChoiceField(label='Type', choices=(('Point','Point'),
                                                            ('PencilBeam','PencilBeam'),
                                                            ('Volume','Volume'),
                                                            ('Ball','Ball'),
                                                            ('Line','Line'),
                                                            ('Fiber','Fiber'),
                                                            ('Tetraface','Tetraface'),
                                                            ('Cylinder','Cylinder'),
                                                            ('Composite','Composite')))
    xPos = forms.FloatField(label='X Position')
    yPos = forms.FloatField(label='Y Position')
    zPos = forms.FloatField(label='Z Position')
    power = forms.IntegerField(label='Power')

class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

materialSetSet = formset_factory(materialSet, formset=RequiredFormSet)
lightSourceSet = formset_factory(lightSource, formset=RequiredFormSet)
