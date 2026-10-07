from rest_framework import serializers

from .models import Article, Category, Partner, Product, SiteContent, Testimonial, HeroSlide


class CategorySerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Category
        fields = ['category_id', 'category_name', 'slug', 'description', 'created_at', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source='id', read_only=True)
    category_name = serializers.CharField(source='category.category_name', read_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Product
        fields = ['product_id', 'category', 'category_name', 'product_name', 'quality_tier', 'slug',
                  'description', 'image', 'image_url', 'is_favorite', 'created_at', 'updated_at']


class PartnerSerializer(serializers.ModelSerializer):
    partner_id = serializers.IntegerField(source='id', read_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Partner
        fields = ['partner_id', 'name', 'type', 'city', 'address', 'phone', 'status', 'image', 'created_at', 'updated_at']


class TestimonialSerializer(serializers.ModelSerializer):
    review_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Testimonial
        fields = ['review_id', 'customer_name', 'location', 'comment', 'is_published', 'created_at', 'updated_at']


class ArticleSerializer(serializers.ModelSerializer):
    article_id = serializers.IntegerField(source='id', read_only=True)
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = Article
        fields = ['article_id', 'title', 'slug', 'content', 'featured_image', 'image', 'published_at', 'created_at', 'updated_at']


class HeroSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSlide
        fields = ['id', 'image', 'title', 'subtitle', 'cta', 'order', 'is_active']


class SiteContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteContent
        fields = '__all__'
