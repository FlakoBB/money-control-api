from django.shortcuts import render

def income(request):
  return render(request, 'income/index.html')
