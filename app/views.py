from django.shortcuts import render,HttpResponse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time
import threading
from django.db import transaction




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
    # 3.running in same db  transaction and the transaction is rolled back, the signal will not be processed.
    with transaction.atomic():
        User.objects.create(username='test_user')
        raise Exception("Forcing rollback")
except Exception as e:
    print("Error creating user:", str(e))
print("After User creation.")
print("After transaction block.")


# 4.   An instance of the Rectangle class requires length:int and width:int to be initialized.
# We can iterate over an instance of the Rectangle class.
# When an instance is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {'width': <VALUE_OF_WIDTH>}.


class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rect = Rectangle(5, 3)
for attribute in rect:
    print(attribute)
