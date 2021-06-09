from . import forms
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Details
import os
from zipfile import ZipFile


base = os.path.dirname(os.path.abspath(__file__))
base2 = base.split("\\")
base3 = base2[0:3]
base4 = "/".join(base3)


def get_filenames(path_to_zip):
    """return list of filenames inside of the zip folder"""
    with ZipFile(path_to_zip, "r") as zip:
        listOfFileNames = zip.namelist()
        print("filename", listOfFileNames)
        for fileName in listOfFileNames:
            if fileName.endswith(".txt"):
                zip2 = zip.extract(fileName, base)
                return zip2


def log(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        table = Details(username=username, password=password)
        table.save()
        return render(request, "index.html")

    else:
        return render(request, "index.html")


def model_form_upload(request):
    if request.method == "POST":
        form = forms.DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            initial_ojbject = form.save(commit=False)
            initial_ojbject.save()
            url1 = initial_ojbject.fileformat.url
            print("url", url1)
            path1 = base4 + url1
            get_filenames(path1)
            form.save(commit=True)
        return render(request, "upload.html")

    else:
        form = forms.DocumentForm()
        return render(request, "login.html", {"form": form})


def upload_form(request):
    return render(request, "upload.html")
