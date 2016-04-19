#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from cStringIO import StringIO


def qrcode_gene(request, data):
    img = qrcode.make(data)

    buf = StringIO()
    img.save(buf)
    img_stream = buf.getvalue()

    response = HttpResponse(img_stream, content_type="image/png")
    response['Last-Modified'] = 'Sun, 17 Apr 2016 02:05:03 GMT'
    response['Cache-Control'] = 'max-age=31536000'
    return response

# Create your views here..
