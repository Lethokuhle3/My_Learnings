import streamlit as st
import time

col1, col2, col3 = st.columns([1, 2, 1])

col1.markdown(" ## Welcome to Letho's application, so Glad to have you here!")
col1.markdown("Lets get the party started!")

uploadedPhoto = col2.file_uploader("Upload a photo")
camera_photo = col2.camera_input("Take a picture")

progress_bar = col2.progress(0)

for percentage_completed in range(100):
    time.sleep(0.05)
    progress_bar.progress(percentage_completed + 1)

col2.success("Photo uploaded successfully!")

col3.metric(label="Temperature", value="60 C", delta="3 C")

# Expanders

with st.expander("Click to read more"):
    st.write(
        "Dont say I didnt warn you about this .. I was talking to your mom the other day and she said that we must displine you because you have been getting out of hand")

    if uploadedPhoto is None:
        st.image(camera_photo)
    else:
        st.image(uploadedPhoto)

    # Callbacks and session states-- when I want to keep track if the photo has een uploaded or not



