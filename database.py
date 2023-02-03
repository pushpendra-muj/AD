from deta import Deta

DETA_KEY = "d03z5mkt_TafGU463A3bYRKHcWz4zP8au8bTdXUuQ"

deta = Deta(DETA_KEY)

db=deta.Base("Skin_Cancer_Detection")

def insert_result(docname,doc_contact,doc_quli,hospital_name,hospital_address,id,name,age,date,address,pat_contact,aadhar,remark,pred):
    db.put({
        "docname":docname,
        "doc_contact":doc_contact,
        "doc_quli":doc_quli,
        "hospital_name":hospital_name,
        "hospital_address":hospital_address,
        "id":id,
        "name":name,
        "age":age,
        "date":str(date),
        "address":address,
        "pat_contact":pat_contact,
        "aadhar":aadhar,
        "remark":remark,
        "pred":pred,
    })
