from django.shortcuts import render

posts = [
    {
        'author': 'Omaewa',
        'title': 'Blog_Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Nani',
        'title': 'Blog_Post 2',
        'content': 'Second post content',
        'date_posted': 'December 7, 2018'
    }
]

def homepage(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/homepage.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
