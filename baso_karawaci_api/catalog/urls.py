from rest_framework.routers import DefaultRouter

from .views import (ArticleViewSet, CategoryViewSet, HeroSlideViewSet, PartnerViewSet,
                    ProductViewSet, SiteContentView, TestimonialViewSet)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet, basename='product')
router.register(r'partners', PartnerViewSet, basename='partner')
router.register(r'testimonials', TestimonialViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'hero-slides', HeroSlideViewSet)

from django.urls import path
urlpatterns = router.urls + [path('site-content/', SiteContentView.as_view())]
