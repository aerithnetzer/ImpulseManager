from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from .models import Page
import base64

S3_BUCKET = "nu-impulse-production"

def extract_html(node):
    results = []
    if isinstance(node, dict):
        if "html" in node and node["html"]:
            results.append(node["html"])
        for value in node.values():
            results.extend(extract_html(value))
    elif isinstance(node, list):
        for item in node:
            results.extend(extract_html(item))
    return results

def index(request: HttpRequest):
    pages = Page.objects.filter(JPG__isnull=False)[:10]
    pages_with_images = []
    for page in pages:
        jpg_b64 = base64.b64encode(bytes(page.JPG)).decode("utf-8") if page.JPG else None
        html_parts = extract_html(page.children) if page.children else []
        pages_with_images.append({
            "page": page,
            "jpg_b64": jpg_b64,
            "html_parts": html_parts,
        })
    ctx = {"pages": pages_with_images}
    return render(request, "JobViewer/pages.html", ctx)
