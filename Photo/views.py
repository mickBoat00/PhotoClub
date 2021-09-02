from django.core import paginator
from django.views.generic.edit import DeleteView
from Photo.models import Category
from django.shortcuts import redirect, render
from .models import Category, Comment,Photo
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator


# Create your views here.
def gallery(request):
    category = request.GET.get('category')

    if category == None:
        photos = Photo.objects.all().order_by('-created')
    else:
        photos = Photo.objects.filter(category__name=category).order_by('-created')


    categories = Category.objects.all()
     
    p = Paginator(Photo.objects.all().order_by('-created'), 8)
    page = request.GET.get('page')
    photoPaginator = p.get_page(page)

    context = {
        'categories': categories,
        'photos': photos,
        'photoPaginator': photoPaginator
    }
    return render(request, 'Photo/gallery.html', context)

class PhotoList(ListView):
    model = Photo
    template_name = 'Photo/gallery.html'
    context_object_name = 'photos'
    ordering = ['-created']
    paginate_by = 8


class ViewPic(LoginRequiredMixin, DetailView):
    model = Photo
    template_name = 'Photo/view_pic.html'
    


class AddPicture(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'Photo/add_pic.html'
    fields = ['category', 'image', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdatePicture(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo
    template_name = 'Photo/update_pic.html'
    fields = ['category', 'image', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        photo = self.get_object()
        if self.request.user == photo.user:
            return True
        return False

class DeletePicture(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    template_name = 'Photo/delete_pic.html'

    def test_func(self):
        photo = self.get_object()
        if self.request.user == photo.user:
            return True
        return False

    success_url = '/'

class AddComment(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'Photo/add_comment.html'
    fields = ['comment_body']
    
    success_url = reverse_lazy('gallery')

    def form_valid(self, form):
        form.instance.photo_id = self.kwargs['pk']
        form.instance.commenter_name = self.request.user
        return super().form_valid(form)

class EditComment(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'Photo/update_comment.html'
    fields = ['comment_body']
    success_url = reverse_lazy('gallery')

    def form_valid(self, form):
        form.instance.photo_id = self.kwargs['pk']
        form.instance.commenter_name = self.request.user
        return super().form_valid(form)

def search_category(request):
    if request.method == "POST":
        searched = request.POST['searched']

        categories = Category.objects.filter(name__contains=searched)
        
        photos = Photo.objects.filter(description__contains=searched)

        context = {
            'searched':searched,
            'categories': categories, 
            'photos':photos,
            }

        return render(request, 'Photo/search_category.html', context)
    else:
        return render(request, 'Photo/search_category.html')
    