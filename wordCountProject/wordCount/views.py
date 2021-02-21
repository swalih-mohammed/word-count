from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import operator
from .forms import URLForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = URLForm(request.POST or None)
        # print(form.errors)
        if form.is_valid():
            url = form.cleaned_data["url"]
            # print(url)
    try:
        # print("trying")
        # print(url)
        # url = "https://www.bbc.com/arabic"
        page = requests.get(url).text
        soup = BeautifulSoup(page, "lxml")
        # testing = [tag.name for tag in soup.find_all()]
        # print(testing)
        # text = [p.text for p in soup.find_all('p')]
        text = [p.text for p in soup.find_all()]

        word_dict = {}

        for sentance in text:
            words = sentance.split()
            for word in words:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

        word_list = []

        for key, value in word_dict.items():
            word_list.append((value, key))

        # print(word_list)

        sorted_dict = sorted(
            word_dict.items(), key=operator.itemgetter(1), reverse=True)

        context = {'word_dict': sorted_dict}
    except:
        print("error")
        context = {}
    return render(request, 'wordCount/home.html', context)
