import csv

from django.shortcuts import render


def inflation_view(request):
    template_name = 'inflation.html'
    with open('inflation_russia.csv') as file:
        reader = csv.reader(file, delimiter=';')
        info = []
        for a in reader:
            info.append(a)

    # чтение csv-файла и заполнение контекста
    context = {'info': info}

    return render(request, template_name,
                  context)