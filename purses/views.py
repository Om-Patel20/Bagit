from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse
import json
from .models import Purse, Order


class PursesListView(ListView):
    model = Purse
    template_name = 'list.html'


class PursesDetailView(DetailView):
    model = Purse
    template_name = 'detail.html'


class SearchResultsListView(ListView):
	model = Purse
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Purse.objects.filter(
		Q(name__icontains=query) | Q(brand=query) | Q(description=query)
		)

class PurseCheckoutView(LoginRequiredMixin, DetailView):
    model = Purse
    template_name = 'checkout.html'
    login_url     = 'login'


def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Purse.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
	)
	return JsonResponse('Payment completed!', safe=False)