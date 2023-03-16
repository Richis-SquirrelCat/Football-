from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['GET'])
def slider(request):
    s = News.objects.filter(banner=True).order_by('-id')[:2]
    ser = NewsSerializer(s, many=True)
    data = {
        "slider": ser.data
    }
    return Response(data)


@api_view(['GET'])
def media(request):
    m = Media.objects.all().order_by('-id')
    ser = MediaSerializer(m, many=True)
    return Response(ser.data)


@api_view(['GET'])
def news(request):
    n = News.objects.all().order_by('-id')[:12]
    ser = NewsSerializer(n, many=True)
    return Response(ser.data)


@api_view(['GET'])
def forma(request):
    f = FormView.objects.last()
    ser = FormViewSerializer(f)
    return Response(ser.data)


@api_view(['GET'])
def brand(request):
    b = Brand.objects.last()
    ser = BrandSerializer(b)
    return Response(ser.data)


@api_view(['GET'])
def statistica(request):
    st = Statistica.objects.order_by('-id')[:2]
    ser = StatisticaSerializer(st, many=True)
    return Response(ser.data)


@api_view(['GET'])
def participant(request):
    par = Participant.objects.all()
    ser = ParticipantSerializer(par, many=True)
    return Response(ser.data)


@api_view(['GET'])
def opinion(request):
    op = Opinion.objects.last()
    ser = OpinionSerializer(op)
    return Response(ser.data)


@api_view(["GET"])
def info_social(request):
    info = Info.objects.last()
    info_ser = InfoSerializer(info)
    s_media = SocialMedia.objects.all()
    s_media_ser = SocialMediaSerializer(s_media, many=True)
    data = {
        "info": info_ser.data,
        "social_media": s_media_ser.data
    }
    return Response(data)



