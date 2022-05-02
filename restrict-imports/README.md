## Run the usage file
`python usage.py`

The intension is to avoid/restrict the import of the MongoOpertions class and direct usage of the operations.
The attempt is to have a some additional private defination for the class and methods to let know user not to use them, rather use the available `ops` object of the public interface of the class. 
