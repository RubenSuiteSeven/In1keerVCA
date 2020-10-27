#Imports
import pandas as pd;
import mysql.connector;
import pandasql as ps;
import matplotlib.pyplot as plt;
import seaborn as sns;

#Database connection
mydb = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              database='wincoop_laravel',
                               );


#Variables
customer_lat = 52.3953334;
customer_lng = 4.9493602;
customer_course = 1;
date = '10-01-20';

#Dataframes
locations = pd.read_sql_query("""SELECT * FROM locations""", mydb);
location_meta = pd.read_sql_query("""SELECT * FROM location_meta""", mydb);
course_availability = pd.read_sql_query("""SELECT * FROM course_availability""", mydb);

#Data preparation
locations = locations[locations.pontifex_active != 1];
locations = locations[locations.pontifex_ids.isnull()];
locations = locations[locations.deleted_at.isnull()];

course_availability = course_availability[course_availability.pontifex_id.isnull()];

#Data prediction
# course_availability_2 = pd.read_sql_query("""SELECT * FROM course_availability JOIN availability ON course_availability.availability_id=availability.id JOIN locations l on l.id = availability.locations_id WHERE courses_id = 1 AND spots_taken is not null order by date""", mydb);
# course_availability_2 = course_availability_2[course_availability_2.pontifex_ids.isnull()];

#Remove pontifex locations
location_df = pd.read_sql_query("""SELECT * FROM locations JOIN location_meta ON locations.id=location_meta.locations_id WHERE pontifex_ids IS NULL AND pontifex_active = 0 AND status = "PUBLISHED" """, mydb);

#Distance locations
query = """SELECT ROUND(6371 * acos(cos(radians(%s)) * cos(radians(lat)) * cos(radians(lng) - radians(%s)) + sin(radians(%s)) * sin(radians(lat)))) as distance,lat,lng,city,locations_id from location_meta HAVING distance<=20  order by distance""";
closest_locations = pd.read_sql_query(query, mydb, params=[customer_lat, customer_lng, customer_lat]);
print(closest_locations);

for x in location_df.id:
    closest_locations.drop[closest_locations[closest_locations.locations_id] == x]
