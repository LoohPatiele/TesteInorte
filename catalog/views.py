# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Product, Category

class ProductListView(generic.ListView):
    
    model = Product
    template_name = 'catalog/product_list.html'
    paginate_by = 9


product_list= ProductListView.as_view()


class CategoryListView(generic.ListView):
    
    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kargs):
        context = super(CategoryListView, self).get_context_data( **kargs )
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


category = CategoryListView.as_view()


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
    }
    return render(request,'catalog/product.html', context)