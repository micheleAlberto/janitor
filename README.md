# janitor
A personal library to notify yourselg via pushbullet

##install
you need a pushbullet account and a pushbullet token

[pushbullet](https://docs.pushbullet.com/)
[get a token](https://www.pushbullet.com/#settings/account)

```
git clone https://github.com/micheleAlberto/janitor.git
cd janitor
python setup.py install
```
The last command will ask you to provide the token, just copy paste it.

##use it
```python
import janitor as charlie
charlie.call()
charlie.call('this is a notification title','this is a message')
charlie.call(message="""
You know what? 
Let me kick down a little thing to you that our Founding Fathers kicked down to me. 
It goes, "Don't. Tread. On me," and right now, you guys are TREADING ALL OVER ME. """)
```

