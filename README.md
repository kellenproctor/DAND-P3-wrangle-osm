# P3: Wrangle OpenStreetMap Data
## Udacity Data Analyst NanoDegree
___
### Files included in this Github Repository

#### Data Directory

Name | K value | Size | Lines | Note
---|---:|---:|---:|---|
*la-sample.osm* | 1,000 | 8.6 MB | 110,729 | This file was used to test early python data auditing and cleaning scripts.
*la-small.osm.json* |  | 9.7 MB | 41,124 | Result of running data_converter.py, imported into the MongoDB database.

#### Code Directory

Name | Description
---|---
audit.py | Returns a list of **tag** "k" values for **nodes**. To explore **ways** please change the file path in the main call.
data_converter.py | Cleans, shapes, and converts the xml files to json
data_structure.py | A more complex form of map_parser.py, which includes the children counts for each node type.
map_parser.py | Prints a dictionary of the node types, their counts, and attributes
sample.py | Provided in the project prep for making a smaller file from the original OSM dataset

#### Root Directory

Name | Description
---|---
mapdata.txt | A text file containing a link to the map position you wrangled in your project, a short description of the area and a reason for your choice.
P3_Wrangling_OSM_data.ipynb | Jupyter Notebook containing my Project Submission
P3_Wrangling_OSM_data-v-1.html | The html version of the notebook, for your review
query.py | a Python script for querying the MongoDB database, can be called from the command line, please read comments in script, and critique for improvements!
README.md | What you're reading

#### Resources Used
Can be found at the end of the html submission