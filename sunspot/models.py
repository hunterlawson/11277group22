from mongoengine import *

class Bookmark(EmbeddedDocument):
    location = StringField(required=True)
    date = DateTimeField(required=True)

class User(Document):
    email = StringField(required=True)
    username = StringField(required=True)
    password = StringField(required=True)
    admin = BooleanField()
    bookmarks = EmbeddedDocumentListField(Bookmark)