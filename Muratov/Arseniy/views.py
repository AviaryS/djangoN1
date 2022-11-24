from django.shortcuts import render
from django.http import HttpResponse


def index(request, fullName, age, interests):
    return HttpResponse(f"""<h2>Я {fullName} <br> Мне {age} <br> {interests}</h2>""")


def about(requst, home, estimates, isLikeStudy):
    return HttpResponse(f'<h2>Я из {home} <br> В школе {estimates} <br> И я {isLikeStudy}</h2>')


def contacts(requst, github, tg):
    return HttpResponse(f'<h2>Мой гитхаб: {github} <br> Мой телеграмм: {tg}</h2>')
