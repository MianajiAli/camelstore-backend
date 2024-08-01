from django.views.generic import ListView
from .models import Message
class MessageView(ListView):
    model= Message
    template_name='home.html'