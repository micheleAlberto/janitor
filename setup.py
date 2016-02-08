
import sys
def set_token(t):
    with open('janitor/token.py','w') as f:
        f.write("pushbullet_token=\"{}\"\n".format(t))
    return

def token_from_args():
    return None
    if len(sys.argv)==1:
        return None
    else:
        return sys.arv[1]

def token_from_input():
    print 'you can find the pushbullet token by loggin in to:'
    print '\thttps://www.pushbullet.com/#settings/account'
    print 'request an access token and copy paste it below:'
    t=raw_input("PUSHBULLET TOKEN:")
    return t

t=token_from_args()
if not t:
    t=token_from_input()
set_token(t)

import janitor as dayman
dayman.call('janitor setup','https://youtu.be/TzaVd6zl2bA?t=1m5s')
from setuptools import setup
setup(name='janitor',
      version='0.1',
      description='A personal library to notify yourselg via pushbullet',
      url='https://github.com/micheleAlberto/janitor',
      author='Michele Alberto',
      license='MIT',
      packages=['janitor'],
      zip_safe=False)

