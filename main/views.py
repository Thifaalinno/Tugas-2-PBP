from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Thifaalinno Fawwaz Abdi',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
