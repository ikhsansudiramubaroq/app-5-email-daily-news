import requests
import streamlit as st

# persiapkan api key
api_key = "BdqyKkhXY2Bt0INDBtQJq9tW6yQd1fnHdbd5heu7"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# get request data
response1 = requests.get(url)
data = response1.json()

# extract image, url and explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# donwload image
image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)
