from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Produk,Order,Customer
from .forms import OrderForm

# Create your views here (dashboard).
@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    orders=Order.objects.all()
    customer=Customer.objects.all()
    total_order=orders.count()
    deliver=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()

    context={
        'orders': orders,
        'customer': customer,
        'total_order': total_order,
        'deliver': deliver,
        'pending': pending,
    }
    return render (request, 'dashboard.html', context)
    # template  = loader.get_template('dashboard.html',context)
    # return HttpResponse(template.render())

def produk(request):
    item=Produk.objects.all()
    context={
        'item':item
    }
    return render (request, 'produk.html', context)
   
def customer(request,pk_test):
   customer=Customer.objects.get(id=pk_test)
   order=customer.order_set.all()
   order_count=order.count()
   context={
       'pk_test':pk_test,'customer':customer, 'order':order, 'order_count': order_count }
   return render (request, 'customer.html',context )

def orderCreate(request):
    form=OrderForm()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'order_create.html', context)

def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=="POST":
        form=OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        'form':form,
    }

    return render(request, 'order_create.html', context)

def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect('/')
    context={
        'order':order
    }
    return render(request, 'delete.html', context)