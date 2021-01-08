from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import UserProfileForm
import json
from stats.models import Stat


def instructions(request):
    return render(request, 'pages/instructions.html')

def avgTypingData(typingdata):
    typingdatakeys = list(typingdata.keys())

    for x in range(len(typingdatakeys)):
        key = typingdatakeys[x]
        if (isinstance(typingdata[key], str)):
            dataValues = typingdata[key].split(",")
            totalNumber = 0
            for y in range(len(dataValues)):
                totalNumber += int(dataValues[y])
                typingdata[key] = round(totalNumber / len(dataValues), 1)

    return(typingdata)

def scoreTypingData(newtypingdata, savedtypingdata, min, max):
    newtypingdatakeys = list(newtypingdata.keys()) 
    numOfAccepted = 0
    numOfTotal = 0
    for x in range(len(newtypingdatakeys)):
        key = newtypingdatakeys[x]
        if (key in savedtypingdata):
            numOfTotal += 1
            if (newtypingdata[key] / savedtypingdata[key] > min and newtypingdata[key] / savedtypingdata[key] < max):
                numOfAccepted += 1
    return round((numOfAccepted / numOfTotal * 50), 2)


def evalTypingData(user, dwelldata, flightdata):
    dwelldata = json.loads(dwelldata)
    flightdata = json.loads(flightdata)

    newdwelldata = avgTypingData(dwelldata)
    newflightdata = avgTypingData(flightdata)
    saveddwelldata = avgTypingData(user.userprofile.dwelldata)
    savedflightdata = avgTypingData(user.userprofile.flightdata)

    return scoreTypingData(newdwelldata, saveddwelldata, 0.8, 1.2) + scoreTypingData(newflightdata, savedflightdata, 0.5, 1.5)

def updateNumStats(userScore, supposedToBeAccepted):
    stats = Stat.objects.get(testNum = 'Test 1')
    stats.numOfAttemptedLogins += 1
    if userScore >= 65:
        stats.numOfAcceptedLogins += 1

        percentsWhenAccepted = json.loads(stats.percentsWhenAccepted)
        percentsWhenAccepted.append(round(userScore, 2))
        percentsWhenAccepted = json.dumps(percentsWhenAccepted)
        stats.percentsWhenAccepted = percentsWhenAccepted

        if supposedToBeAccepted:
            stats.numOfAcceptedLoginsCorrect += 1

            percentsWhenAcceptedCorrect = json.loads(stats.percentsWhenAcceptedCorrect)
            percentsWhenAcceptedCorrect.append(round(userScore, 2))
            percentsWhenAcceptedCorrect = json.dumps(percentsWhenAcceptedCorrect)
            stats.percentsWhenAcceptedCorrect = percentsWhenAcceptedCorrect

        else:
            stats.numOfAcceptedLoginsIncorrect += 1

            percentsWhenAcceptedIncorrect = json.loads(stats.percentsWhenAcceptedIncorrect)
            percentsWhenAcceptedIncorrect.append(round(userScore, 2))
            percentsWhenAcceptedIncorrect = json.dumps(percentsWhenAcceptedIncorrect)
            stats.percentsWhenAcceptedIncorrect = percentsWhenAcceptedIncorrect
    else: 
        stats.numOfDeniedLogins += 1

        percentsWhenDenied = json.loads(stats.percentsWhenDenied) 
        percentsWhenDenied.append(round(userScore, 2))
        percentsWhenDenied = json.dumps(percentsWhenDenied)
        stats.percentsWhenDenied = percentsWhenDenied
        if not supposedToBeAccepted:
            stats.numOfDeniedLoginsCorrect += 1

            percentsWhenDeniedCorrect = json.loads(stats.percentsWhenDeniedCorrect)
            percentsWhenDeniedCorrect.append(round(userScore, 2))
            percentsWhenDeniedCorrect = json.dumps(percentsWhenDeniedCorrect)
            stats.percentsWhenDeniedCorrect = percentsWhenDeniedCorrect
        else:
            stats.numOfDeniedLoginsIncorrect += 1

            percentsWhenDeniedIncorrect = json.loads(stats.percentsWhenDeniedIncorrect)
            percentsWhenDeniedIncorrect.append(round(userScore, 2))
            percentsWhenDeniedIncorrect = json.dumps(percentsWhenDeniedIncorrect)
            stats.percentsWhenDeniedIncorrect = percentsWhenDeniedIncorrect
    stats.save()

