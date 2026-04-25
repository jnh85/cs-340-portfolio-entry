Justin Hardin
CS 340 Client/Server Development
Project Two README
April 19, 2026

Grazioso Salvare Dashboard

Description
The Grazioso Salvare Dashboard is a web application that helps Grazioso Salvare, an international rescue-animal training company, identify dogs that are suitable for search and rescue training from the Austin Animal Center Outcomes data set. The dashboard uses shelter data from a MongoDB database and presents it through an interface that is interactive and filterable. Certain breeds excel at certain rescue missions, and this dashboard allows the user to narrow down thousands of records to the specific dogs that match the intended criteria.
The application uses the Model-View-Controller pattern, where MongoDB serves as the model, the dashboard layout serves as the view, and the CRUD Python module, along with the callback functions serve as the controller tying everything together.

Features
-	Interactive radio filter with four options: Water Rescue, Mountain or Wilderness Rescue, Disaster or Individual Tracking, and Reset (no filter)
-	Paginated, filterable, and sortable data table that updates in real time to the currently selected rescue type
-	Pie chart that shows the breeds of whatever rows are currently visible in the table
-	Interactive Leaflet geolocation map with a tooltip and popup for the currently selected animal

Tech Stack
-	Python 3 – the programming language used for development
-	MongoDB – NoSQL database serving as the Model
-	PyMongo – MongoDB driver for Python. It is used in the CRUD Python module
-	Dash – the web application framework
-	Dash-Leaflet – Dash components for the geolocation map
-	Plotly Express – Provides the pie chart in the dashboard
-	Pandas – works with MongoDB to present the query results in a dictionary of records

MongoDB stores data flexibly, which is convenient for our project because each animal record contains a mix of required fields and optional fields. PyMongo returns query results as Python dictionaries that convert directly to pandas data frames and then into the row of dictionaries format the Dash data table needs. This does a lot of the heavy lifting because developers don’t have to do the conversion themselves. MongoDB has handy query operators like $in for breed lists and $gte/$lte for age ranges. This makes filtering very easy. MongoDB also has role-based authentication, working well to support the aacuser account.
Dash is a Python web application framework. It lets a developer develop the entire front end and the behavior behind it using nothing but Python code. In this project, app.layout is composed of HTML, Core, DataTable, and Leaflet components and presents it into the user interface, while the functions using @app.callback connect the user input to the component outputs. The CRUD Python Module is called from inside those callbacks to query MongoDB.

Visuals
The screenshots below demonstrate the functionality of the web app. Each screenshot shows the different states of the web app based on which of the various filters are selected.

Starting State
<img width="986" height="650" alt="image" src="https://github.com/user-attachments/assets/5965f5aa-8af5-4495-9ec3-6705f529908c" />


Water Rescue Filter
<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/85ea4f6b-e0f2-487f-953a-c7967fa8f896" />


Mountain or Wilderness Rescue Filter
<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/67dddf16-c3f1-428d-9ccc-6f55446c8190" />


Disaster or Individual Tracking Filter
<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/17a39f26-df7c-482d-acaa-e4681fa9e434" />


Reset (no filter)
<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/7d6e1ba3-5e72-445b-ad9c-9a3c71192069" />


Usage
To launch the dashboard, follow the steps below.
1.	Open ProjectTwoDashboard.ipynb in Jupyter Notebook
2.	Confirm that “username” and “password” match your MongoDB user. Update them if necessary.
3.	Run every cell in the Notebook
4.	Click the resulting URL at the bottom to open the dashboard in your browser

To use the dashboard, see the points below.
-	Select one of the four radio button options to filter the data: Water Rescue, Mountain or Wilderness Rescue, Disaster or Individual Tracking, or Reset.
-	The data table, pie chart, and map update automatically, reflecting the currently selected filter.
-	Sort the data table by clicking any column header. Filter individual columns using the per-column filter boxes.
-	Click a row’s radio button to highlight that animal on the geolocation map. The tooltip shows the breed and the popup shows the animal’s name.
-	Click the Grazioso Salvare logo at the top of the page to open the client home page in a new tab.

Development
Below are the steps that were taken to build the project.
1.	Review the Dashboard Specifications Document to confirm the breed, sex, and age criteria for each rescue type.
2.	Import the CRUD Python Module from Project One, which provides the create, read, update, and delete operations for the animals collection.
3.	Establish the MongoDB connections from the notebook by instantiating the AnimalShelter class with the aacuser credentials.
4.	Populate the initial data frame with db.read() and drop the non-serializable _id column.
5.	Design the Dash layout, making sure to include the logo that hyperlinks to snhu.edu, unique identifier, radio button filter, DataTable, pie chart, and geolocation map.
6.	Implement the filter callback, mapping each radio button value to a MongoDB query that uses $in for breed lists and $gte/$lte for age ranges.
7.	Implement the pie chart callback so that chart content always matches the rows in the data table.
8.	Implement the map callback that places a marker at the selected animal’s location.
9.	Iterate through running the notebook, testing, debugging, and verifying proper functionality.
 
There were some challenges along the way during development. It took several iterations of testing and tweaking the code to get the layout and results that I wanted. Fortunately, the challenges I faced were minor and could be overcome through trial and error, as well as applying what I learned from the previous milestone assignment along with the feedback that came from it. This project was a fun one to undertake, and it was a valuable learning experience.

Resources
Dash: https://dash.plotly.com/
MongoDB: https://www.mongodb.com/docs/
PyMongo: https://pymongo.readthedocs.io/en/stable/
Pandas: https://pandas.pydata.org/docs/
README template: https://www.makeareadme.com/

