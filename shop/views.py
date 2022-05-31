from cmath import nan
from django.shortcuts import render, redirect
from shop.models import Cart, Cook, Dish
from django.contrib.auth.forms import UserCreationForm
from shop.recommender import Recommender
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
recommender = Recommender()
# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def foodzone(request):
    dish = Dish.objects.all()
    dish = dish.order_by('-specialty')
    m = {'dishes' : dish}
    if request.user.is_authenticated:
        cust = Cook.objects.filter(user=request.user).first()
        m['cook'] = cust
    return render(request,'shop/foodzone.html',context=m)

def dishView(request,dishId):
    dish = Dish.objects.filter(id=dishId).first()
    
    recommended = recommender.recommend(str(dish.name).lower())
    recom = []
    for rec in recommended:
        recom.append(Dish.objects.filter(name=rec).first())
    m = { 'dish': dish,'recommended': recom}
    return render(request,'shop/dish-view.html',context=m)

def payment(request):
    return render(request, 'shop/payment.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def filter(request):
    f = request.POST['flavour']
    p = request.POST['preference']
    t = request.POST['timing']
    pref = True
    if (p == 'veg'):
        pref = True
    else:
        pref = False
    dishes = Dish.objects.filter(flavour= f,preference=t,veg=pref)
    m = { 'dishes': dishes}
    return render(request,'shop/filter.html',context=m)

def reset(request):
    return redirect('/')

def authenti(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            print(username)
            user = authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                alert = True
                return render(request, "shop/login.html", {"alert":alert})
            
    return render(request, "shop/login.html")

def loginn(request):
    return render(request,'shop/login.html')

def signup(request):
    return render(request,'shop/signup.html')

def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":   
            username = request.POST['username']
            full_name=request.POST['full_name']
            password1 = request.POST['password']
            phone_number = request.POST['phone_number']
            role = int(request.POST['role'])
            email = request.POST['email']
            print(role)
            user = User.objects.create_user(username=username, password=password1, email=email)
            user.save()
            cook = Cook.objects.create(user=user,name = full_name,number = phone_number,role= role,email=email)
            cook.save()
            return render(request, "shop/login.html")
    return render(request, "shop/signup.html")


def Logout(request):
    logout(request)
    alert = True
    return redirect('/')

def myDish(request):
    m = {}
    if request.user.is_authenticated:
        cook = Cook.objects.filter(user=request.user).first()
        if cook.role:
            myDish = Dish.objects.filter(cook = cook)
            m['myDish'] = myDish
            print(m['myDish'])
    return render(request,'shop/myDish.html',m)

def deleteDish(request,dishID):
    if request.user.is_authenticated:
        dish = Dish.objects.filter(id=dishID).first()
        Dish.delete(dish)
    return redirect('/my-dish')

def addDish(request):
    if request.user.is_authenticated:
        cook = Cook.objects.filter(user=request.user).first()
        if cook.role:
            name = request.POST['name']
            price = int(request.POST['price'])
            image = request.POST['image']
            veg = int(request.POST['veg'])
            preference = request.POST['preference']
            specialty = int(request.POST['specialty'])
            flavour = request.POST['flavour']
            if (specialty == nan):
                specialty = 0
            newDish = Dish(name = name,price = price,img= image,veg = veg,preference= preference,specialty = specialty,flavour= flavour,cook = cook)
            newDish.save()
    return redirect('/my-dish')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            return render(request, 'shop/thanks.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'shop/contact.html', context)

def thanks(request):
    return render(request, 'shop/thanks.html')

def AddToCart(request,dishID):
    if request.user.is_authenticated:
        item = Dish.objects.filter(id=dishID).first()
        cook = Cook.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(cust= cook).first()
        if cart:
            cart.items.add(item)
        else:
            newCart = Cart(cust=cook)
            newCart.save()
            newCart.items.add(item)
            
        return redirect('/')
def clear(request):
    return render(request, 'shop/cart.html')
def getCart(request):
    m = {}
    cart_total = 0
    if request.user.is_authenticated:
        cook = Cook.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(cust= cook).first()
        if cart:
            cart_items = cart.items.all()
            cart_total = sum([item.price for item in cart_items])
            m['cart_items'] = cart_items
            m['cart_total'] = cart_total
    return render(request,'shop/cart.html',m)

def clear(request):
    cart = Cart(request.session)
    cart = Cart.objects.all()
    cart.delete()
    return redirect('/foodzone')
         
def DeleteCartItem(request,disID):

    if request.user.is_authenticated:
        item = Dish.objects.filter(id=disID).first()
        cook = Cook.objects.filter(user=request.user).first()
        cart = Cart.objects.filter(cust= cook).first()
        if cart:
            cart.items.remove(item)
    return redirect('/view-cart')