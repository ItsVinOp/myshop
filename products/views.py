from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Feedback
from django.contrib import messages
# from django.views import View

from .forms import FeedbackForm

# Create your views here.

# class IndexView(View):
#     def get(self, request):
#         user = "pouya"
#         products_numb = 7
#         products = Product.objects.all().order_by('id')[:4]
#         return render(request, "products/home.html",{
#         "name":user,
#         "product_numb": products_numb,
#         "products": products,
#         })
#     def post(self, request):
#         pass

def index(request):
    user = "pouya"
    products_numb = 7
    products = Product.objects.all().order_by('id')[:4]
    return render(request, "products/home.html",{
        "name":user,
        "product_numb": products_numb,
        "products": products,
    })

def signup(request):
    return render(request, "products/signup.html")

def product_cat(request, product):
    if product =="suits" or product=="dresses" or product=="shirts" or product=="shoes":
        return HttpResponse(f"Here is the list of our {product}.")
    else:
        return HttpResponse("The page you are looking for doesn't exist.")
    
# class ProductPageView(View):
#     def get(self, request, product,product_slug):
#         pass
#     def post(self, request, product,product_slug):


def product_page(request, product_brand, product_slug):
    product = Product.objects.get(slug = product_slug)
    form = FeedbackForm()
    reviews = Feedback.objects.filter(product=product)
    if request.method == "GET":
    
       return render(request,"products/product.html", {
          "product":product,
          "form": form,
          "reviews": reviews,
        })
    else:
        form=FeedbackForm(request.POST)
        reviews = Feedback.objects.filter(product=product)
        if form.is_valid():
            feedback = Feedback(
                name = form.cleaned_data["name"],
                rating = form.cleaned_data["rating"],
                product = product,
                text = form.cleaned_data["text"]
            )
            
            feedback.save() 
            messages.success(request, "Your feedback is submitted sucessfully")
            form = FeedbackForm()
    
        return render(request,"products/product.html", {
           "product":product,
           "form": form,
           "reviews": reviews,
        })  
