from django.shortcuts import render

def exemplo(request):
    return render(request, 'exemplos/exemplo.html')
