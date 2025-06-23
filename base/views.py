from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages as django_messages
from django.db import connection  # Add this import
from items.models import Item 
from conversation.models import Conversation 
from .forms import MessageForm
from .models import Message

def base(request):
    User = get_user_model()
    
    # Initialize counts with safe defaults
    counts = {
        'users_count': 0,
        'active_users_count': 0,
        'items_count': 0,
        'conversations_count': 0
    }

    try:
        # Check if tables exist before querying
        table_names = connection.introspection.table_names()
        
        if 'users_customuser' in table_names:
            counts['users_count'] = User.objects.count()
            counts['active_users_count'] = User.objects.filter(is_active=True).count()
            
        if 'items_item' in table_names:
            counts['items_count'] = Item.objects.count()
            
        if 'conversation_conversation' in table_names:
            counts['conversations_count'] = Conversation.objects.count()

    except Exception as e:
        # Log error if needed
        pass

    # Message form handling
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            Message.objects.create(
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            django_messages.success(request, 'Message sent successfully!')
            return redirect('base:index')
    else:
        form = MessageForm()

    # Add counts to context
    context = {
        **counts,
        'form': form
    }
    return render(request, 'base/index.html', context)

def message_list(request):
    try:
        all_messages = Message.objects.all().order_by('-created_at')
    except:
        all_messages = []
    return render(request, 'base/messages.html', {'messages': all_messages})
def admin_links(request):
    return render(request, 'base/admin_links.html')

def about_us(request):
    return render(request, 'base/about_us.html')