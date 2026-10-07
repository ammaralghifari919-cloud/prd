from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    QUALITY_CHOICES = [('Medium', 'Medium'), ('Premium', 'Premium')]

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    product_name = models.CharField(max_length=150)
    quality_tier = models.CharField(max_length=20, choices=QUALITY_CHOICES)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


class Partner(models.Model):
    TYPE_CHOICES = [('distributor', 'Distributor'), ('agen', 'Agen')]
    STATUS_CHOICES = [('active', 'Active'), ('inactive', 'Inactive')]

    name = models.CharField(max_length=150)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    city = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    image = models.ImageField(upload_to='partners/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    customer_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    comment = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer_name


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    featured_image = models.URLField(blank=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SiteContent(models.Model):
    """Konten teks homepage yang bisa diedit lewat admin."""

    hero_title = models.CharField(max_length=200, default='Produk Olahan Berkualitas Sejak 1970')
    hero_subtitle = models.CharField(max_length=255, default='BPOM • Halal • NKV • HACCP')
    hero_cta = models.CharField(max_length=100, default='Lihat Katalog')
    company_title = models.CharField(max_length=200, default='Tentang Baso Karawaci')
    company_description = models.TextField(default='Berdiri sejak 1970, PT Anugrah Citra Boga menghadirkan produk olahan berkualitas seperti bakso, sosis, dan olahan ikan dengan komitmen pada kualitas dan keamanan pangan.')
    products_title = models.CharField(max_length=200, default='Produk Terbaik Kami')
    categories_title = models.CharField(max_length=200, default='Kategori Produk')
    testimonials_title = models.CharField(max_length=200, default='Ulasan Pelanggan')
    distribution_title = models.CharField(max_length=200, default='Temukan Distributor & Agen Terdekat')
    articles_title = models.CharField(max_length=200, default='Kabar Terkini')
    marketplace_title = models.CharField(max_length=200, default='Belanja di Marketplace')
    tokopedia_url = models.URLField(blank=True)
    shopee_url = models.URLField(blank=True)
    footer_text = models.CharField(max_length=255, default='© PT Anugrah Citra Boga — Baso Karawaci, Karawaci, Tangerang')
    hero_image_url = models.URLField(blank=True, help_text='URL background hero (kosongkan untuk gradient default)')
    hero_image = models.ImageField(upload_to='hero/', blank=True, null=True, help_text='Upload gambar hero (prioritas di atas URL)')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Konten Situs'


class HeroSlide(models.Model):
    image = models.ImageField(upload_to='hero/')
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    cta = models.CharField(max_length=100, default='Lihat Katalog', blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title or f'Slide {self.id}'
