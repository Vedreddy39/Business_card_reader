import easyocr as ocr  
import streamlit as st  
from PIL import Image 
import numpy as np 

st.set_page_config(page_title='Business Card Reader', layout='wide')

#title
st.title("Business Card Reader")

#subtitle
st.subheader("Using `easyocr`, `streamlit`")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


@st.cache_data
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 



if image is not None:
    reader = load_model() #load model
    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 AI is at Work! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = {'Company Name': '','Card Holder Name': '','Designation': '','Mobile Number': '','Email Address': '','Website url': '', 'Area': ''}
       
        result_text['Card Holder Name'] = result[0][1]
        result_text['Designation'] = result[1][1] 
        
        for r in result:
            if '@' in r[1]:
                result_text['Email Address'] = r[1]
            elif '.com' in r[1]:
                result_text['Website url'] = r[1]
            elif '+' in r[1]:
                result_text['Mobile Number'] = r[1]
            elif 'St' in r[1] or 'Rd' in r[1]:
                result_text['Area'] = r[1]
           
            else:
                result_text['Company Name'] = r[1]


        st.write(result_text)
    
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("Made by Ved")
