from deta import Deta

DETA_KEY = "d03z5mkt_TafGU463A3bYRKHcWz4zP8au8bTdXUuQ"

deta = Deta(DETA_KEY)

db=deta.Base("Skin_Cancer_Detection")

def insert_result(name,age,address,pred):
    db.put({
        "name": name,
        "age": age,
        "address": address,
        "pred": pred
    })
