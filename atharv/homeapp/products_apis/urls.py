from django import forms
from django.shortcuts import render
from ..models import UserModelCustom


def getProducts(request):
    user = UserModelCustom.objects.get(id=1)
    context = {
        "user": user
    }
    return render(request, 'details.html', context)


def addUser(request):
    # entered_name = request.POST.get("full_name")
    # entered_age = request.POST.get("age")
    # UserModelCustom.objects.create(name=entered_name, age=entered_age)
    my_form = RawFormData()
    initial1 = {"name": "init name", "age": 99}
    if request.method == "POST":
        my_form = RawFormData(request.POST, initial=initial1)
        if my_form.is_valid():
            print("Valid data:", my_form.cleaned_data)
            UserModelCustom.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)

    context = {
        "form": my_form
    }

    return render(request, 'create_user.html', context)


def getUser(request, user_id):
    user = None
    try:
        user = UserModelCustom.objects.get(id=user_id)
    except:
        pass

    context = {
        'name': None,
        'age': None
    }

    if user:
        context = {
            'name': user.name,
            'age': user.age
        }

    return render(request, 'getSingleUser.html', context)


def deleteUser(request, user_id):
    user = None
    try:
        user = UserModelCustom.objects.get(id=user_id)
    except:
        pass

    message = {
        'result': 'User deleted successfully!',
        'status': 1
    }

    if user:
        user.delete()
    else:
        message = {
            'result': 'User does not exist!',
            'status': 0
        }
    return render(request, 'deletedUserPage.html', message)


def getAllUsers(request):
    queryset = UserModelCustom.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'allUsersList.html', context)


class RawFormData(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
