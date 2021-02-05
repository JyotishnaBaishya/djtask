from django.shortcuts import render
from .forms import Search
from .util import start
from .models import UrlModel
import json, requests

def frequency(request):
	context = {
		'form': Search
	}
	return render(request, 'frequency.html', context)
def result(request):
	if request.method == "POST":
		form = Search(request.POST or None)
		if form.is_valid():
			data= form.cleaned_data.get("Url_search")
			if not UrlModel.objects.filter(url=data).exists():
				ans=start(data)
				U_in=UrlModel.objects.create(url=data, json=json.dumps(ans))
				context = {'data': ans, 'msg':"Data newly inserted"}
				return render(request, 'results.html', context)
			else:
				obj_all=UrlModel.objects.get(url=data)
				context = {'data': json.loads(obj_all.json), 'msg':"Data from database"}
				return render(request, 'results.html', context)
