import configparser
import random
import string
import os.path


def run():
    config = configparser.ConfigParser()
    config.optionxform = str
    while True:
        try:
            config['SETTINGS'] = {
                'SECRET_KEY': random_string(),
                'ALLOWED_HOSTS': 'localhost, 127.0.0.1',
                'DEBUG': True,
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
    except IOError as err:
        print('Cannot create file: {}'.format(err))


def random_string():
    return "".join(
        [random.SystemRandom().choice("{}{}{}".format(string.ascii_letters, string.digits, string.punctuation))
         for _ in range(50)])


def set():
    vars = {
        'SECRET_KEY': random_string(),
        'ALLOWED_HOSTS': 'localhost, 127.0.0.1',
        'DEBUG': True,
    }
    for key, val in vars.items():
        os.environ.setdefault(key.upper(), val)


if __name__ == '__main__':
    run()
