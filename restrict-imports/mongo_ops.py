__all__ = ["ops"]


def _deco_class_attributes(method):
    def deco_method(self, **kwargs):
        # Set the attributes of the class instance passed in kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

        # Call the original method
        method(self)

        # Delete the set attributes of the class instance
        # This is to avoid the attributes being set to the class instance and used in the future
        # by other methods
        for key, value in kwargs.items():
            delattr(self, key)

    return deco_method


# Class to hold the operations
# Using underscore on name to highlight the class is private and not be used outside this module
class _MongoOperations:
    class __PrivateOps:
        # The class defines the actual operations
        @_deco_class_attributes
        def find(self):
            print(f"Finding in MongoDB collection:{self.collection}\nquery:{self.query}")

        @_deco_class_attributes
        def insert(self):
            print(f"Insert in MongoDB collection:{self.collection}\ndata:{self.data}")

        @_deco_class_attributes
        def update(self):
            print(f"Update in MongoDB collection:{self.collection}\nquery:{self.query}\ndata:{self.data}")

    class PublicOps:
        # Class acting as an interface to the private class
        def __init__(self, cls_interface):
            self.cls_interface = cls_interface()._MongoOperations__PrivateOps()

        def find(self, collection, query):
            self.cls_interface.find(collection=collection, query=query)

        def insert(self, collection, data):
            self.cls_interface.insert(collection=collection, data=data)

        def update(self, collection, query, data):
            self.cls_interface.update(collection=collection, query=query, data=data)


ops = _MongoOperations.PublicOps(_MongoOperations)

