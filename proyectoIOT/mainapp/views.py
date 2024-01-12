from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    if request.method =='POST':
        valor = request.POST.get('valor')

    return render(request, 'mainapp/index.html', {
        'title': 'Inicio',
        'nombre': 'Luis Ikeda',
        'valor': 'valor'
    })

# def state_led(request):

#     if request.method =='POST':
#         valor = request.POST.get('valor')

#     return render(request, 'users/login.html', {
#         'title': 'Identifícate'
#     })