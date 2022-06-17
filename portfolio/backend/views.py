from django.http import HttpResponse
import json
from . import models

# Create your views here.
def getProjects(request):
    projects = models.Project.objects.values("title", "subtitle", "content", "url", "imgUrl", "bgUrl", "imgAlt")
    data = json.dumps(list(projects))
    
    return HttpResponse(data, content_type="application/json")