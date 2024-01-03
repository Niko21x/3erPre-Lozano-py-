
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'base.html')

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            website = 'http://mysite.com/profiles/' + str(user.id)
            Profile.objects.create(user=user, website=website)  # Use Profile, not ProfileForm
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from .models import Message
from django.contrib.auth import login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(request.user)
            print(request.session)

   
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



# App/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Message

from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    sent_messages = Message.objects.filter(sender=request.user)
    received_messages = Message.objects.filter(receiver=request.user)
    return render(request, 'profile.html', {'profile': profile, 'sent_messages': sent_messages, 'received_messages': received_messages})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    Profile.objects.get(user=request.user).delete()
    messages.success(request, 'Your profile was successfully deleted!')
    return redirect('home')



from .models import Message
from .forms import MessageForm

@login_required
def message_list(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'message_list.html', {'messages': messages})

from django.shortcuts import render, redirect
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            if 'receiver_id' in request.POST and request.POST['receiver_id']:
                try:
                    message.receiver = User.objects.get(id=request.POST['receiver_id'])
                except User.DoesNotExist:
                    messages.error(request, 'User does not exist')
                    return render(request, 'send_message.html', {'form': form})
            else:
                messages.error(request, 'Receiver ID is missing')
                return render(request, 'send_message.html', {'form': form})
            message.save()
            return redirect('profile')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})