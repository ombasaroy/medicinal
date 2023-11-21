from django.shortcuts import render, redirect
from .models import Strains, Sliders, Mainpage
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.db.models import Q #allows us to search all columns in table


# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    # ourstrains = Strains.objects.order_by('cost_blunt')[:8]
    paginator = Paginator(Strains.objects.all().order_by('?'), 4)  # displays 4 products in a random order
    new_page = request.GET.get('page')
    strains = paginator.get_page(new_page)
    slides = Mainpage.objects.all()[0]
    context = {"strains": strains, "nav": 'home', "slides": slides}

    return render(request, 'home.html', context)


def signupform(request):
    return render(request, 'signupform.html')


def loginform(request):
    return render(request, 'loginform.html', {'nav': 'signin'})


def cart(request):
    return render(request, 'cart.html', {'nav': 'cart'})


def addstrain(request):
    return render(request, 'addstrain.html')


def orders(request):
    straincount = Strains.objects.all().count()
    userscount = User.objects.all().count()
    context = {"straincount": straincount, "userscount": userscount}

    return render(request, 'admin/orders.html', context)


def strains(request):
    paginator = Paginator(Strains.objects.all().order_by('id'), 3)  # displays 4 products in a random order
    new_page = request.GET.get('page')
    strains = paginator.get_page(new_page)

    straincount = Strains.objects.all().count()
    userscount = User.objects.all().count()

    context = {'strains': strains, "straincount": straincount, "userscount": userscount}

    return render(request, 'admin/strains.html', context)


def addStrainToDb(request):
    if request.method == 'POST':
        strain_name = request.POST.get('strain_name').title()
        thc = request.POST.get('thc')
        effect = request.POST.get('effect')
        cost_blunt = request.POST.get('cost_blunt')
        product_image = request.FILES.get('product_image')

        query = Strains(strain_name=strain_name, thc=thc,
                        effect=effect, cost_blunt=cost_blunt,
                        product_image=product_image)
        query.save()

        messages.success(request, 'Strain added')

        return redirect('addstrain')


def userSignUp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password1')

        query = User.objects.create_user(email, username, password)
        query.save()

        messages.success(request, 'Success!')

        return redirect('signupform')


def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')
        userlog = authenticate(request, username=username, password=password)

        if userlog is not None:
            login(request, userlog)
            return redirect('/home')
        else:
            messages.error(request, "  Username or password is incorrect")
            return redirect('/loginform')

    return render(request, 'loginform.html')


def editstrain(request, id):
    if request.method == 'POST':
        strain_name = request.POST['strain_name']
        thc = request.POST['thc']
        effect = request.POST['effect']
        cost_blunt = request.POST['cost_blunt']
        product_image = request.FILES['product_image']

        update = Strains.objects.get(id=id)
        update.strain_name = strain_name
        update.thc = thc
        update.effect = effect
        update.cost_blunt = cost_blunt
        update.product_image = product_image

        update.save()
        messages.success(request, '  Strain updated successfully')
        return redirect('strains')

    fetchstrains = Strains.objects.get(id=id)
    context = {"strain": fetchstrains}

    return render(request, 'editstrain.html', context)


def deletestrain(request, id):
    fetchStrain = Strains.objects.get(id=id)
    fetchStrain.delete()

    messages.success(request, '  Strain deleted successfully')
    return redirect('strains')


def adminbase(request):
    return render(request, 'admin/adminbase.html')


def deliverydetails(request):
    return render(request, 'deliverydetails.html')


def resetpassword(request):
    return render(request, 'resetpassword.html')


def logoutuser(request):
    logout(request)
    return redirect('loginform')


def sliders(request):
    sliders = Sliders.objects.all()
    context = {"sliders": sliders}
    return render(request, 'sliders.html', context)


def searchresult(request):
    if request.method == 'GET':
        search  = request.GET.get('searchstrains')
        if search:
            strains = Strains.objects.filter(Q(strain_name__icontains=search) | Q(effect__icontains=search))
            context = {"strains": strains, "search": search}
            return render(request, 'admin/searchresult.html', context)
        return render(request, 'admin/searchresult.html')

