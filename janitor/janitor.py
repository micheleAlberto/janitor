
from pushbullet import Pushbullet
import sys
from token import pushbullet_token

pb = Pushbullet(pushbullet_token) if pushbullet_token else None

def context():
    return ' '.join(sys.argv)

def call(situation=None,message=None):
    a=situation if situation else context()
    b=message if message else "Cat in the wall, eh?!"
    if pb:
        push = pb.push_note(a,b)
    else:
        print a
        print b

