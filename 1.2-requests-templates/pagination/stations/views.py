from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    current_page = reverse('bus_stations')
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': [],

    }
    with open(settings.BUS_STATION_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for i in reader:
            dic = {
                'Name': i['Name'],
                'Street': i['Street'],
                'District': i['District']
            }
            context['bus_stations'].append(dic)
    page = int(request.GET.get('page', 1))
    element_per_page = 10
    paginator = Paginator(context['bus_stations'], element_per_page)
    page_ = paginator.get_page(page)
    page_list = page_.object_list
    context['bus_stations'] = page_list
    context['pages'] = {
        'number': page,
        'next_page_number': page_.next_page_number() if page_.has_next() else paginator.num_pages,
        'previous_page_number': page_.previous_page_number() if page_.has_previous() else 1,
        'page_has_next': page_.has_next(),
        'page_has_prev': page_.has_previous(),
        'num_pages': paginator.num_pages
    }

    return render(request, 'stations/index.html', context)
