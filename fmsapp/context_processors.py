from .models import DepStock,Department,FarmStock

def getDepartments(request):
    dept = Department.objects.all()
    return {'dept':dept}

def getDepStocks(request):
    deptstock = DepStock.objects.all()
    return {'deptstock':deptstock}

def getFarmStocks(request):
    farstock = FarmStock.objects.all()
    return {'farstock':farstock}