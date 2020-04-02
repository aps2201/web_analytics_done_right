from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
def index(request):
    return render(request,
                  'service/home.html',
                  {'page':'service',
                   'products':product.objects.all(),})
def detail(request,item_id):
    return render(request,
                  'service/product_page.html',
                  {'page':'service',
                   'products':product.objects.get(product_id=item_id),})


# cart functions
@login_required()
def add_to_cart(request,**kwargs):
    user_cart =  get_object_or_404(cart,user=request.user)
    product = product.objects.filter(id=kwargs.get('item_id','')).first()
    if product in request.user.cart.items.all():
        messages.info(request, 'You already have this item')
        return redirect(reverse('service:home'))
    order_item, status = orderItem.objects.get_or_create(product=product)
    user_order, status = order.objects.get_or_create(owner=cart, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()
    messages.info(request, "item added to cart")
    return redirect(reverse('products:home'))
        



#@login_required()
#def delete_from_cart(request,item_id):
    
