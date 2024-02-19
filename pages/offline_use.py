import streamlit, PIL
from digital_resume import init

init()

image = PIL.Image.open("./assets/footer_pic.png")
cols = streamlit.columns(3)
with cols[1]:
	streamlit.image(image)
streamlit.title("Application designed for offline use. Inaccessible online")