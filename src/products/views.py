from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id=1)
	context = {
		'title': obj.title,
		'description': obj.description,
	}
	return render(request,"product_detail.html", context) 
	# no need for path when present inside same folder

	# return render(request,"product/detail.html", context) 
	# the file in templates folder


from .forms import ProductForm
def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm() # rerender after save
	context = {
		'form': form,
	}
	return render(request,"product_create.html", context) 
