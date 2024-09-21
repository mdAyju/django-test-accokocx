from django.shortcuts import render,HttpResponse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time
import threading



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Question 1: By default, are Django signals executed synchronously or asynchronously?
@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    print("Signal received.")
    time.sleep(5)  # Sleep to simulate time-consuming task
    print("Signal finished processing.")

# 2.Do Django signals run in the same thread as the caller?
# Yes, by default, Django signals run in the same thread as the caller, which means that signal handling occurs in the main thread unless explicitly offloaded to another thread.
    print(f"Signal received in thread: {threading.current_thread().name}")
    
# # Creating a new user will trigger the signal
try:
# Creating a user and observing the thread
    print(f"Main thread: {threading.current_thread().name}")
    User.objects.create(username='test_user')
    User.objects.create(username='test_user')
except Exception as e:
    print("Error creating user:", str(e))
print("After User creation.")

