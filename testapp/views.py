# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from .models import Test
from .serializers import TestSerializer

class TestView(generics.ListCreateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
