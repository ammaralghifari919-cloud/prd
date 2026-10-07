from django.contrib import admin
from django.utils.html import format_html

from .models import Article, Category, HeroSlide, Partner, Product, SiteContent, Testimonial

admin.site.site_header = 'Baso Pak De Ammar - Admin'
admin.site.site_title = 'Baso Pak De Ammar Admin'
admin.site.index_title = 'Kelola Konten Website'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'created_at')
    search_fields = ('category_name',)
    prepopulated_fields = {'slug': ('category_name',)}
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'quality_tier', 'is_favorite', 'updated_at')
    list_filter = ('category', 'quality_tier', 'is_favorite')
    search_fields = ('product_name',)
    list_editable = ('is_favorite',)
    prepopulated_fields = {'slug': ('product_name',)}
    fields = ('category', 'product_name', 'quality_tier', 'slug', 'description', 'image', 'image_url', 'is_favorite')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 20


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'city', 'status_badge', 'phone', 'image_preview')
    list_filter = ('type', 'status', 'city')
    search_fields = ('name', 'city')
    list_editable = ()
    fields = ('name', 'type', 'city', 'address', 'phone', 'status', 'image', 'image_preview_large', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'image_preview_large')
    date_hierarchy = 'created_at'
    list_per_page = 15

    @admin.display(description='Status', ordering='status')
    def status_badge(self, obj):
        color = '#2F855A' if obj.status == 'active' else '#C53030'
        bg = '#C6F6D5' if obj.status == 'active' else '#FED7D7'
        return format_html(
            '<span style="background:{};color:{};padding:3px 10px;border-radius:999px;font-size:11px;font-weight:700;">{}</span>',
            bg, color, obj.status.upper(),
        )

    @admin.display(description='Foto')
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:34px;width:34px;object-fit:cover;border-radius:6px;" />', obj.image.url)
        return '—'

    @admin.display(description='Pratinjau gambar')
    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:220px;border-radius:10px;box-shadow:0 2px 8px rgba(0,0,0,.15);" />', obj.image.url)
        return 'Belum ada gambar'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'location', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('customer_name', 'location')
    list_editable = ('is_published',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'updated_at')
    search_fields = ('title',)
    date_hierarchy = 'published_at'
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'content', 'image', 'featured_image', 'published_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    fields = ('image', 'title', 'subtitle', 'cta', 'order', 'is_active')
    ordering = ('order', 'id')


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'updated_at')
    fieldsets = (
        ('Tentang Perusahaan', {'fields': ('company_title', 'company_description')}),
        ('Section Titles', {'fields': ('products_title', 'categories_title', 'testimonials_title', 'distribution_title', 'articles_title', 'marketplace_title')}),
        ('Marketplace', {'fields': ('tokopedia_url', 'shopee_url')}),
        ('Footer', {'fields': ('footer_text',)}),
    )
    readonly_fields = ('updated_at',)
