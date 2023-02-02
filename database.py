from deta import Deta

DETA_KEY = "d03z5mkt_KJv6bvaiTBvxUuJJLMNXjfvLYioRig61"

deta = Deta(DETA_KEY)

db=deta.Base("Skin Cancer Detection")

def insert_result(name,age,address,pred):
    db.put({
        "name": name,
        "age": age,
        "address": address,
        "pred": pred
    })