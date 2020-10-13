from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
import string
import pyshorteners
from .models import *
from django.core.mail import EmailMessage
from django.utils.encoding import *
from django.utils.http import *
from django.contrib.sites.shortcuts import *
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import *

# Create your views here.
def home(request):
    return render(request, './url/home.html')

def aa(request,slug):
    try:
        code = Shorturl.objects.filter(uni_key = slug)
        finalop = code[0].ori_url
        return redirect(finalop)
    except:
        print("Error")
        return redirect('home')
    # return render(request, './url/home.html')


def get(request):
    # URL Validation
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


    # POST
    if request.method=='POST':
        link = request.POST['link']
        label = request.POST['label']
        ans = re.match(regex, link) is not None
        if(ans==True):
            longurl = Shorturl.objects.filter(ori_url=link)
            if(longurl):
                print("Already Exists")
                context = {'posts' : longurl}
            else:

                # creating random string
                letters = string.ascii_letters
                shorturl = Shorturl.objects.filter(short_url=link)
                result_str = ''.join(random.choice(letters) for i in range(random.randint(5,10)))
                ans11=False
                ans1 = Shorturl.objects.filter(uni_key=result_str)

                # Checking for same pattern. And if same pattern already exists then again again take random string and match until we get unique pattern
                while(ans11==False):
                    if(ans1):
                        print('This is same as done')
                        result_str = ''.join(random.choice(letters) for i in range(random.randint(6,10)))
                        if(not(Shorturl.objects.filter(uni_key=result_str))):
                            ans1=False
                    else:
                        ans1=not(ans1)
                        ans11=True

                # creating domain
                domain = get_current_site(request).domain
                short = 'http://'+domain+"/"+result_str
                # print(reset_password_url)



            #    saving it to database 
                x = [short]
                newUrl=x[0]
                contact = Shorturl(ori_url=link, short_url=newUrl,uni_key=result_str,label=label)
                contact.save()
                xx=Shorturl.objects.filter(short_url=short)
                context = {'posts' : xx}
                print(context)
        else:
            url = ['You have entered wrong email id. Please Check the URL that you have provided']
            context = {'q' : url}
    return render(request,'./url/home.html', context)


def showAll(request):
    all_Object = Shorturl.objects.all()
    context = {'all' : all_Object}
    return render(request,'./url/allUrls.html', context)
