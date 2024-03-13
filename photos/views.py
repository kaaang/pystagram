from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from django.shortcuts import get_object_or_404


def hello(request):
    return HttpResponse('hello!')


def detail(request, pk, hidden=False):
    if hidden is True:
        pass

    # try:
    #     photo = Photo.objects.get(pk=pk)
    # except Photo.DoesNotExist:
    #     return HttpResponse("사진이 없습니다.")

    photo = get_object_or_404(Photo, pk=pk)

    messages = (
        '<p>{pk}번 사진 보여줄게요</p>'.format(pk=photo.pk),
        '<p>주소는 {url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),
    )
    return HttpResponse('\n'.join(messages))
