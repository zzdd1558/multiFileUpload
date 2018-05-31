from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from pprint import pprint
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('file')
            
            for image in images:
                print(image.name)
                print(type (image))
                path = default_storage.save(image.name , ContentFile(image.read()))
                print(path)

            return HttpResponse(str("성공적"))
    else:
        form = UploadFileForm()

    return HttpResponse(str("HELLO"))
