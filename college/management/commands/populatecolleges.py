from django.core.management.base import BaseCommand
from college.models import College

class Command(BaseCommand):
    help = 'Populate the database with sample college data for Nepal.'

    def handle(self, *args, **kwargs):
        College.objects.all().delete()
        colleges_data = [
            # ... (copy your sample data here, as in your previous script) ...
        ]
        for college_data in colleges_data:
            College.objects.create(**college_data)
        self.stdout.write(self.style.SUCCESS(f'Successfully populated {len(colleges_data)} colleges.'))
