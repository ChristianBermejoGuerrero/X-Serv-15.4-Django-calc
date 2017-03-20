from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# No hace falta comprobar que sean numeros porque ya lo hacemos al meter en la url solo uno o mas numeros

def suma (request, num1, num2):
    resultado = int(num1) + int(num2)
    return HttpResponse ("El resultado de " + str(num1) + " + " + str(num2) + " = " + str(resultado))

def resta (request, num1, num2):
    resultado = int(num1) - int(num2)
    return HttpResponse ("El resultado de " + str(num1) + " - " + str(num2) + " = " + str(resultado))

def multiplicacion (request, num1, num2):
    resultado = int(num1) * int(num2)
    return HttpResponse ("El resultado de " + str(num1) + " * " + str(num2) + " = " + str(resultado))

def division (request, num1, num2):
    try:
        resultado = float(num1) / float(num2)
        return HttpResponse ("El resultado de " + str(num1) + " / " + str(num2) + " = " + str(resultado))
    except ZeroDivisionError:
    	return HttpResponse ("No es posible dividir entre 0, introduzca otro valor")

def default (request):
    return HttpResponse ("Has introducido algo mal, por favor vuelve a intentarlo. Recuerda localhost:1234/num1(+,-,*,/)num2")
