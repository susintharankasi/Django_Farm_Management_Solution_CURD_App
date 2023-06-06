from django.shortcuts import render,redirect,resolve_url,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Sum
from django.contrib.auth import get_user_model,logout
from . models import Livestock, DepStock, FarmStock, LiveFarmStock
from django.contrib.auth.views import LoginView, TemplateView
from django.views.generic import CreateView,ListView,DetailView,UpdateView,View
from .forms import LoginForm,RegisterForm
from .forms import LivestockForm, DepStockForm, FarmStockForm, LiveFarmStockForm
from .library.fms import Income
# Create your views here.

class Index(TemplateView):
    template_name = 'fmsapp/home/index.html'
    
class Dashboard(LoginRequiredMixin,TemplateView):
    template_name = 'fmsapp/dashboard/index.html'
    login_url = 'fms:login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        TotalLivestock = Livestock.objects.all().aggregate(Sum('sell'))
        context["stocklist"] =TotalLivestock 
        res = []
        for key in TotalLivestock.keys() :
            res.append(TotalLivestock[key])
        y = str(res)
        y =y.replace("[","")
        y =y.replace("]","")
        if y  == "None":
            y = 0
        else:
            y = y
        y = int(y)
 

        
        Totalexpensels = Livestock.objects.all().aggregate(Sum('expense'))
        context["stocklistexp"] = Totalexpensels
        res = []
        for key in Totalexpensels.keys() :
            res.append(Totalexpensels [key])
        x = str(res)
        x=x.replace("[","")
        x=x.replace("]","")
        if x  == "None":
            x = 0
        else:
            x = x
        x = int(x)
        
        TotalLivestockf = LiveFarmStock.objects.all().aggregate(Sum('sell'))
        context["stocklistf"] = TotalLivestockf
        res = []
        for key in TotalLivestockf.keys() :
            res.append(TotalLivestockf[key])
        b = str(res)
        b =b.replace("[","")
        b =b.replace("]","")
        if b  == "None":
            b = 0
        else:
            b = b
        b = int(b)

        
        Totalexpenselsf = LiveFarmStock.objects.all().aggregate(Sum('expense'))
        context["stocklistexpf"] = Totalexpenselsf
        res = []
        for key in Totalexpenselsf.keys() :
            res.append(Totalexpenselsf [key])
        a = str(res)
        a=a.replace("[","")
        a=a.replace("]","")
        if a  == "None":
            a = 0
        else:
            a = a
        a = int(a)
   

        inc = Income(x)
        # Call the income method
        income = (inc.incomify(y))
        context["stocklistinc"] = income

        inc = Income(a)
        # Call the income method
        income = (inc.incomify(b))
        context["stocklistincf"] = income
        return context

#################################################################################

class Login(LoginView):
    template_name = 'fmsapp/home/login.html'
    form_class = LoginForm
    model = get_user_model()
    def get_success_url(self):
        query = get_user_model().objects.get(pk=self.request.user.pk)
        self.request.session['username'] = query.username
        #self.request.session['']
        url = resolve_url('fmsapp:dashboard')
        return url

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('fmsapp:login', permanent=True)

class AccountUpdate(LoginRequiredMixin,UpdateView):
    login_url = 'fms:login'
    model = get_user_model()
    form_class = RegisterForm
    template_name = 'fmsapp/account.html'
    success_url = reverse_lazy('fmsapp:dashboard')

class Register(CreateView):
    template_name = 'fmsapp/home/signup.html'
    form_class = RegisterForm
    model = get_user_model()
    success_url =  reverse_lazy('fmsapp:login')


##########################################################################
##############################################################################


#LiveStock department

class DepstockNew(LoginRequiredMixin,CreateView):
    model = DepStock
    login_url = 'fms:login'
    form_class = DepStockForm
    template_name  = 'fmsapp/depstock/create.html'

class DepstockDetail(LoginRequiredMixin,DetailView):
    model = DepStock
    login_url = 'fms:login'
    template_name = 'fmsapp/depstock/index.html'
    context_object_name = 'livestock'

class DepstockView(LoginRequiredMixin,ListView):
    model = DepStock
    login_url = 'fms:login'
    template_name = 'fmsapp/depstock/view.html'
    context_object_name = 'stocklist'

class DepstockUpdate(LoginRequiredMixin,UpdateView):
    model = DepStock
    login_url = 'fms:login'
    template_name = 'fmsapp/depstock/edit.html'
    form_class = DepStockForm

