from django.shortcuts import render, reverse, redirect
from django.views.generic import View
from .models import Listing, Amenity, Host, Review, User, Calendar
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
class Signup(View):
    def get(self, request):
        if request.user.is_authenticated:
            print('Logged in')
            return render(request, 'logoutHome.html', {'username': request.user.username})
        return render(request, 'signup.html')

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        check_password = request.POST.get('check_password', '')
        mail = request.POST.get('mail', '')

        if password != check_password:
            return HttpResponse('Inconsistent password')
        exists = User.objects.filter(username=username).exists()
        if exists:
            return HttpResponse('The account is existed.')
        User.objects.create_user(username=username, password=password, email=mail)
        return redirect(reverse('login'))

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        exists = User.objects.filter(username=username).exists()
        if not exists:
            return HttpResponse('The account has not sign up. Please sign up first.')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'logoutHome.html', {'username': username})
        else:
            return HttpResponse('Incorrect Password')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))
    def post(self, request):
        pass

class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            print('Logged in')
            return render(request, 'logoutHome.html', {'username': request.user.username})
        return render(request, 'home.html')



    def post(self, request):
        indate = request.POST.get('indate')
        outdate = request.POST.get('outdate')
        p_num = request.POST.get('p_num')
        city = request.POST.get('city')


        print(type(indate), type(outdate))
        print(indate, outdate)

        if indate > outdate:
            return render(request, 'incorrect.html')


        if city == 'Taipei':
            result = Listing.objects.filter(amenity__city='Taipei', amenity__bed__gte=p_num, calendar__available=True).values()
            amen_result = Amenity.objects.filter(city__exact='Taipei',  bed__gte=p_num, listing__calendar__available=True).values()
            review = Review.objects.filter(listing__amenity__city__exact='Taipei', listing__amenity__bed__gte=p_num, listing__calendar__available=True).values()
        elif city == 'San Fran':
            result = Listing.objects.filter(amenity__city='San Fran', amenity__bed__gte=p_num, calendar__available=True).values()
            amen_result = Amenity.objects.filter(city__exact='San Fran',  bed__gte=p_num, listing__calendar__available=True).values()
            review = Review.objects.filter(listing__amenity__city__exact='San Fran',
                                           listing__amenity__bed__gte=p_num, listing__calendar__available=True).values()
        elif city == 'New York':
            result = Listing.objects.filter(amenity__city='New York', amenity__bed__gte=p_num, calendar__available=True).values()
            amen_result = Amenity.objects.filter(city__exact='New York',  bed__gte=p_num, listing__calendar__available=True).values()
            review = Review.objects.filter(listing__amenity__city__exact='New York',
                                           listing__amenity__bed__gte=p_num, listing__calendar__available=True).values()
        elif city == 'Roma':
            result = Listing.objects.filter(amenity__city='Roma', amenity__bed__gte=p_num, calendar__available=True).values()
            amen_result = Amenity.objects.filter(city__exact='Roma',  bed__gte=p_num, listing__calendar__available=True).values()
            review = Review.objects.filter(listing__amenity__city__exact='Roma',
                                           listing__amenity__bed__gte=p_num, listing__calendar__available=True).values()
        elif city == 'Paris':
            result = Listing.objects.filter(amenity__city='Paris', amenity__bed__gte=p_num, calendar__available=True).values()
            amen_result = Amenity.objects.filter(city__exact='Paris',  bed__gte=p_num, listing__calendar__available=True).values()
            review = Review.objects.filter(listing__amenity__city__exact='Paris',
                                           listing__amenity__bed__gte=p_num, listing__calendar__available=True).values()
        elif city == 'Tokyo':
            result = Listing.objects.filter(amenity__city='Tokyo', amenity__bed__gte=p_num, calendar__available=True).values()
            amen_result = Amenity.objects.filter(city__exact='Tokyo',  bed__gte=p_num, listing__calendar__available=True).values()
            review = Review.objects.filter(listing__amenity__city__exact='Tokyo',
                                           listing__amenity__bed__gte=p_num, listing__calendar__available=True).values()

        return render(request, 'search.html', {'indate': indate, 'outdate': outdate, 'p_num': p_num, 'city': city, 'result': result, 'amen_result': amen_result, 'review': review})

class Reservation(View):
    def get(self, request):

        return render(request, 'reservation.html')

    def post(self, request):
        listing_id = request.POST.get('listing_id')
        listing_name = request.POST.get('listing_name')
        bed = Amenity.objects.filter(listing__name__exact=listing_name).values('bed')
        rules = Amenity.objects.filter(listing__name__exact=listing_name).values('rules')
        rate = Review.objects.filter(listing__name__exact=listing_name).values('rate')
        indate = request.POST.get('indate')
        outdate = request.POST.get('outdate')
        p_num = request.POST.get('p_num')
        city = request.POST.get('city')
        return render(request, 'reservation.html', {'listing_id': listing_id, 'listing_name': listing_name, 'bed': bed, 'rules': rules, 'rate': rate, 'indate': indate, 'outdate': outdate, 'p_num': p_num})

class Payment(View):
    def get(self, request):
        pass
    def post(self, request):
        cc_name = request.POST.get('cc_name')
        cc_number = request.POST.get('cc_number')
        cc_expiry = request.POST.get('cc_expiry')
        cc_cvv = request.POST.get('cc_cvv')
        listing_name = request.POST.get('listing_name')
        listing_id = Listing.objects.get(name=listing_name).id
        indate = request.POST.get('indate')
        outdate = request.POST.get('outdate')
        print(listing_id, listing_name, indate, outdate)

        reserve = Calendar.objects.get(listing_id=listing_id)
        reserve.available = False
        reserve.dateFrom = indate
        reserve.dateEnd = outdate
        reserve.save()


        return render(request, 'complete.html')

class About(View):
    def get(self, request):
        return render(request, 'about.html')

class Faqs(View):
    def get(self, request):
        return render(request, 'faqs.html')



