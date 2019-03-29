from django.shortcuts import render
from .models import ContactData
from .form import Contactform
def contactview(request):
    if request.method=="POST":
        cform=ContactData(request.POST)
        if cform.is_vaild():
            first_name =  request.post.get('first_name', '')
            last_name= request.post.get('last_name', '')
            salary = request.post.get('salary', '')
            location = request.post.get('location', '')
            mobile = request.post.get('mobile', '')
            data=ContactData(
                first_name=first_name,
                last_name=last_name,
                salary=salary,
                location=location,
                mobile=mobile

            )
            data.save()
            cform = Contactform()
            return render(request, 'contact.html', {'cform': cform})

    else:
            cform=Contactform()
            return render(request,'contact.html',{'cform':cform})
