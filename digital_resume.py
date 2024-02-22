import streamlit, PIL, streamlit_extras

# General Info
page_title = "Digital CV | Tareq Abbood"
page_icon = ":page_facing_up:"
name = "Tareq Abbood"
email = "Tareq.Abbood@thedeveloper.me"
phone = "+9647731895660"
profile_pic_path = "./assets/profile_pic.png"
footer_pic_path = "./assets/footer_pic.png"
css_file_path = "./styles/main.css"
resume_path = "./assets/resume.pdf"

description = "Aerospace Engineer, assisting enterprises through inovative solutions and by supporting data-driven decision-making."
social_media = {
	"LinkedIn": "https://www.linkedin.com/in/tareq-abbood-087a68105",
	"Github": "https://github.com/TheDeveloper314",
	"Instagram": "https://www.instagram.com/x_tariq/"
}
projects = {
	":trophy: Training Portal - Web app to provide insight into training status and view certificates (click me!)": "https://training-portal-demo.onrender.com",
	":trophy: Agora Menu - Coffee House cloud hosted menu (click me!)": "https://agora-coffee-house.onrender.com",
	":trophy: Finance Dashboard - A dashboard to track varios financial aspects (click me!)": "finance_dashboard",
	":trophy: Reliability Dashboard - Dashboard to provide insight into and analysis of the reliability of various fleets of an airline operator (click me!)": "reliability_dashboard",
	":trophy: Whatsup Hub - An offline app to automate communication through whatsapp. Used for marketing purposes.": "offline_use"
}

def init():
	streamlit.set_page_config(page_title = page_title, page_icon = page_icon, initial_sidebar_state = "collapsed")
	with open(css_file_path) as file:
		streamlit.markdown(f'<style>{file.read()}</style>', unsafe_allow_html = True)
	streamlit.markdown("<style>[data-testid='collapsedControl']{display: none}</style>", unsafe_allow_html = True)

@streamlit.cache_data
def load_images():
	profile_pic = PIL.Image.open(profile_pic_path)
	footer_pic = PIL.Image.open(footer_pic_path)
	return (profile_pic, footer_pic)

def build_hero_section():
	streamlit.markdown("###")
	profile_pic = load_images()[0]
	col1, col2 = streamlit.columns([1, 2], gap = "large")
	with open(resume_path, "rb") as pdf_file:
		pdf = pdf_file.read()
	with col1:
		streamlit.image(profile_pic, width = 200)
	with col2:
		streamlit.title(name)
		streamlit.write(description)
		streamlit.write(":email:", email)
		streamlit.download_button(f"{page_icon} Download CV", pdf, file_name = "Tareq-Abbood-CV.pdf", mime = "application/octet-stream")

def build_social_secion():
	streamlit.markdown("#")
	cols = streamlit.columns(len(social_media.keys()))
	for index, (platform, link) in enumerate(social_media.items()):
		cols[index].subheader(f"[{platform}]({link})")

def build_experience_section():
	streamlit.markdown("#")
	streamlit.subheader("Experience & Qualifications")
	streamlit.write("""
		- :heavy_check_mark: 4 Years experience in the aviation industry.
		- :heavy_check_mark: Hands-on experience in building dashboards using Python, PowerBI, and Excel.
		- :heavy_check_mark: Hands-on experience in building and optimising procedures.
		- :heavy_check_mark: Built Reliability procedures and database for Iraqi Airways.
		- :heavy_check_mark: Experience in project management for and with industry leading companies, such as AirFrance, ALC, and Boeing.
		- :heavy_check_mark: Lead the e-Enabling establishment project in Iraqi Airways (infrastructure, training, roles, and operation management)
		- :heavy_check_mark: Excellent team-player displaying a strong sense of initiative on tasks.
		""")

def build_skills_section():
	streamlit.markdown("#")
	streamlit.subheader("Hard Skills")
	streamlit.write("""
	- :computer: Programming: Python, PyGame, VBA, MatLab.
	- :chart_with_upwards_trend: Visualisation: Streamlit, PowerBI, Excel, Plotly.
	- :lower_left_ballpoint_pen: Modeling: CreoParametric, MeshLess, GMsh, PointWise.
	- :airplane: CFD: ChiDG, Parallel MeshLess, OpenFoam.
	- :desktop_computer: Database: MySQL.
	- :frame_with_picture: Design: Adobe Photoshop.
	- :speaking_head_in_silhouette: Languages: English, Arabic.
	""")

