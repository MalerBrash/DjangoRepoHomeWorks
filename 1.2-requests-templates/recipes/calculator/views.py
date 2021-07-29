from django.conf import settings
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
template_name = 'calculator/recipes.html'

def prepare_context(request, name_dish):
    page = {
        'Главную страницу': reverse('home')
    }

    service = request.GET.get('servings')
    if service:
        context = {
            'recipe': {key: round(val * int(service), 1) for key, val in DATA[name_dish].items()},
            'page': page
        }
    else:
        context = {
            'recipe': DATA[name_dish],
            'page': page
        }
    return context

def home_view(request):
    pages = {
        'Главная страница': reverse('home'),
        'Показать рецепт классического омлета': reverse('omlet'),
        'Показать рецепт итальянской пасты': reverse('pasta'),
        'Показать рецепт идеального бутерброда': reverse('buter')
    }
    context = {
        'pages': pages
    }
    return render(request, 'calculator/index.html', context)

def omlet_view(request):
    return render(request, template_name, prepare_context(request, 'omlet'))

def pasta_view(request):
    return render(request, template_name, prepare_context(request, 'pasta'))

def buter_view(request):
    return render(request, template_name, prepare_context(request, 'buter'))
