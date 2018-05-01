from django.core.management.base import BaseCommand
import configparser
import random
import string
import os.path


class Command(BaseCommand):
    help = 'Create file with environment variables'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str)

    def handle(self, *args, **options):
        config = configparser.ConfigParser()
        config.optionxform = str
        while True:
            try:
                config['SETTINGS'] = {
                    'SECRET_KEY': self.random_string,
                    'ALLOWED_HOSTS': 'localhost, 127.0.0.1',
                    'DEBUG': False,
                    'IPSTACK_ACCESS_KEY': '0e3e331a2e84afc272c53c97982cc67c'
                }
                break
            except ValueError:
                continue
        for file in options['file']:
            if os.path.isfile(file):
                print('File {} already exist, cannot rewrite it. '.format(file))
                continue
            try:
                with open(file, 'w') as f:
                    config.write(f)
                    print('Config file was created success')
                    continue
            except IOError:
                pass

    @property
    def random_string(self):
        return "".join(
            [random.SystemRandom().choice("{}{}{}".format(string.ascii_letters, string.digits, string.punctuation))
             for _ in range(50)])