def build_projects_section():
	streamlit.markdown("#")
	streamlit.subheader("Projects & Accomplishements", help = "View a project or a demo of the project by clicking it")
	streamlit.markdown("---")
	for project, link in projects.items():
		streamlit.write(f"[{project}]({link})")

def build_work_history_section():
	streamlit.markdown("#")
	streamlit.subheader("Work History")
	streamlit.markdown("---")

	# Job 1
	streamlit.write(":office: **Technical Training Specialist** | Iraqi Airways Co.")
	streamlit.write("*Baghdad | Iraq*")
	streamlit.write("November-2023 to *Present*")
	with streamlit.expander("View details"):
		streamlit.write("""
			- :scroll: Defining training objectives for the technical department, following up on their implementation and overcoming obstacles.
			- :scroll: The preparation of the annual technical training plan for the technical department.
			- :scroll: Supervising the practical training of engineers and technicians.
			- :scroll: Supervising the review of training costs internally and externally.
			- :scroll: Manage the list of Training Providers and Instructors from evaluating, deleting and adding in coordination with the quality department.
			- :scroll: Managing training records for employees in the technical department.
			""")

	# Job 2
	streamlit.write(":office: **Project Manager** | JAT Tehnika")
	streamlit.write("*Belgrade | Serbia*")
	streamlit.write("May-2023 to November-2023")
	with streamlit.expander("View details"):
		streamlit.write("""
			- :scroll: Monitor and control the flow of the check; ensures milestones; card closure and other established indicators are achieved to ensure the agreed TAT is met.
			- :scroll: Participate and co-ordinates recovery plans between the relevant stakeholders if the TAT / CRS date is at risk or cannot be met.
			- :scroll: Perform re-planning, together with check leader, for each work package, regarding findings or additional customer requests.
			- :scroll: Co-ordinate between all relevant stakeholders to ensure all KPIs and agreed timelines are met
			- :scroll: Cooperate in the analysis of the work package for downtime, workflow, manpower, material, tooling and special processes.
			- :scroll: Organize Daily meetings with customers and ensure positive customer relationships.
			- :scroll: Conducts wash up meetings as part of the continuous improvement program.
			- :scroll: Assure compliance with applicable safety and quality standards.
			- :scroll: Facilitate and drive process improvements, performing risk assessment and managing cost and time constraints together with the process owners.
			- :scroll: Carry out other duties per set procedures to ensure optimum flow and quality of work, and customer satisfaction.
			""")

	# Job 3
	streamlit.write(":office: **Reliability Team Leader** | Iraqi Airways Co.")
	streamlit.write("*Baghdad | Iraq*")
	streamlit.write("August-2022 to November-2023")
	with streamlit.expander("View details"):
		streamlit.write("""
			- :scroll: Management of the Reliability Team to ensure that variations from the operational standards are analyzed, and displayed, and that changes to the maintenance program are substantiated.
			- :scroll: Participation in Reliability Control Board Meetings.
			- :scroll: Liaison with Technical Support Teams, and Technical Services to ensure analysis is carried out.
			- :scroll: Liaison with various Directorates, CAMO, SMS, Operations, Line Maintenance, Base Maintenance, and Workshops to ensure flow of data to the Reliability Team and to further improve data delivery efficiency.
			""")

	# Job 4
	streamlit.write(":office: **e-Enabling Project Manager** | Iraqi Airways Co.")
	streamlit.write("*Baghdad | Iraq*")
	streamlit.write("October-2022 to May-2023")
	with streamlit.expander("View details"):
		streamlit.write("""
			- :scroll: Ensure that Iraqi Airways has the proper facilities, equipment, and training for a successful e-Enabled B737-Max, and B787 Entry into Service.
			- :scroll: Assist in the writing of the e-Enabling Policies and Procedures that ensure a high safety and security standard, and continues airworthiness and availability of the the B737Max and B787 fleets.
			- :scroll: Liaison with Boeing Entry into Service Team to set-up data retrieval procedures, and configure loadable software parts.
			- :scroll: Liaison with Cellular Companies to ensure e-Enabled A/C's connectivity at the required stations.
			- :scroll: Ensure smooth running of e-Enabling operations after Entry into Service.
			""")

	# Job 5
	streamlit.write(":office: **Reliability and Maintenance Program Manager** | Iraqi Airways Co.")
	streamlit.write("*Baghdad | Iraq*")
	streamlit.write("February-2022 to August-2022")
	with streamlit.expander("View details"):
		streamlit.write("""
			- :scroll: Establishment of the Reliability function within Iraqi Airways.
			- :scroll: Participated in the writing of the IAW Reliability Program.
			- :scroll: Writing of the procedures related to reliability reports issuance, and maintenance program revising.
			- :scroll: Management of the Reliability and Maintenance Program Teams to ensure that variations from the operational standards are analyzed, and displayed, and the appropriate adjustments to the maintenance program are carried out.
			- :scroll: Participation in Reliability Control Board Meetings.
			- :scroll: Liaison with Technical Support Teams, and Technical Services to ensure analysis is carried out.
			- :scroll: Liaison with various Directorates, CAMO, SMS, Operations, Line Maintenance, Base Maintenance, and Workshops to ensure flow of data to the Reliability Team and to further improve data delivery efficiency.
			- :scroll: Liaison with Quality Assurance to ensure findings found in new revisions of Aircraft Maintenance Programs are resolved appropriately and in a timely manner.
			- :scroll: Participated in the customisation of the A330 Aircraft Maintenance Program.
			- :scroll: RAMCO Aviation Solutions maintenance Program End-user. Maintaining of the B737-800 Maintenance Program on RAMCO.
			""")

	# Job 6
	streamlit.write(":office: **Maintenance Planning Deputy Manager** | Iraqi Airways Co.")
	streamlit.write("*Baghdad | Iraq*")
	streamlit.write("September-2021 to February-2022")
	with streamlit.expander("View details"):
		streamlit.write("""
			- :scroll: Supervision of IAW Maintenance Planning teams that handle a fleet of 28 Aircrafts, B737-800, B747-400, B777-200, A320-214, A321-231, A330-202, and CRJ-900LR, and problem solving within the unit.
			- :scroll: Liaison with various CAMO units, such as Technical Services, Technical Records, and Technical Library, and various Direcorates within the company, such as, Base Maintenance, Line maintenance, SCM, and Quality Assurance to ensure the Airworthiness of IAW fleet and that maintenance is not delayed.
			- :scroll: Maintenance Forecasting Team leader. Planning Hangar and Line stops to minimise A/Cs downtime. Short-Term, 3 Months, and Long-Term, 3 Years, planning.
			- :scroll: The improvement of the Maintenance Planning Unit's already existing processes and helping in the establishment of new ones, such as the Forecasting system, and material tracking.
			- :scroll: Maintenance planning of an A330-202 A/C. Tracking routine maintenance tasks performed on the A/C, and the tasks to be performed. Producing work packages, and following up on them.
			- :scroll: Participated in the process of receiving the new addition to IAW Fleet, the A220-300. Partook in the workshops done by Airbus Canada for IAW concerning the A220-330, and lead the operator feedback session done by IAW for Airbus Canada.
			""")

	# Job 7
	streamlit.write(":office: **Maintenance Planner** | Iraqi Airways Co.")
	streamlit.write("*Baghdad | Iraq*")
	streamlit.write("June-2021 to September-2021")
	with streamlit.expander("View details"):
		streamlit.write("""
			- :scroll: Maintenance Forecasting Team leader. Planning Hangar and Line stops to minimise A/Cs downtime. Short-Term, 3 Months, and Long-Term, 3 Years, planning.
			- :scroll: Maintenance planning of a B737-800 A/C. Tracking routine maintenance tasks performed on the A/C, and the tasks to be performed. Producing work packages, and following up on them.
			""")

	# Job 8
	streamlit.write(":office: **Line Maintenance Engineer** | Iraqi Airways Co.")
	streamlit.write("*Baghdad | Iraq*")
	streamlit.write("December-2019 to June-2021")
	with streamlit.expander("View details"):
		streamlit.write("""
			- :scroll: Supervised the process of preparing an Aircraft for flight, from the technical point of concern, as well as the arrival process.
			- :scroll: Assisted in performing the Pre-flight, Daily, Weekly, Ramp, and Service checks on different A/C types of IAW Fleet, including B737-800, B747-400, CRJ900, and A320-214.
			- :scroll: Assisted in the troubleshooting of Aircraft's defects, and rectification of such defects.
			- :scroll: Lead the process of Aircraft's Pushback as a part of training.
			""")

