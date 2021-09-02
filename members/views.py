from members.models import Profile
from Photo.models import Photo
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request,pk):
    user = User.objects.get(id=pk)
    photos = Photo.objects.filter(id=pk)
    return render(request, 'registration/profile.html', {'user':user, 'photos':photos})
     
class UpdateProfilePicture(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'registration/update_profile.html'
    fields = ['image', 'bio']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False

    success_url = '/'
