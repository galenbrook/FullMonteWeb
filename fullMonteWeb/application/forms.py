from django import forms

class tclInput(forms.Form):
    class materialSet(forms.Form):
        material = forms.CharField(label='Material')
        scatteringCoeff = forms.IntegerField(label='ScatteringCoeff')
        absorptionCoeff = forms.IntegerField(label='AbsorptionCoeff')
        refractiveIndex = forms.IntegerField(label='RefractiveIndex')
        anisotropy = forms.IntegerField(label='Anisotropy')

    class lightSource(forms.Form):
        type = forms.ChoiceField(label='Type', choices=(('point','Point'),
                                                        ('pencilbeam','PencilBeam'),
                                                        ('volume','Volume'),
                                                        ('ball','Ball'),
                                                        ('line','Line'),
                                                        ('fiber','Fiber'),
                                                        ('tetraface','Tetraface'),
                                                        ('cylinder','Cylinder'),
                                                        ('composite','Composite')))
        xPos = forms.IntegerField(label='X Position')
        yPos = forms.IntegerField(label='Y Position')
        zPos = forms.IntegerField(label='Z Position')
        power = forms.IntegerField(label='Power')