class DepstockDestroy(LoginRequiredMixin,View):
    login_url = 'fms:login'
    def get(self, request,pk):
        dept = DepStock.objects.get(pk=pk)
        dept.delete()
        return redirect('fms:all_stock')


#Live Stocks
class LiveAdd(LoginRequiredMixin,CreateView):
    login_url = 'fms:login'
    model = Livestock
    form_class = LivestockForm
    template_name = 'fmsapp/livestock/create.html'
    success_url = reverse_lazy('fmsapp:all_livestock')

class LiveList(LoginRequiredMixin,ListView):
    model = Livestock
    login_url = 'fms:login'
    template_name = 'fmsapp/livestock/index.html'
    context_object_name = 'livestocklist'


class LiveView(LoginRequiredMixin,DetailView):
    model = Livestock
    login_url = 'fms:login'
    template_name = 'fmsapp/livestock/single.html'
    context_object_name = 'dpt' 

def livestockdata(request, pk, format=None):
    livestocksp = Livestock.objects.filter(department=pk)
    context = {'livestocksp': livestocksp}
    return render(request, 'fmsapp/livestock/single.html', context)   



class LiveEdit(LoginRequiredMixin,UpdateView):
    model = Livestock
    login_url = 'fms:login'
    template_name = 'fmsapp/livestock/edit.html'
    form_class = LivestockForm
    success_url = reverse_lazy('fms:all_livestock') 

class LiveDestroy(LoginRequiredMixin,View):
    login_url = 'fms:login'
    def get(self, request,pk):
        dept = Livestock.objects.get(pk=pk)
        dept.delete()
        return redirect('fms:all_livestock')


##########################################################################
##############################################################################


#FarmStock department

class FarmstockNew(LoginRequiredMixin,CreateView):
    model = FarmStock
    login_url = 'fms:login'
    form_class = FarmStockForm
    template_name  = 'fmsapp/farmstock/create.html'
    success_url = reverse_lazy('fms:all_farmstock')

class FarmstockDetail(LoginRequiredMixin,DetailView):
    model = FarmStock
    login_url = 'fms:login'
    template_name = 'fmsapp/farmstock/index.html'
    context_object_name = 'farmstock'

class FarmstockView(LoginRequiredMixin,ListView):
    model = FarmStock
    login_url = 'fms:login'
    template_name = 'fmsapp/farmstock/view.html'
    context_object_name = 'farmlist'

class FarmstockUpdate(LoginRequiredMixin,UpdateView):
    model = FarmStock
    login_url = 'fms:login'
    template_name = 'fmsapp/farmstock/edit.html'
    form_class = FarmStockForm

class FarmstockDestroy(LoginRequiredMixin,View):
    login_url = 'fms:login'
    def get(self, request,pk):
        dept = FarmStock.objects.get(pk=pk)
        dept.delete()
        return redirect('fms:all_farmstock')


#Live Farm Stocks
class LivefarmAdd(LoginRequiredMixin,CreateView):
    login_url = 'fms:login'
    model = LiveFarmStock
    form_class = LiveFarmStockForm
    template_name = 'fmsapp/livefarmstock/create.html'
    success_url = reverse_lazy('fmsapp:all_livefarmstock')

class LivefarmList(LoginRequiredMixin,ListView):
    model = LiveFarmStock
    login_url = 'fms:login'
    template_name = 'fmsapp/livefarmstock/index.html'
    context_object_name = 'livefarmlist'


class LivefarmView(LoginRequiredMixin,DetailView):
    model = LiveFarmStock
    login_url = 'fms:login'
    template_name = 'fmsapp/livefarmstock/single.html'
    context_object_name = 'dpt' 

def livefarmdata(request, pk, format=None):
    livefarmsp = LiveFarmStock.objects.filter(farmdepartment=pk)
    context = {'livefarmsp': livefarmsp}
    return render(request, 'fmsapp/livefarmstock/single.html', context)   


class LivefarmEdit(LoginRequiredMixin,UpdateView):
    model = LiveFarmStock
    login_url = 'fms:login'
    template_name = 'fmsapp/livefarmstock/edit.html'
    form_class = LiveFarmStockForm
    success_url = reverse_lazy('fms:all_livefarmstock') 

class LivefarmDestroy(LoginRequiredMixin,View):
    login_url = 'fms:login'
    def get(self, request,pk):
        dept = LiveFarmStock.objects.get(pk=pk)
        dept.delete()
        return redirect('fms:all_livefarmstock')

###############################################################


#def deleteconfirm(request):
#    return render(request,'fmsapp/depstock/deleteconfirm.html')

