import streamlit as st
import base64
import tensorflow
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model

st.title("Dog or Cat :confused:")
#st.text_input("Enter Name: ", 'Gabriel')
#st.image('kolkata.jpg', caption='Kolkata')
#st.file_uploader()


model= load_model('cat_dog_model.h5')
def set_bg(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
        # background-size:cover always works 
         f"""
         <style>
         .stApp {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});          
            background-size: cover;
                
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


set_bg('cover2.jpg')

image_data= st.file_uploader("Choose an image", type=['jpg', 'png', 'jpeg'])


def predict():
    from tensorflow.keras.preprocessing import image
    test_image = image.load_img(image_data, target_size=(256,256))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
    #train_set.class_indices
    if result[0][0] ==1:
        st.success("Yeah a dog!! :dog:")
        st.image(image_data)        
    else:
        st.success("Yeah a cat!! :cat:")
        st.image(image_data)
        
    
    
try:
    if image_data is not None:
        st.button('Predict', on_click=predict)

except TypeError:
    st.error("No input")
