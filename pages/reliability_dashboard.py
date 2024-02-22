import streamlit, PIL
from digital_resume import init

images_B737_titles = ["General Information B737", "Utilisation B737", "System Reliability B737", "AC Systems B737"]
images_CRJ_titles = ["General Information CRJ", "Utilisation CRJ", "System Reliability CRJ", "AC Systems CRJ"]
titles = {
		"General Information": "The summary page. Shows the main KPIs that indicate the fleet's performance.",
		"Utilisation": "Shows the utilisation of the fleet in terms of flight hours per day, and flight cycles per day over a period of time (annual).",
		"System Reliability": "The occurences in the various systems of the fleet, and the rate at which they occur. This table is the main element in determining the alert level (which indicates which system is to be placed on watch, and which system is to be actioned on).",
		"Aircraft Systems": "A breakdown of the occurences based on Registration and System. These graphs show the distribution of occurencs on the fleet and also provide more insight into the systems' reliability."
		}

@streamlit.cache_data
def load_images(fleet_images):
	images = [PIL.Image.open(f"./assets/reliability_dashboard/{image}.png") for image in fleet_images]
	return images

def build_main_page():
	images_B737 = load_images(images_B737_titles)
	images_CRJ = load_images(images_CRJ_titles)
	streamlit.markdown("#")
	streamlit.header("Reliability Dashboard")
	streamlit.write("A dashboard to provide insight into the reliability of an airlines' fleet and support data-driven decision-making. The dashboard relies on statistical, historical, and operational methods to indicate when and on what an action needs to be taken to improve the overall reliability of the fleet.")
	streamlit.markdown("---")
	for index, image in enumerate(images_B737_titles):
		streamlit.subheader(list(titles.keys())[index])
		streamlit.write(titles[list(titles.keys())[index]])
		streamlit.markdown("###")
		with streamlit.container(border = True):
			streamlit.write("B737")
			streamlit.image(images_B737[index])
			streamlit.markdown("###")
			streamlit.write("CRJ")
			streamlit.image(images_CRJ[index])
		streamlit.markdown("###")


def run():
	init()
	build_main_page()

run()