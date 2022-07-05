# from category import Category
# from document import Document
# from topic import Topic
from project.category import Category
from project.document import Document
from project.topic import Topic

class Storage:
    def __init__(self) -> None:
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        msg = "\n".join([repr(d) for d in self.documents])
        return msg
    
    @staticmethod
    def get_item(item_id: int, source: list):
        for item in source:
            if item.id == item_id:
                return item

    @staticmethod
    def add_item(item, source: list):
        if item not in source:
            source.append(item)

    @classmethod
    def edit_item(cls, item_id: int, source: list, *changes):
        item_obj = cls.get_item(item_id, source)
        item_obj.edit(*changes)

    @classmethod
    def delete_item(cls, item_id: int, source: list):
        item_obj = cls.get_item(item_id, source)
        source.remove(item_obj)

    def add_category(self, category: Category):
        self.add_item(category, self.categories)

    def add_topic(self, topic: Topic):
        self.add_item(topic, self.topics)

    def add_document(self, document: Document):
        self.add_item(document, self.documents)

    def edit_category(self, category_id: int, new_name:str):
        self.edit_item(category_id, self.categories, new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.edit_item(topic_id, self.topics, new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        self.edit_item(document_id, self.documents, new_file_name)

    def delete_category(self, category_id):
        self.delete_item(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.delete_item(topic_id, self.topics)

    def delete_document(self, document_id):
        self.delete_item(document_id, self.documents)

    def get_document(self, document_id):
        return self.get_item(document_id, self.documents)
