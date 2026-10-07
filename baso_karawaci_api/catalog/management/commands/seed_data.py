from django.core.management.base import BaseCommand
from django.utils import timezone

from catalog.models import Article, Category, Partner, Product, Testimonial


class Command(BaseCommand):
    help = 'Seed sample catalog data'

    def handle(self, *args, **options):
        bakso = Category.objects.get_or_create(slug='bakso', defaults={'category_name': 'Bakso', 'description': 'Produk bakso'})[0]
        sosis = Category.objects.get_or_create(slug='sosis', defaults={'category_name': 'Sosis', 'description': 'Produk sosis'})[0]
        ikan = Category.objects.get_or_create(slug='olahan-ikan', defaults={'category_name': 'Olahan Ikan', 'description': 'Produk olahan ikan'})[0]

        products = [
            ('Bakso Sapi Premium', 'Premium', bakso, True, 'Bakso sapi berkualitas tinggi.'),
            ('Bakso Sapi Medium', 'Medium', bakso, True, 'Bakso sapi ekonomis.'),
            ('Sosis Sapi Premium', 'Premium', sosis, True, 'Sosis sapi pilihan.'),
            ('Otak-Otak Ikan', 'Medium', ikan, False, 'Otak-otak ikan segar.'),
        ]
        for name, tier, cat, fav, desc in products:
            Product.objects.get_or_create(slug=name.lower().replace(' ', '-'), defaults={
                'product_name': name, 'quality_tier': tier, 'category': cat,
                'is_favorite': fav, 'description': desc,
            })

        partners = [
            ('PT Distributor Utama', 'distributor', 'Jakarta', 'Jl. Contoh No. 1', '021-123456', 'active'),
            ('Agen Bandung', 'agen', 'Bandung', 'Jl. Agen No. 2', '022-654321', 'active'),
            ('Agen Surabaya', 'agen', 'Surabaya', 'Jl. Contoh No. 3', '031-111222', 'active'),
        ]
        for name, typ, city, addr, phone, status in partners:
            Partner.objects.get_or_create(name=name, defaults={'type': typ, 'city': city, 'address': addr, 'phone': phone, 'status': status})

        Testimonial.objects.get_or_create(customer_name='Ibu Sari', defaults={'location': 'Jakarta', 'comment': 'Enak dan higienis!', 'is_published': True})
        Testimonial.objects.get_or_create(customer_name='Bapak Budi', defaults={'location': 'Bandung', 'comment': 'Produk favorit keluarga.', 'is_published': True})

        Article.objects.get_or_create(slug='kabar-terbaru-baso-karawaci', defaults={
            'title': 'Kabar Terbaru Baso Karawaci', 'content': 'Konten kabar terbaru...',
            'published_at': timezone.now(),
        })

        self.stdout.write(self.style.SUCCESS('Seed data selesai'))
