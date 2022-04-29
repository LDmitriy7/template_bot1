from typing import Optional

import mongoengine as me


class Document(me.Document):
    meta = {
        'abstract': True,
    }

    @classmethod
    def object(cls, *args, **kwargs) -> Optional[Document]:
        return cls.objects(*args, **kwargs).first()


class Test(Document):
    a: str = me.StringField()
    b: int = me.IntField()
