from django.core.management.base import BaseCommand, CommandError

from mynews.newsw.models import News, Appointment


class Command(BaseCommand):


    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))

        else:
            try:
                category = News.objects.get(name=options['category'])
                News.objects.filter(postCategory__name=category.name).delete()
                self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {category.name}'))
            except Appointment.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Could not find category {category}'))