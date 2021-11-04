from django import forms
from .models import Founditems,ClaimPerson



# Person_id=models.AutoField
#     fname=models.CharField(max_length=40)
#     lname = models.CharField(max_length=40)
#     ph=models.IntegerField()
#     address=models.CharField(max_length=50)
#     city=models.CharField(max_length=20)
#     states=models.CharField(max_length=40)
#     zip=models.IntegerField()
#     obj_name=models.CharField(max_length=20)
#     date=models.DateField()
class PostForm(forms.ModelForm):
    class Meta:
        model=ClaimPerson
        fields=('fname','lname','ph','address','city','states','zip','claim_reason')
        widget={
            'fname': forms.TextInput(attrs={'class':'form-control'}),
            'lname': forms.TextInput(attrs={'class':'form-control'}),
            'ph': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'states': forms.Select(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
            'claim_reason': forms.Textarea(attrs={'class': 'form-control'})


            }




