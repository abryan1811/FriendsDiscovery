from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from users.models import UserDetails
from django.contrib.auth.models import User
from django.core.paginator import Paginator


# Create your views here.
def userprofile(request):

    """ A view to return the users profile page """

    userinfo = UserDetails.objects.get(user=User.objects.get(
        username=request.user.username))

    data = Post.objects.all().order_by('date_posted').reverse()
    paginator = Paginator(data, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'userinfo': userinfo, 'data': data, 'page_obj': page_obj}
    return render(request, "profilepage/userprofile.html", context)


def update_info(request):

    return render(request, "profilepage/update_info.html")


def update_image(request):
    
    return render(request, "profilepage/update_image.html")


def newpost(request):
    """ A view to return the users profile page """
    if request.method == 'POST':
        BlogPostForm = PostForm(request.POST)

        if BlogPostForm.is_valid():
            BlogPostForm.instance.user = request.user
            BlogPostForm.save(commit=True)
            return redirect('userprofile')

    else:
        BlogPostForm = PostForm()

    context = {'BlogPostForm': BlogPostForm}
    return render(request, 'profilepage/newpost.html', context)
