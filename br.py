#pip install streamlit
#pip install easyocr

import streamlit as st
import easyocr


def extract_info(image):
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(image)
    extracted_info = {'company_name': '','card holder name': '','designation': '','mobile_number': '','email_address': '','website_url': '', 'address': ''}
   
    extracted_info['card holder name'] = result[0][1]
    extracted_info['designation'] = result[1][1] 
    
    for r in result:
        if '@' in r[1] and '.com' in r[1]:
            extracted_info['email_address'] = r[1]
        elif '.com' in r[1]:
            extracted_info['website_url'] = r[1]
        elif '+' in r[1]:
            extracted_info['mobile_number'] = r[1]
        elif 'St' in r[1] or 'Rd' in r[1]:
            extracted_info['address'] = r[1]

    return extracted_info

st.title("Business Card Reader")
st.caption('Using Easyocr')
image = st.file_uploader(label = "Upload your image", type = ['jpeg', 'png', 'jpg'])
st.write("")
st.write("Analyzing image...")
extracted_info = extract_info(image)
st.write("Extracted information:")
for key, value in extracted_info.items():
    st.write(f"{key}: {value}")

    
