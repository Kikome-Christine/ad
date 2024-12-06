from django.shortcuts import render

# Create your views here.
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

@method_decorator(csrf_protect, name='dispatch')
class RegistrationView(View):
    def get(self, request):
        # Render registration form
        form = UserCreationForm()
        return render(request, 'registration_form.html', {'form': form})

    def post(self, request):
        # Process registration data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponse("Registration successful")
        return render(request, 'registration_form.html', {'form': form})
    


#     Explanation:
# CSRF Protection: The @method_decorator(csrf_protect, name='dispatch') line ensures that CSRF protection is applied to all HTTP methods of the view.
# User Creation Form: The UserCreationForm is used to handle user registration, ensuring that the input is validated.
# Redirect on Success: Upon successful registration, a simple success message is returned.

# b) Lines of Code for CSRF Protection
# The line of code that incorporates CSRF protection to all HTTP methods of the view is:
# python
# @method_decorator(csrf_protect, name='dispatch')

# This decorator ensures that CSRF protection is applied to both the get and post methods of the RegistrationView.
# c) Expected Output After Correction and Execution
# Once the above code is corrected and executed successfully, the expected output will be:
# On GET Request: When a user accesses the registration page (via a GET request), they will see a registration form rendered from registration_form.html.
# On POST Request: When the user submits the form with valid data:
# A new user will be created in the database.
# The response will be an HTTP response with the message: "Registration successful".
# If Invalid Data is Submitted: If the submitted data does not pass validation (e.g., username already exists), the same registration form will be rendered again with error messages displayed.
# This implementation provides a robust way to handle user registrations while ensuring security against CSRF attacks.

