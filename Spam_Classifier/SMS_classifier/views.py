
from django.shortcuts import render
import joblib

# Create your views here.

#home page of the website connects email and SMS
def home(request):
    return render(request, 'home.html')

# input page for SMS 
def SMSin(request):
    return render(request, 'SMSin.html')

# result page for SMS
def SMS(request):
    text = request.GET.get('sms','no message here')
    # print(text)
    inp = [text]
    clf = joblib.load('SMSmodel.sav')
    res = clf.predict(inp)
    if (res[0]==1):
        result = 'Spam'
    else:
        result = 'not Spam'
    parms = {
        'Prediction': result
    }
    return render(request, 'SMS.html', context=parms)

# input page for email
def emailin(request):
    return render(request, 'emailin.html')

# result page for email
def email(request):
    text = request.GET.get('email','no message here')
    # print(text)
    inp = [text]
    clf = joblib.load('Emailmodel.sav')
    res = clf.predict(inp)
    if (res[0]==1):
        result = 'Spam'
    else:
        result = 'not Spam'
    parms = {
        'Prediction': result
    }
    return render(request, 'email.html', context=parms) 