import streamlit
from digital_resume import *

page_title = "vCard | Tareq Abbood"
page_icon = ":page_facing_up:"
vcf = "./assets/tareq_abbood.vcf"

def init():
	streamlit.set_page_config(page_title = page_title, page_icon = page_icon, initial_sidebar_state = "collapsed")
	with open(css_file_path) as file:
		streamlit.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)
	streamlit.markdown("<style>[data-testid='collapsedControl']{display: none}</style>", unsafe_allow_html = True)

def build_vcard_section():
	streamlit.title(name)
	streamlit.download_button(f"{page_icon} Download Contact Info", vcf, file_name = "Tareq-Abbood.vcf", mime = "application/octet-stream")
	tabs = streamlit.tabs(["Contact", "Social"])
	with tabs[0]:
		streamlit.write(f"Mobile: {phone}")
		streamlit.write(f"Email: {email}")

	with tabs[1]:
		streamlit.write("[Portfolio](https://tareq-abbood-digital-cv.onrender.com)")
		for media, link in social_media.items():
			streamlit.write(f"[{media}]({link})")

def run():
	init()
	build_vcard_section()

if __name__ == "__main__":
	run()