from django.shortcuts import render, redirect
from .models import GuestbookEntry
from .forms import GuestbookEntryForm

# Create your views here.


def home_view(request):
    if request.method == 'POST':
        if 'view_posts' in request.POST:
            return redirect('guestbook')
        elif 'add_post' in request.POST:
            return redirect('add_guestbook_entry')
    return render(request, 'guestbook/home_view.html')


def add_guestbook_entry(request):
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook')
    else:
        form = GuestbookEntryForm()
    return render(request, 'guestbook/add_guestbook_entry.html', {'form': form})


def guestbook_view(request):
    entries = GuestbookEntry.objects.all()
    return render(request, 'guestbook/guestbook.html', {'entries': entries})
