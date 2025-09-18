# orders/views.py

import stripe
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

stripe.api_key = settings.STRIPE_SECRET_KEY


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # saves the Order, but do not save the items yet
            order = form.save()

            # add the OrderItems to the order/separating the database logic cleanly
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            # order is saved, preparing for Stripe
            line_items = []
            for item in cart:
                line_items.append({
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(item['price'] * 100),
                        'product_data': {
                            'name': item['product'].name,
                        },
                    },
                    'quantity': item['quantity'],
                })

            try:
                # the Stripe Checkout Session
                success_url = request.build_absolute_uri(reverse('orders:payment_success'))
                cancel_url = request.build_absolute_uri(reverse('orders:payment_canceled'))

                session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=line_items,
                    mode='payment',
                    success_url=success_url,
                    cancel_url=cancel_url,
                    # local order ID in Stripe's metadata stored
                    metadata={
                        'order_id': order.id
                    }
                )

                cart.clear()
                return redirect(session.url, code=303)

            except Exception as e:
                # if Stripe fails
                order.delete()
                return render(request, 'orders/payment/canceled.html')
    else:
        form = OrderCreateForm()

    return render(request, 'orders/create.html', {'cart': cart, 'form': form})


def payment_success(request):
    return render(request, 'orders/payment/success.html')

def payment_canceled(request):
    return render(request, 'orders/payment/canceled.html')