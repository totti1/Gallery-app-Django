from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image, Category
import pyperclip

# Create your views here.
def home(request):
    images = Image.objects.all()
    # print(images)
    return render(request, 'home.html', {"images":images})

def photo(request,image_id):
    
    image = Image.objects.get(id = image_id)
    return render(request,"photo.html", {"image":image})

def search_results(request):
    search_term = None
    searched_image = None
    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_category = Category.search_by_name(search_term)
        for item in searched_category:
            searched_image = Image.search_by_category(item.id)
        # searched_image = Image.search_by_title(search_term)
        # print(searched_image)
        message = f"{search_term}"

        return render(request, 'results.html',{"message":message, "images": searched_image})

    else:
        message = "Sorry we don't have any category called like "+ search_term
        return render(request, 'results.html',{"message":message})
def get_link(request, img_id):
    image = Image.objects.get(id = img_id)
    test = pyperclip.copy("127.0.0.1:8000"+image.image.url)
    # print(images)
    return redirect(photo, img_id)
# def news_today(request):
#     date = dt.date.today()
#     news = Article.todays_news()
#     return render(request, 'all-news/today-news.html', {"date": date,"news":news})

# def convert_dates(dates):

#     # Function that gets the weekday number for the date.
#     day_number = dt.date.weekday(dates)

#     days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

#     # Returning the actual day of the week
#     day = days[day_number]
#     return day

# def past_days_news(request, past_date):
#     try:
#         # Converts data from the string Urrequest, 'home.html', {"images":images}l
#         date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False

#     if date == dt.date.today():
#         return redirect(news_today)

#     news = Article.days_news(date)
#     return render(request, 'all-news/past-news.html',{"date": date,"news":news})

# def search_results(request):

#     if 'article' in request.GET and request.GET["article"]:
#         search_term = request.GET.get("article")
#         searched_articles = Article.search_by_title(search_term)
#         message = f"{search_term}"

#         return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'all-news/search.html',{"message":message})

# def article(request,article_id):
#     try:
#         article = Article.objects.get(id = article_id)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"all-news/article.html", {"article":article})