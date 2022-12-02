from django.shortcuts import render
from django.http import HttpResponse
from .forms import delivery

# Create your views here.

def form(request):
    return render(request, 'Form.html')

def appointment(request):
    name = request.POST.get('name', 'Javapon')
    email = request.POST.get('email', 'javapon@java.js')
    phone_number = request.POST.get('phone-number', '+79856782343')
    service = request.POST.get('select-service', 'JavaScript')
    input_text = request.POST.get('input__text', 'javajavajavajavafrontfronfront')
    return HttpResponse(f'<p>Ваше имя: {name} <br>Ваш еmail: {email}<br> Ваш телефонный номер: {phone_number}<br> Ваш комментарий: {input_text} </p>')

def adress(request):
    Delivery = delivery()
    return render(request, 'userAderss.html', {'form': Delivery})

def order(request):
    name = request.GET.get('name', 'Javapon')
    surname = request.GET.get('surname', 'Javaponov')
    email = request.GET.get('email', 'javapon@mail.js')
    country = request.GET.get('country', 'Javaponstan')
    city = request.GET.get('city', 'Noviy Javapon')
    street = request.GET.get('street', 'Javapona')
    houseNum = request.GET.get('houseNum', '+123132')
    flat = request.GET.get('flat', '123')
    return HttpResponse(f'{name} {surname}, проверьте адресс: <br> {email} <br>country: {country}<br>city: {city}<br>street: {street}<br>Num of house: {houseNum}<br>flat: {flat}')