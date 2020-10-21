#Imports
import pandas as pd;
import mysql.connector
import matplotlib.pyplot as plt;
import seaborn as sns;

#Database connection
mydb = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              database='wincoop_laravel',
                               );

#Dataframes
locations = pd.read_sql_query("""SELECT * FROM locations""", mydb);
location_meta = pd.read_sql_query("""SELECT * FROM location_meta""", mydb);
course_availability = pd.read_sql_query("""SELECT * FROM course_availability""", mydb);

#Data preparation
course_availability = course_availability.drop(['pontifex_id', 'created_at'], axis=1);

locations = locations[locations.pontifex_active != 1];
locations = locations[locations.pontifex_ids.isnull()];
locations = locations[locations.deleted_at.isnull()];


#Data prediction
course_availability_2 = pd.read_sql_query("""SELECT * FROM course_availability JOIN availability ON course_availability.availability_id=availability.id JOIN locations l on l.id = availability.locations_id WHERE date = '2020-11-10'""", mydb);
course_availability_2 = course_availability_2[course_availability_2.pontifex_ids.isnull()];


plt.scatter(course_availability_2['name'], course_availability_2['spots']);
plt.xticks(rotation=90);
plt.title('2020-11-10');
plt.ylabel('Aantal beschikbare plekken');
plt.xlabel('Locatie');
plt.show();