def build_academic_history_section():
	streamlit.markdown("#")
	streamlit.subheader("Academic History")
	streamlit.markdown("---")

	# Masters Degree
	streamlit.write(":book: **MSc in Advanced Aerospace Engineering** | University of Liverpool")
	streamlit.write("*Liverpool | United Kingdom*")
	streamlit.write("September-2017 to September-2018")
	with streamlit.expander("View details"):
		streamlit.write("""
			- :books: Masters Project: Analysis of a High Order CFD code for Aircraft Aerodynamics. The project involved the analysis of a high order finite element CFD code. The code was used to obtain a wing's characteristics, NACA2412, such as the coefficients of lift and drag, in the subsonic regime. The results were evaluated against the data obtained from running the same case using an in house finite element code.

			- :blue_book: Modules studied include: Advanced Aerodynamics; Advanced Structural Analysis; Aeroelasticity; Advanced Guidance Systems; Rotorcraft flight; Flight Handling Qualities, Space flight; Entreprise Studies; Risk and Uncertainty; and Capstone Group Project.

			- :green_book: Capstone Group project involved building a fixed-wing UAV. Served as a designer, constructor and head Avionics engineer. Responsibilities included designing and constructing parts of the UAV as well as setting up the autopilot, sensors and the connections between them.

			- :orange_book: Flight Handling Qualities project involved the assessment of XV-15 Tiltrotor in a search and rescue mission in Airplane mode. responsibilities included offline assessment of various Aircraft Handling Qualities in various flight envelopes.

			- :notebook: Served as Flight Engineer in the online testing of the same aircraft, in the University's simulator, by a guest testing pilot.
			""")

	# Bachelors Degree
	streamlit.write(":book: **BSc in Mechanical/Aeronautical Engineering** | University of Baghdad")
	streamlit.write("*Baghdad | Iraq*")
	streamlit.write("September-2012 to September-2016")
	with streamlit.expander("View details"):
		streamlit.write("""
			- :books: Modules studied include: Aerodynamics; internal combustion engines/propulsion engines; aircrafts’ systems and efficiency; Structure of materials; gas dynamics; fluid mechanics and thermodynamics.

			- :blue_book: Participated in the University exhibit for engineering projects two years in a row, the projects being "Dancing Fountain" Group project, Self-built; "Simple Climbing Robot" Group project, Self-built.

			- :green_book: Awarded for being the top student in the aeronautics department in junior year, 2014 - 2015.

			- :orange_book: Awarded for being the third top student in the aeronautics department in senior year, 2015 - 2016.
			""")

