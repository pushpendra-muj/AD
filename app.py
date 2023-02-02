import streamlit as st
import os
import database as db
from keras.models import model_from_json
import numpy as np
from tensorflow.keras.preprocessing import image
# from keras.preprocessing import image
with open('model_arch.json', 'r') as json_file:
    json_savedModel= json_file.read()
model = model_from_json(json_savedModel)
model.load_weights('my_model_weights.h5')



def form():
    st.write ("This is a form")
    with st.form(key= "Information form"):
        name=st.text_input("Enter you name ")
        age=st.number_input("Enter your age: ",step=1)
        address=st.text_input("Enter your Address: ")
        # date=st.date_input("Enter the date: ")
        st.markdown("Predicted Class is "+str(pred_class))
        pred=str(pred_class)
        submission=st.form_submit_button (label="Submit")
        if submission == True :
            db.insert_result(name,age,address,pred)
            st.success ("Successfully submitted")


def predict_img(img):
    input_img = image.img_to_array(img)
    input_img = np.expand_dims(input_img, axis=0)
    predict_img = model.predict(input_img)
    y_pred = np.argmax(predict_img, axis=1)
    target_names = ['Actinic Keratosis', 'Basal Cell Carcinoma', 'Dermatofibroma','Melanoma' , 'Nevus', 'Pigmented Benign Keratosis', 'Seborrheic Keratosis','Squamous Cell Carcinoma' , 'Vascular Lesion']
    return target_names[y_pred[0]]

html_temp = """
    <div style="background-color:#f63366;padding:10px;margin-bottom: 25px">
    <h2 style="color:white;text-align:center;">Skin Cancer Detection</h2>
    <p style="color:white;text-align:center;" >This is a <b>Streamlit</b> app use for prediction of the <b>9 type of Skin Cancer</b>.</p>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

option = st.radio('', ['Choose a test image', 'Choose your own image'])
if option == 'Choose your own image':
    uploaded_file = st.file_uploader("Choose an image...", type="jpg") #file upload
    if uploaded_file is not None:
        
        img = image.load_img(uploaded_file, target_size=(180,180,3))
        pred_class = predict_img(img)
        col1, col2 = st.columns(2)
        with col1:
            st.image(img, width=200)
        with col2:
            st.success("Skin Cancer Type:  [" + str(pred_class) + "] ")
            form()
else:
    test_images = os.listdir('sample_images')
    test_image = st.selectbox('Please select a test image:', test_images)
    file_path = 'sample_images/' + test_image
    img = image.load_img(file_path, target_size=(180,180,3))
    pred_class = predict_img(img)
    col1, col2 = st.columns(2)
    with col1:
        st.image(img, width=200)
    with col2:
        st.success("Skin Cancer Type:  [" + str(pred_class) + "] ")
        form()
