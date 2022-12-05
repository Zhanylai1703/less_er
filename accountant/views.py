from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Profile
from .forms import ProfileForm
from .utils import password_validation

# Create your views here.
def index_view(request):
    message = None
    form = ProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    
    return render(
        request,
        'login.html',
        {'form':form, 'message': message}
        )
    

def index_view2(request):
    return HttpResponse(3+3)

