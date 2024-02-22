import streamlit, PIL
from digital_resume import init

images_names = {"Summary":"The main page. Shows the total amount of funds available, gross income and withdrawls over time, and various totals.",
				"Breakdown":"A breakdown of the expenditures over a period of time grouped by category, and the daily total amount spent. A graph showing the discrepancy between calculated and actual values is used to indicate the reliability of the calculations.", 
				"Trend Analysis":"Graphs showing the cumulative expenditure as well as the expenditure rate.", 
				"PpI_Item1":"A graph to provide analysis of similar items. The Grpah shows the price of a unit of an item from different brands providing insight into the most cheapest and most expensive brand of the same item.", 
				"PpI_Item2":"A graph to provide analysis of similar items. The Grpah shows the price of a unit of an item from different brands providing insight into the most cheapest and most expensive brand of the same item.", 
				"PpI_Item3":"A graph to provide analysis of similar items. The Grpah shows the price of a unit of an item from different brands providing insight into the most cheapest and most expensive brand of the same item."}

@streamlit.cache_data
def load_images():
	images = {}
	for image in images_names.keys():
		images[image] = PIL.Image.open(f"./assets/finance_dashboard/{image}.png")
	return images

def build_main_page():
	images = load_images()
	streamlit.markdown("#")
	streamlit.header("Finance Dashboard", help ="USD and Serbian Din.")
	streamlit.write("Proof that small steps can lead to unexpected results. What started out as a simple spreadsheet to track financial transactions turned into a fully functioning, cross-platform dashboard that provides insight into the details of the finances of an individual or an entity.")
	streamlit.markdown("---")
	for image, data in images.items():
		streamlit.subheader(image)
		streamlit.write(images_names[image])
		streamlit.markdown("###")
		with streamlit.container(border = True):
			streamlit.image(data)
		streamlit.markdown("###")
		streamlit.markdown("---")

def run():
	init()
	build_main_page()

run()