import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myshop.settings")
django.setup()

from shop.models import Product

data = []

for p in Product.objects.all():
    data.append({
        "name": p.name,
        "slug": p.slug,
        "image": p.image.name if p.image else "",
        "stock": p.stock,
    })

with open("export_images_stock.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Экспорт завершён.")