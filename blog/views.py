from django.shortcuts import render, redirect, HttpResponse
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication

from . import serializers

# Create your views here.
from .models import Blogform, Blog
from .models import comment
from django.contrib.auth.decorators import login_required, permission_required
from django.views import View
from django.contrib import messages
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin


def home_blog(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', context={'blogs': blogs})


#   Below is the example of class based view.
class contact_blog(View):
    template_name=''
    def get(self,request):
        return render(request, self.template_name)
    def post(self,request):
        query = request.POST['query']
        email = request.POST['email']
        import smtplib
        my_email = "ankitdevkota107@gmail.com"
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        password = "hlcm ejly eobf uyfr"
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="growmore202@gmail.com",
                            msg=f"Subject:New query \n\n{query} \n\n {email}")

        connection.close()
        messages.add_message(request, messages.SUCCESS, "Message sent successfully😊")
        return redirect('contact')



def about_blog(request):
    return render(request, 'about.html')


def show_blog(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        blog_id = id
        comment_body = request.POST.get('my_text_area')
        commented_post = Blog.objects.get(id=blog_id)
        comment_author = request.user

        comment.objects.create(body=comment_body, author=comment_author, commented_post=commented_post)

    return render(request, 'blog.html', context={
        'blog': blog
    })

@login_required(login_url='/accounts/login/')
def add_blog(request):
    form = Blogform()
    if request.method == 'POST':
        form = Blogform(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user

            form.save()
            return redirect('home')
        else:
            print(form.errors)

    return render(request, 'add_blog.html', {'form': form})


def delete_blog(request, id):
    blog = Blog.objects.get(id=id)

    def check_delete_permission():
        if request.user.has_perm('blog.delete_blog') and request.user.id == blog.author.id:
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False

    is_delete_allowed = check_delete_permission()

    if is_delete_allowed:
        blog.delete()
        return redirect('home')
    else:
        return HttpResponse("You don't have permission to delete this blog")


def edit_blog(request, id):
    blog = Blog.objects.get(id=id)
    form = Blogform(instance=blog)
    if request.method == 'POST':
        form = Blogform(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'update_post.html', context={'form': form, 'blog': blog})



# It was just a try.
from rest_framework.generics import ListAPIView

class BlogAPI(ListAPIView):
    throttle_classes = []
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class =serializers.BlogSerializer


    def get_queryset(self):

        if self.request.user.is_superuser:
            return Blog.objects.all()

        return Blog.objects.filter(author=self.request.user)

    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]

    ordering_fields = ['created_at']

    filterset_fields = ['id']

    search_fields = ['^title']





