from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class PaginationMixin:
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page_number = self.request.GET.get('page')

        if self.paginate_by <= 0:
            self.paginate_by = 1
        
        paginator = Paginator(self.get_queryset(), self.paginate_by)

        try:
            context['page_obj'] = paginator.page(page_number)
        except PageNotAnInteger:
            context['page_obj'] = paginator.page(1)
        except EmptyPage:
            context['page_obj'] = paginator.page(paginator.num_pages)

        context['paginator'] = paginator
        context['is_paginated'] = True

        return context



class CacheMixixn:
    cache_timeout = 60

    @method_decorator(cache_page(cache_timeout))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
