import random

from django.shortcuts import render

from .data import tours, title, subtitle, description, departures


def MainView(request):
    main_tours = {}
    while len(main_tours) < 6:
        key = random.randint(1, len(tours))
        if key not in main_tours:
            main_tours[key] = tours[key]

    data = {
        'title': title,
        'subtitle': subtitle,
        'description': description,
        'departures': departures,
        'tours': main_tours
    }
    return render(request, 'tours/index.html', context=data)


def DepartureView(request, departure):
    departure_tours = {}
    costs, nights = [], []

    for key in tours:
        if tours[key]['departure'] == departure:
            departure_tours[key] = tours[key]
            costs.append(tours[key]['price'])
            nights.append(tours[key]['nights'])

    page_departure = departures[departure].split()[-1]
    min_cost = min(costs)
    max_cost = max(costs)
    min_nights = min(nights)
    max_nights = max(nights)

    data = {
        'title': title,
        'departures': departures,
        'page_departure': page_departure,
        'min_cost': min_cost,
        'max_cost': max_cost,
        'min_nights': min_nights,
        'max_nights': max_nights,
        'tours': departure_tours
    }
    return render(request, 'tours/departure.html', context=data)


def TourView(request, id):
    title_page = tours[id]['title'] + ' ' + ('★' * int(tours[id]['stars']))
    departure = tours[id]['departure']
    city = departures[departure].split(' ')[-1]
    data = {
        'title': title_page,
        'departures': departures,
        'city': city,
        'tour': tours[id]
    }
    return render(request, 'tours/tour.html', context=data)
