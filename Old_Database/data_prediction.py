#Imports
import pandas as pd;
import mysql.connector;
import datetime;

#Database connection
mydb = mysql.connector.connect(user='root', password='admin',
                              host='127.0.0.1',
                              database='wincoop_laravel',
                               );


#Variables
customer_lat = 52.48918;
customer_lng = 4.654158;

customer_course = 1;

#Date acceptable range
start_date = '2020-10-25';
date = datetime.datetime.strptime(start_date, '%Y-%m-%d');
end_date = date + datetime.timedelta(days=14);

#Select course availability data
query = """SELECT * FROM course_availability JOIN availability ON course_availability.availability_id=availability.id JOIN locations l on l.id = availability.locations_id WHERE spots_taken is not null AND spots != 0 AND date between %s AND %s""";
course_availability = pd.read_sql_query(query, mydb, params=[start_date, end_date]);

#Select locations data
location_df = pd.read_sql_query("""SELECT * FROM locations JOIN location_meta ON locations.id=location_meta.locations_id WHERE pontifex_ids IS NOT NULL AND pontifex_active = 1 AND status = "PUBLISHED" """, mydb);
query = """SELECT ROUND(6371 * acos(cos(radians(%s)) * cos(radians(lat)) * cos(radians(lng) - radians(%s)) + sin(radians(%s)) * sin(radians(lat)))) as distance,lat,lng,city,locations_id from location_meta HAVING distance<=30  order by distance""";
closest_locations = pd.read_sql_query(query, mydb, params=[customer_lat, customer_lng, customer_lat]);

#Remove pontifex locations
for x in location_df.id:
    closest_locations = closest_locations[closest_locations.locations_id != x];

#Create DataFrame with nearest locations
d = [];
for x in closest_locations.locations_id:
    b = course_availability[course_availability.locations_id == x];
    d.append(b);

available_locations = pd.concat(d);
print(available_locations);