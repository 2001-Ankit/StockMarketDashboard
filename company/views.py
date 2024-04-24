from django.shortcuts import render
from .models import Company
from django.views import View
# Create your views here.

class BaseView(View):
    context ={}


class CompanyView(BaseView):
    def get(self,request):
        self.context['companies'] = Company.objects.all()
        return render(request,'dashboard.html',self.context)