from celery import task
import requests
from django.conf import settings


def get_client_ip(request_meta):
    keys = ['HTTP_X_FORWARDED_FOR', 'HTTP_X_REAL_IP', 'REMOTE_ADDR']
    for key in keys:
        try:
            x_forwarded_for = request_meta[key]
            ip = x_forwarded_for.split(',')[-1].strip()
            return ip
        except KeyError:
            continue
    return ''

@task
def get_location(language_code, request_meta):
    ip_address = get_client_ip(request_meta)
    response = requests.get('http://api.ipstack.com/{}'.format(ip_address),
                            timeout=5,
                            verify=False,
                            params={'access_key': settings.IPSTACK_ACCESS_KEY,
                                    'language': language_code}
                            )
    geodata = response.json()
    city = None
    try:
        city = geodata['city']
    except KeyError:
        pass
    return city if city is not None else ''
