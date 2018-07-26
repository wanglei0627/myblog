#!/usr/bin/env python3
from django.shortcuts import render_to_response


def home(request):
    context = {}
    return render_to_response("index.html", context)