# def login(request, supposedToBeAccepted):
#     username = request.POST['username']
#     password = request.POST['password']

#     dwelldata = request.POST['dwelldata']
#     flightdata = request.POST['flightdata']

#     user = auth.authenticate(username=username, password=password)

#     if user is not None:
#         userScore = evalTypingData(user, dwelldata, flightdata)

#         updateNumStats(userScore, False)


#         auth.login(request, user)
#         return redirect('test2')
#     else:
#         messages.error(request, 'This Account Does Not Exist')
#         return redirect('test1error')

def test1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        dwelldata = request.POST['dwelldata']
        flightdata = request.POST['flightdata']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            userScore = evalTypingData(user, dwelldata, flightdata)

            updateNumStats(userScore, False)


            auth.login(request, user)
            return redirect('test2')
        else:
            messages.error(request, 'This Account Does Not Exist')
            return redirect('test1error')   
    else:
        return render(request, 'pages/test1.html')

def test1error(request):
    return render(request, 'pages/test1.html')


def test2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        dwelldata = request.POST['dwelldata']
        flightdata = request.POST['flightdata']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            userScore = evalTypingData(user, dwelldata, flightdata)

            updateNumStats(userScore, False)


            auth.login(request, user)
            return redirect('test3')
        else:
            messages.error(request, 'This Account Does Not Exist')
            return redirect('test2')
    else:
        return render(request, 'pages/test1.html')


