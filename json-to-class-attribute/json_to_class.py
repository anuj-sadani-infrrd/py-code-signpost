import json


class Generic:
    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj


data = json.load(open("sample-1.json"), object_hook=Generic.from_dict)

# Access the values with dot "." notation
print(data.root.name)  # root
for child in data.root.children[0].children:
    print(child.name)  # child1.1 child1.2