def build_workshops_section():
	streamlit.markdown("#")
	streamlit.subheader("Workshops")
	streamlit.markdown("---")

	# Workshop 1
	streamlit.write("Airbus A220 Maintenance Program | Hosted by Airbus Canada")
	streamlit.write("""
		- :white_check_mark: 3 Year Maintenance Forecsats & Long-term Planning.
		- :white_check_mark: Material & Support Equipment planning.
		- :white_check_mark: Check/Task Deviations and Airbus Support.
		- :white_check_mark: Data Collection.
		- :white_check_mark: Scheduled Maintenance.
		""")

	# Workshop 2
	streamlit.write("Airbus A220 Data Collection | Hosted by Airbus Canada")
	streamlit.write("""
		- :white_check_mark: Fleet Performance Introduction.
		- :white_check_mark: Data Sharing.
		- :white_check_mark: AODS Format.
		- :white_check_mark: Data Reports.
		- :white_check_mark: Skywise Analysis.
		""")

def build_courses_section():
	streamlit.markdown("#")
	streamlit.subheader("Courses")
	streamlit.write("""
		- :white_check_mark: Introduction to Engine Fleet Management | Pratt & Whitney.
		- :white_check_mark: Introduction to EngineWise Data | Pratt & Whitney.
		""")

def build_footer_section():
	streamlit.markdown("#")
	streamlit.markdown("---")
	cols = streamlit.columns([2.2, 4, 1])
	with cols[1]:
		streamlit.image(load_images()[1])
	cols = streamlit.columns([1, 4, 1])
	with cols[1]:
		streamlit.subheader("Looking forward to working with you")

def run():
	init()
	build_hero_section()
	build_social_secion()
	build_experience_section()
	build_skills_section()
	build_projects_section()
	build_work_history_section()
	build_academic_history_section()
	build_workshops_section()
	build_courses_section()
	build_footer_section()

if __name__ == "__main__":
	run()