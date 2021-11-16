from mongoengine import *
from sunspot import login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.objects.get(id=user_id)
    except Exception as e:
        print(e)
    
    return None
    
class Bookmark(EmbeddedDocument):
    location = DictField(required=True)
    date = DateTimeField(default=datetime.utcnow)

class User(Document, UserMixin):
    email = StringField(required=True, unique=True)
    username = StringField(required=True)
    password = StringField(required=True)
    admin = BooleanField()
    bookmarks = EmbeddedDocumentListField(Bookmark)