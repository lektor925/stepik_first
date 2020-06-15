from django.shortcuts import render


def MainView(request):
    return render(request, 'tours/index.html')


def DepartureView(request, departure):
    return render(request, 'tours/departure.html')


def TourView(request, id):
    return render(request, 'tours/tour.html')
