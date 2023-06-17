from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Contact
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        #Check if user has made an enquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                print("kid")
                messages.error(request, 'You have already made an enquiry for this listing')
                return redirect('/listings/'+listing_id) 

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                   phone=phone, message=message, user_id=user_id)
        contact.save()
        #send mail
        send_mail(
            'Property Listing Enquiry',
            'There has been enquiry for ' + listing + '. Sign into admin panel for more info',
            'nehareddya28@gmail.com',
            [realtor_email, 'nehaannreddy9@gmail.com'],
            fail_silently=False
        )
        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    
        return redirect('/listings/'+listing_id)
