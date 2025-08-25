from django.core.management.base import BaseCommand
from college.models import College

class Command(BaseCommand):
    help = 'Populate the database with sample college data for Nepal.'

    def handle(self, *args, **kwargs):
        # Clear existing data (optional, comment out if you want to append)
        College.objects.all().delete()

        # Sample college data based on provided sources
        colleges_data = [
            {
                "name": "Certified College of Accountancy (CCA)",
                "location": "Thapagaun, Kathmandu",
                "affiliation": "National Examination Board (NEB)",
                "courses": "ACCA, Bachelor of Business Studies (BBS)",
                "budget": "Contact college for budget details",
                "facilities": "Library, computer labs, seminar halls, Wi-Fi"
            },
            {
                "name": "Informatics College Pokhara",
                "location": "Matepani, Pokhara",
                "affiliation": "London Metropolitan University, UK",
                "courses": "BBA in Accounting & Finance, BBA in Marketing, B.Sc. (Hons) in Computing, BBA in International Business",
                "budget": "Approx. $7,000–$13,000 USD/year for international students",
                "facilities": "Computer labs, library, student lounge, Wi-Fi, cafeteria"
            },
            {
                "name": "ISMT College",
                "location": "Tinkune, Kathmandu",
                "affiliation": "University of Sunderland, UK",
                "courses": "BSc (Hons) Cyber Security and Digital Forensics, BHM, BSc (Hons) Computer Systems Engineering, BA (Hons) Business and Management (BBA)",
                "budget": "Approx. $7,000–$13,000 USD/year for international students",
                "facilities": "Modern classrooms, IT labs, cafeteria, hostel, sports facilities"
            },
            {
                "name": "Kathmandu Model College",
                "location": "Bagbazar, Kathmandu",
                "affiliation": "Tribhuvan University",
                "courses": "BASW, BA in Major English, BA in Psychology, BBM, BCA",
                "budget": "Approx. $1,000–$8,700 USD/year",
                "facilities": "Library, computer labs, sports facilities, counseling services"
            },
            {
                "name": "KMC Lalitpur",
                "location": "Balkumari, Lalitpur",
                "affiliation": "National Examination Board (NEB)",
                "courses": "Ten Plus Two (+2) Law, Management, Science",
                "budget": "Contact college for budget details",
                "facilities": "Science labs, library, sports ground, Wi-Fi"
            },
            {
                "name": "Padmashree College",
                "location": "Tinkune, Kathmandu",
                "affiliation": "Nilai University, Malaysia",
                "courses": "B.Tech Food Technology, BCA, BBA, BHM, BIT",
                "budget": "Approx. $7,000–$13,000 USD/year for international students",
                "facilities": "Food tech labs, computer labs, library, hostel"
            },
            {
                "name": "Nepal Mega College",
                "location": "Babarmahal, Kathmandu",
                "affiliation": "Tribhuvan University",
                "courses": "BBS, BBM, BCA, BSW, +2 Management, Science, Humanities",
                "budget": "Approx. $1,000–$5,000 USD/year",
                "facilities": "Library, science labs, computer labs, sports facilities"
            },
            {
                "name": "Ace Institute of Management",
                "location": "New Baneshwor, Kathmandu",
                "affiliation": "Pokhara University",
                "courses": "BBA, MBA, Executive MBA",
                "budget": "Contact college for budget details",
                "facilities": "Library, seminar halls, Wi-Fi, cafeteria"
            },
            {
                "name": "St. Xavier’s College",
                "location": "Maitighar, Kathmandu",
                "affiliation": "Tribhuvan University",
                "courses": "BSc Physics, Microbiology, BSW, +2 Science, Management",
                "budget": "Approx. $1,500–$6,000 USD/year",
                "facilities": "Science labs, library, sports facilities, counseling center"
            },
            {
                "name": "Little Angels’ College",
                "location": "Hattiban, Lalitpur",
                "affiliation": "National Examination Board (NEB)",
                "courses": "+2 Science, Management, GCE A-Level",
                "budget": "Contact college for budget details",
                "facilities": "Science labs, library, sports ground, hostel"
            },
            {
                "name": "Pokhara University School of Engineering",
                "location": "Lekhnath, Pokhara",
                "affiliation": "Pokhara University",
                "courses": "BE Civil, BE Computer, BE Electrical and Electronics",
                "budget": "Approx. $2,000–$7,000 USD/year",
                "facilities": "Engineering labs, library, hostel, Wi-Fi"
            },
            {
                "name": "Nepal Engineering College",
                "location": "Changunarayan, Bhaktapur",
                "affiliation": "Pokhara University",
                "courses": "BE Civil, BE Computer, BE Electronics and Communication",
                "budget": "Approx. $2,000–$7,000 USD/year",
                "facilities": "Engineering labs, library, sports facilities, hostel"
            },
            {
                "name": "Kantipur Engineering College",
                "location": "Dhapakhel, Lalitpur",
                "affiliation": "Tribhuvan University",
                "courses": "BE Civil, BE Computer, BE Electronics",
                "budget": "Approx. $2,000–$7,000 USD/year",
                "facilities": "Engineering labs, computer labs, library, Wi-Fi"
            },
            {
                "name": "Himalaya College of Engineering",
                "location": "Chyasal, Lalitpur",
                "affiliation": "Tribhuvan University",
                "courses": "BE Civil, BE Computer, BE Architecture",
                "budget": "Approx. $2,000–$7,000 USD/year",
                "facilities": "Engineering labs, library, hostel, sports facilities"
            },
            {
                "name": "Balkumari College",
                "location": "Narayangarh, Chitwan",
                "affiliation": "Tribhuvan University",
                "courses": "BBS, B.Ed, +2 Management, Science",
                "budget": "Approx. $1,000–$4,000 USD/year",
                "facilities": "Library, science labs, computer labs, sports ground"
            },
            {
                "name": "Saptagandaki Multiple Campus",
                "location": "Bharatpur, Chitwan",
                "affiliation": "Tribhuvan University",
                "courses": "BBS, BA, B.Ed, +2 Management, Humanities",
                "budget": "Approx. $1,000–$4,000 USD/year",
                "facilities": "Library, computer labs, sports facilities"
            },
            {
                "name": "Birendra Multiple Campus",
                "location": "Bharatpur, Chitwan",
                "affiliation": "Tribhuvan University",
                "courses": "BSc, BBS, BA, +2 Science, Management",
                "budget": "Approx. $1,000–$4,000 USD/year",
                "facilities": "Science labs, library, computer labs, hostel"
            },
            {
                "name": "Kshitiz International College",
                "location": "Butwal, Rupandehi",
                "affiliation": "Pokhara University",
                "courses": "BBA, BCA",
                "budget": "Approx. $1,500–$5,000 USD/year",
                "facilities": "Library, computer labs, Wi-Fi, cafeteria"
            },
            {
                "name": "Lumbini Banijya Campus",
                "location": "Butwal, Rupandehi",
                "affiliation": "Tribhuvan University",
                "courses": "BBS, MBA, +2 Management",
                "budget": "Approx. $1,000–$4,000 USD/year",
                "facilities": "Library, seminar halls, computer labs"
            },
            {
                "name": "Nepal College of Travel and Tourism Management",
                "location": "Lalitpur, Kathmandu",
                "affiliation": "Purbanchal University",
                "courses": "BTTM, BHM",
                "budget": "Approx. $2,000–$6,000 USD/year",
                "facilities": "Training kitchens, library, computer labs, hostel"
            }
        ]

        # Populate the database
        for college_data in colleges_data:
            College.objects.create(**college_data)

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {len(colleges_data)} colleges.'))