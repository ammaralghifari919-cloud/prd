from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article, Category, HeroSlide, Partner, Product, SiteContent, Testimonial
from .serializers import (ArticleSerializer, CategorySerializer, HeroSlideSerializer,
                          PartnerSerializer, ProductSerializer, SiteContentSerializer,
                          TestimonialSerializer)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name', 'category__category_name']

    def get_queryset(self):
        qs = Product.objects.select_related('category').all()
        category = self.request.query_params.get('category')
        if category:
            qs = qs.filter(category__slug=category)
        favorite = self.request.query_params.get('favorite')
        if favorite:
            qs = qs.filter(is_favorite=True)
        return qs


class PartnerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PartnerSerializer

    def get_queryset(self):
        qs = Partner.objects.filter(status='active')
        partner_type = self.request.query_params.get('type')
        if partner_type in ('distributor', 'agen'):
            qs = qs.filter(type=partner_type)
        city = self.request.query_params.get('city')
        if city:
            qs = qs.filter(city__icontains=city)
        return qs


class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.filter(is_published=True)
    serializer_class = TestimonialSerializer


class HeroSlideViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HeroSlide.objects.filter(is_active=True)
    serializer_class = HeroSlideSerializer


class SiteContentView(APIView):
    def get(self, request):
        obj = SiteContent.objects.first()
        if obj is None:
            obj = SiteContent.objects.create()
        return Response(SiteContentSerializer(obj, context={'request': request}).data)


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.filter(published_at__isnull=False).order_by('-published_at')
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
