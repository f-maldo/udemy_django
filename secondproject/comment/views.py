from django.shortcuts import render, redirect, get_object_or_404
from .models import Comment, Contact
from .forms import CommentForm, ContactForm
from django.contrib import messages


# Create your views here.
def index(request):
    comments = Comment.objects.all()

    return render(request, 'index.html', {'comments': comments})


def add(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment:index')
    else:
        form = CommentForm()
    return render(request, 'add.html', {'form': form})


def update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comment:update', pk=comment.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'update.html', {'form': form, 'comment': comment})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = Contact()
            contact.name = form.cleaned_data['name']
            contact.last_name = form.cleaned_data['last_name']
            contact.email = form.cleaned_data['email']
            contact.phone = form.cleaned_data['phone']
            contact.birth_date = form.cleaned_data['birth_date']
            contact.type_contact = form.cleaned_data['type_contact']
            if 'document' in request.FILES:
                contact.document = request.FILES['document']
            contact.save()
            messages.add_message(request, messages.INFO, 'Form was received')
            return redirect('comment:contact')
        else:
            pass
    else:
        form = ContactForm
    return render(request, 'contact.html', {"form": form})
