from typing import Any
from blog.models import category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="This command inserts categories data"

    def handle(self, *args:Any, **options:Any):
        category.objects.all().delete()
        categories=['sports','Technology','Science','Art','Food']

        for category_name in categories:
            category.objects.create(name=category_name)

        self.stdout.write(self.style.SUCCESS("Completed inerting data!"))