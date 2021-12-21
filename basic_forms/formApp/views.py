from django.shortcuts import render
from .forms import survey_form
# Create your views here.

def index(request):
    return render(request, 'formApp/index.html')

def survey_form_view(request):
    form = survey_form()

    if request.method == 'POST':
        form=survey_form(request.POST)
        print(request.POST.items())
        # print("form data is:- ",form)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])


    return render(request,'formApp/forms.html',{'form':form})

