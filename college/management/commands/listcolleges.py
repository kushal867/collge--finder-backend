from django.core.management.base import BaseCommand
from college.models import College

class Command(BaseCommand):
    help = 'List all colleges in the system.'

    def handle(self, *args, **kwargs):
        colleges = College.objects.all()
        if not colleges:
            self.stdout.write(self.style.WARNING('No colleges found.'))
        else:
            self.stdout.write(self.style.SUCCESS('Colleges:'))
            for college in colleges:
                self.stdout.write(f'- Name: {college.name}')
                self.stdout.write(f'  Affiliation: {college.affiliation}')
                self.stdout.write(f'  Budget: {college.budget}')
                self.stdout.write(f'  Province: {college.province}')
                self.stdout.write(f'  District: {college.district}')
                self.stdout.write(f'  Municipality: {college.municipality}')
                self.stdout.write(f'  Website: {college.website}')
                self.stdout.write(f'  Scholarship: {college.scholarship}')
                self.stdout.write(f'  Contact Info: {college.contact_info}')
                self.stdout.write(f'  Latitude: {college.latitude}')
                self.stdout.write(f'  Longitude: {college.longitude}')
                self.stdout.write('')