from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from paper.models import Note
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404


@login_required
def home(request):
    username = request.user.username
    note = Note.objects.filter(user=request.user)
    context = {'username': username, 'notes': note}
    return render(request, 'paper/home.html', context)

def create_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        user = request.user
        Note.objects.create(user=user, title=title, content=content)
        return redirect('paper:home')
    return render(request, 'paper/create_note.html')

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect('paper:home')

def view_note(request, note_id):
    note = Note.objects.get(id=note_id)
    context = {'notes': note}
    return render(request, 'paper/view_note.html', context)

@login_required
def update_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('paper:home')
    context = {'notes': note}
    return render(request, 'paper/view_note.html', context)

@login_required
def settings(request):
    return render(request, 'paper/settings.html')