from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash # to make sure user is still logged in after password change
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib import messages

from homepage.forms import RegistrationForm, EditProfileForm
from homepage.models import Bookmark
from schedule.models import SchedulePost
from django.db.models import Q


def search(request):

    template = 'homepage/search.html'

    query = request.GET.get('q')

    if query:
     results = SchedulePost.objects.filter(Q(title__icontains=query) | Q(faculty__icontains=query) | Q(desc__icontains=query))
    else:
     results = SchedulePost.objects.all()
   
    args = {
            'results': results, 
        } 
    
    return render(request, template, args)


# Create your views here.
def index(request):
    return render(request, 'homepage/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid: #all the fields are validated
            form.save() #creates user and save data in database
            return redirect('/register/complete')

    else: #requesting for the blank form to fill in
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'homepage/reg_form.html', args)

def register_complete(request):
    return render(request, 'homepage/reg_done.html')

@login_required
def view_profile(request):
    user = get_user_model().objects.get(id=request.user.id) 
    args = {'user': user}
    return render(request, 'homepage/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'homepage/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
        else:
            return redirect('/profile/change_password')
    
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'homepage/change_password.html', args)

def view_other_profile(request, id):
    user = get_user_model().objects.get(id=id)
    if user == request.user:
        return redirect('view_profile')
    else:
        return render(request, 'homepage/view_other_profile.html', {'user':user})

def view_uploaded_schedules(request, id):
    user = get_user_model().objects.get(id=id)
    schedule_view = ListView.as_view(queryset=SchedulePost.objects.filter(user=user).order_by('-created'), template_name='homepage/view_uploaded_schedules.html')(request)
    return schedule_view

@login_required
def view_bookmarked_schedules(request):
    user = get_user_model().objects.get(id=request.user.id) 
    if Bookmark.objects.filter(user=user).exists():
        user_bookmark = Bookmark.objects.get(user=user)
    else:
        new_user_bookmark, created = Bookmark.objects.get_or_create(user=request.user)
        user_bookmark = Bookmark.objects.get(user=user)

    bookmarks = user_bookmark.bookmarks.all()

    args = {'bookmarks': bookmarks}
    return render(request, 'homepage/view_bookmarked_schedules.html', args)