def test3(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        dwelldata = request.POST['dwelldata']
        flightdata = request.POST['flightdata']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            userScore = evalTypingData(user, dwelldata, flightdata)

            updateNumStats(userScore, False)


            auth.login(request, user)
            return redirect('test4')
        else:
            messages.error(request, 'This Account Does Not Exist')
            return redirect('test3')
    else:
        return render(request, 'pages/test1.html')


def test4(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        dwelldata = request.POST['dwelldata']
        flightdata = request.POST['flightdata']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            userScore = evalTypingData(user, dwelldata, flightdata)

            updateNumStats(userScore, False)


            auth.login(request, user)
            return redirect('test5')
        else:
            messages.error(request, 'This Account Does Not Exist')
            return redirect('test4')
    else:
        return render(request, 'pages/test1.html')


def test5(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        dwelldata = request.POST['dwelldata']
        flightdata = request.POST['flightdata']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            userScore = evalTypingData(user, dwelldata, flightdata)

            updateNumStats(userScore, False)


            auth.login(request, user)
            return redirect('test6')
        else:
            messages.error(request, 'This Account Does Not Exist')
            return redirect('test5')
    else:
        return render(request, 'pages/test1.html')


def test6(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        dwelldata = request.POST['dwelldata']
        flightdata = request.POST['flightdata']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            userScore = evalTypingData(user, dwelldata, flightdata)

            updateNumStats(userScore, False)


            auth.login(request, user)
            return redirect('register')
        else:
            messages.error(request, 'This Account Does Not Exist')
            return redirect('test6')
    else:
        return render(request, 'pages/test1.html')


def register(request):
    if request.method == 'POST':

        profile_form = UserProfileForm(request.POST)

        # Get form values
        username1 = request.POST['username-1']
        password1 = request.POST['password-1']
        username2 = request.POST['username-2']
        password2 = request.POST['password-2']
        username3 = request.POST['username-3']
        password3 = request.POST['password-3']
        username4 = request.POST['username-4']
        password4 = request.POST['password-4']
        username5 = request.POST['username-5']
        password5 = request.POST['password-5']
        username6 = request.POST['username-6']
        password6 = request.POST['password-6']
        username7 = request.POST['username-7']
        password7 = request.POST['password-7']
        username8 = request.POST['username-8']
        password8 = request.POST['password-8']
        username9 = request.POST['username-9']
        password9 = request.POST['password-9']

        dwelldata = request.POST['dwelldata']
        flightdata = request.POST['flightdata']

        # Check if usernames and passwords match
        if username1 == username2 and username2 == username3 and username3 == username4 and username4 == username5 and username5 == username6 and username6 == username7 and username7 == username8 and username8 == username9:
            if password1 == password2 and password2 == password3 and password3 == password4 and password4 == password5 and password5 == password6 and password6 == password7 and password7 == password8 and password8 == password9:
                if User.objects.filter(username=username1).exists():
                    messages.error(request, 'That Username Is Already Taken')
                    return redirect('register')
                else:
                    #Looks good 
                    user = User.objects.create_user(username=username1, password=password1)

                    profile = profile_form.save(commit=False)
                    profile.user = user

                    profile.save()

                    dwelldata = avgTypingData(json.loads(dwelldata))
                    flightdata = avgTypingData(json.loads(flightdata))
                    stats = Stat.objects.get(testNum = 'Test 1')

                    if "69" in dwelldata:
                        dwelldataForKeyE = json.loads(stats.dwelldataForKeyE)
                        dwelldataForKeyE.append(dwelldata["69"])
                        dwelldataForKeyE = json.dumps(dwelldataForKeyE)
                        stats.dwelldataForKeyE = dwelldataForKeyE

                    if "65" in dwelldata:
                        dwelldataForKeyA = json.loads(stats.dwelldataForKeyA)
                        dwelldataForKeyA.append(dwelldata["65"])
                        dwelldataForKeyA = json.dumps(dwelldataForKeyA)
                        stats.dwelldataForKeyA = dwelldataForKeyA

                    if "82" in dwelldata:
                        dwelldataForKeyR = json.loads(stats.dwelldataForKeyR)
                        dwelldataForKeyR.append(dwelldata["82"])
                        dwelldataForKeyR = json.dumps(dwelldataForKeyR)
                        stats.dwelldataForKeyR = dwelldataForKeyR

                    if "73" in dwelldata:
                        dwelldataForKeyI = json.loads(stats.dwelldataForKeyI)
                        dwelldataForKeyI.append(dwelldata["73"])
                        dwelldataForKeyI = json.dumps(dwelldataForKeyI)
                        stats.dwelldataForKeyI = dwelldataForKeyI

                    if "79" in dwelldata:
                        dwelldataForKeyO = json.loads(stats.dwelldataForKeyO)
                        dwelldataForKeyO.append(dwelldata["79"])
                        dwelldataForKeyO = json.dumps(dwelldataForKeyO)
                        stats.dwelldataForKeyO = dwelldataForKeyO

                    if "84-72" in flightdata:
                        flightdataForKeysTH = json.loads(stats.flightdataForKeysTH)
                        flightdataForKeysTH.append(flightdata["84-72"])
                        flightdataForKeysTH = json.dumps(flightdataForKeysTH)
                        stats.flightdataForKeysTH = flightdataForKeysTH

                    if "72-69" in flightdata:
                        flightdataForKeysHE = json.loads(stats.flightdataForKeysHE)
                        flightdataForKeysHE.append(flightdata["72-69"])
                        flightdataForKeysHE = json.dumps(flightdataForKeysHE)
                        stats.flightdataForKeysHE = flightdataForKeysHE

                    if "65-78" in flightdata:
                        flightdataForKeysAN = json.loads(stats.flightdataForKeysAN)
                        flightdataForKeysAN.append(flightdata["65-78"])
                        flightdataForKeysAN = json.dumps(flightdataForKeysAN)
                        stats.flightdataForKeysAN = flightdataForKeysAN

                    if "73-78" in flightdata:
                        flightdataForKeysIN = json.loads(stats.flightdataForKeysIN)
                        flightdataForKeysIN.append(flightdata["73-78"])
                        flightdataForKeysIN = json.dumps(flightdataForKeysIN)
                        stats.flightdataForKeysIN = flightdataForKeysIN

                    if "69-82" in flightdata:
                        flightdataForKeysER = json.loads(stats.flightdataForKeysER)
                        flightdataForKeysER.append(flightdata["69-82"])
                        flightdataForKeysER = json.dumps(flightdataForKeysER)
                        stats.flightdataForKeysER = flightdataForKeysER

                    stats.save()


                    # Login after register
                    auth.login(request,user)
                    messages.success(request, 'You Have Successfully Registered')
                    return redirect('selftest1')
            else: messages.error(request, 'Passwords Do Not Match')
            return redirect('register')

        else: messages.error(request, 'Usernames Do Not Match')
        return redirect('register')
    else: 
        profile_form = UserProfileForm()
    
    context = {'profile_form' : profile_form}
    return render(request, 'pages/register.html')


def selftest1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        dwelldata = request.POST['dwelldata']
        flightdata = request.POST['flightdata']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            userScore = evalTypingData(user, dwelldata, flightdata)

            updateNumStats(userScore, True)


            auth.login(request, user)
            return redirect('selftest2')
        else:
            messages.error(request, 'This Account Does Not Exist')
            return redirect('selftest1')
    else:
        return render(request, 'pages/selftest1.html')

def selftest2(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        dwelldata = request.POST['dwelldata']
        flightdata = request.POST['flightdata']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            userScore = evalTypingData(user, dwelldata, flightdata)

            updateNumStats(userScore, True)


            auth.login(request, user)
            return redirect('selftest3')
        else:
            messages.error(request, 'This Account Does Not Exist')
            return redirect('selftest2')
    else:
        return render(request, 'pages/selftest1.html')

def selftest3(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        dwelldata = request.POST['dwelldata']
        flightdata = request.POST['flightdata']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            userScore = evalTypingData(user, dwelldata, flightdata)

            updateNumStats(userScore, True)


            auth.login(request, user)
            return redirect('selftest4')
        else:
            messages.error(request, 'This Account Does Not Exist')
            return redirect('selftest3')
    else:
        return render(request, 'pages/selftest1.html')

def selftest4(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        dwelldata = request.POST['dwelldata']
        flightdata = request.POST['flightdata']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            userScore = evalTypingData(user, dwelldata, flightdata)

            updateNumStats(userScore, True)


            auth.login(request, user)
            return redirect('selftest5')
        else:
            messages.error(request, 'This Account Does Not Exist')
            return redirect('selftest4')
    else:
        return render(request, 'pages/selftest1.html')

def selftest5(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        dwelldata = request.POST['dwelldata']
        flightdata = request.POST['flightdata']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            userScore = evalTypingData(user, dwelldata, flightdata)

            updateNumStats(userScore, True)


            auth.login(request, user)
            return redirect('selftest6')
        else:
            messages.error(request, 'This Account Does Not Exist')
            return redirect('selftest5')
    else:
        return render(request, 'pages/selftest1.html')

def selftest6(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        dwelldata = request.POST['dwelldata']
        flightdata = request.POST['flightdata']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            userScore = evalTypingData(user, dwelldata, flightdata)

            updateNumStats(userScore, True)


            auth.login(request, user)
            return redirect('completed')
        else:
            messages.error(request, 'This Account Does Not Exist')
            return redirect('selftest6')
    else:
        return render(request, 'pages/selftest1.html')


def completed(request):
    return render(request, 'pages/completed.html')

def consentinstructions(request):
    return render(request, 'pages/consentinstructions.html')