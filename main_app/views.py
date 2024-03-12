from django.shortcuts import render

dogs = [
    {'name': 'Gabi', 'breed': 'Maltese', 'description': 'Friendliest dog ever', 'age': 10},
    {'name': 'Chloe', 'breed': 'Maltese', 'description': 'Not very friendly :()', 'age': 11},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {
        'dogs': dogs
})