from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Products,Cart

# Create your views here.
def home(request):
    return render(request, "home.html")

def search(request):
    query = request.GET['search']
    if len(query)>100:
        post = Products.objects.none()
    else:
        postName = Products.objects.filter(pname__icontains=query)
        postPrice = Products.objects.filter(price__icontains=query)
        post = postName.union(postPrice)
    if post.count()==0:
        messages.warning(request,"No result found")
    params = {"post":post ,"query":query}

    return render(request, "search.html", params)

def products(request):
    data =  Products.objects.all()
    context = {"data":data}
    return render(request, "products.html",context)

def cart(request):
    cart_items = Cart.objects.filter(user = request.user)
    total_price = sum(items.product.price * items.quantity for items in cart_items )
    context = {"cart_items":cart_items , "total_price":total_price}
    return render(request, "cart.html", context)

def addcart(request, id):
    if request.user.is_authenticated:
        products = Products.objects.get(id=id)
        newcart, created =Cart.objects.get_or_create(product=products,user=request.user)
        newcart.quantity +=1
        newcart.save()
        return redirect("/cart")
    else:
        return redirect("/login")

def delcart(request, id):
    citems = Cart.objects.get(id=id)
    citems.delete()
    return redirect("/cart")

def handlesignup(request):
    if request.method == "POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        passw=request.POST.get("pass")
        cpassw=request.POST.get("cpass")
        # print(uname,email,passw,cpassw)
        if passw != cpassw:
            messages.warning(request, "please enter same password")
            return redirect("/signup")
        
        try:
            if User.objects.get(email=email):
                messages.warning(request, "this email already exists")
                return redirect("/signup")
        except:
            pass
        myuser = User.objects.create_user(uname,email,passw)
        myuser.save()
        messages.info(request, "sigin successfull")
        return redirect("/login")
    
    return render(request, "signup.html")

def handlelogin(request):
    if request.method == "POST":
        uname=request.POST.get("username")
        passw=request.POST.get("pass")
        myuser = authenticate(username=User.objects.get(email=uname),password=passw)
        if myuser is not None:
            login(request, myuser)
            messages.info(request, "success full loggedin")
            return redirect("/")
        else:
            messages.error(request, "login failed")
    return render(request, "login.html")





def handlelogout(request):
    logout(request)
    messages.info(request, "success full loggedout")
    return redirect("/")


