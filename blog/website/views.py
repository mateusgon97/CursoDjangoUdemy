from django.shortcuts import render

def hello_blog(request):
    
    lista = 'Django', 'Python', 'Git', 'HTML', 'Banco de dados', 'Linux', 'Ngiux', 'Uwsgi', 'Systemctl'
    data = {'name': 'Curso de Django 3', 'lista_tecnologias': lista}
    return render(request, 'index.html', data)
