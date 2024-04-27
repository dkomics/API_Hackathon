import requests
from django.shortcuts import render

def index(request):
    # Fetching a random fact
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    fact_data = response.json()
    fact = fact_data['text']

    # Fetching a random dog image
    dog_response = requests.get('https://dog.ceo/api/breeds/image/random')
    dog_data = dog_response.json()
    dog = dog_data['message']

    # Fetching a random student
    student_response = requests.get('https://freetestapi.com/api/v1/students')
    student_data = student_response.json()
    # Randomizing student
    import random
    random_student = random.choice(student_data)
    name = random_student['name']

    return render(request, 'templates/index.html', {'fact': fact, 'dog': dog, 'name': name})
