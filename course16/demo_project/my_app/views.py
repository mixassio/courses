from django.shortcuts import HttpResponse, render


def index(request):
    return HttpResponse('Hi!')


def test(request):
    if request.method == 'GET':
        return render(request, 'hello.html', {
            'my_var': [1, 2, 3],
        })
