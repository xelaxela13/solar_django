import configparser
import random
import string
import os.path


def run():
    config = configparser.ConfigParser()
    config.optionxform = lambda x: x.upper()
    while True:
        try:
            config['SETTINGS']= {
                'SECRET_KEY': random_string(),
                'ALLOWED_HOSTS': '*',
                'DEBUG': True,
                'IPSTACK_ACCESS_KEY': '0e3e331a2e84afc272c53c97982cc67c',
                'GMAIL_PASSWORD': '',
                'GMAIL_USER': ''

            }
            config['DB']= {
                'name': 'postgres',
                'USER': 'postgres',
                # 'PASSWORD': 'postgres',
                'HOST': 'db',
                'PORT': '5432'
            }
            break
        except ValueError:
            continue
    file = '.env'
    if os.path.isfile(file):
        print('File {} already exist, cannot rewrite it. '.format(file))
        return
    try:
        with open(file, 'w') as f:
            config.write(f)
            print('Config file was created success')
            return
    except IOError as err:
        print(err)
        return


def random_string():
    return "".join(
        [random.SystemRandom().choice("{}{}{}".format(string.ascii_letters, string.digits, string.punctuation))
         for _ in range(50)])


if __name__ == '__main__':
    run()
