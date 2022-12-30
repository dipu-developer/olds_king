from django.shortcuts import render
from django.http import JsonResponse
from .models import Catogery,SubCatogery,AddData
# import pandas as pd
# import uuid
# Create your views here.

def dashboard(request):
    mycat=Catogery.objects.all() 
    cat1 =SubCatogery.objects.filter(cat=1)
    cat2 =SubCatogery.objects.filter(cat=2)
    cat3 =SubCatogery.objects.filter(cat=3)
    cat4 =SubCatogery.objects.filter(cat=4)
    data=AddData.objects.values()
    data={
        'cat1':cat1,
        'cat2':cat2,
        'cat3':cat3,
        'cat4':cat4,
        'mycat': mycat,
        'data': data
    }
    return render(request,'dashboard.html',data)

def show_ten_data(request):
    mydata=AddData.objects.all().order_by('-date')[:9]
    print('its calles')
    return JsonResponse({'alldata':mydata})


def load_mrp(request):
    mrp= request.POST['mrp']
    lt=SubCatogery.objects.filter(name=mrp).values()
    mrp_lst=list(lt)
    print(mrp_lst)
    return JsonResponse({'status':'Save','mrp':mrp_lst})

def sub_cat(request):
    mycat =request.POST['myscat']
    print("the vale of my cat is")
    print(mycat)
    cat =SubCatogery.objects.filter(cat=mycat).values()
    print(cat)
    data= list(cat)
    # print(cat)                                                                                                                          
    # return render(request,'subcat.html',data)
    return render(request,'list.html',{'data':data})

def add_data(request):
    cat = request.POST['cat']
    subcat = request.POST['subcat']
    mrp = request.POST['mrp']
    quantity = request.POST['quantity']
    b=int(mrp)
    a=int(quantity)
    total=a*b
    order = AddData.objects.create(catogery=cat,sub_catogery=subcat,mrp=mrp,quantity=quantity,total=total)
    data=AddData.objects.values()
    order= list(data)
    return JsonResponse({'status':'done','data':order})

def records(request):
    data=AddData.objects.values()
    return render(request,'records.html',{'data':data})

def exel_convert(request):
    obj= AddData.objects.all()
    data= []

    for i in obj:
        data.append({
            'Id': i.id,
            'Catogery': i.catogery,
            'Sub Catogery': i.sub_catogery,
            'Price':i.mrp,
            'Quantity':i.quantity,
            'Total':i.total,
            'Date':i.date,
        })
    print(data)
    pd.DataFrame(data).to_excel('output')

    return JsonResponse({'status':200})