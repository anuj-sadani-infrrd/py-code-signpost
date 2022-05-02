from mongo_ops import ops


ops.find(collection="user_model", query={"_id": "123-456"})

ops.insert(
    collection="user_model",
    data={
        "_id": "123-456",
        "name": "invoice",
        "fields": [
            {"fieldId": "888-999-000", "name": "invoice_number", "type": "string"},
            {"fieldId": "777-888-999", "name": "invoice_date", "type": "date"},
        ],
    },
)

ops.update(collection="user_model", query={"_id": "123-456"}, data={"name": "Invoice"})
