# Imports
import pandas as pd;
import mysql.connector;
import datetime;

# Database connection
mydb = mysql.connector.connect(user='root', password='admin',
                               host='127.0.0.1',
                               database='wincoop_vca',
                               );

# Variables
customer_lat = 52.48918;
customer_lng = 4.654158;
distance = 30;
customer_course = 1;
date_range = 14;

# Date acceptable range
start_date = '2020-10-25';
date = datetime.datetime.strptime(start_date, '%Y-%m-%d');
end_date = date + datetime.timedelta(days=date_range);

# Select planning where spots_taken has values and spots is not 0
query = """SELECT * FROM planning WHERE spots_taken is not null AND spots != 0 AND date between %s AND %s""";
planning = pd.read_sql_query(query, mydb, params=[start_date, end_date]);

# Select the location information corresponding with the variables
query = """SELECT ROUND(6371 * acos(cos(radians(%s)) * cos(radians(lat)) * cos(radians(lng) - radians(%s)) + sin(radians(%s)) * sin(radians(lat)))) as distance,lat,lng,city,locations_id from location_meta HAVING distance<=(%s)  order by distance""";
closest_locations = pd.read_sql_query(query, mydb, params=[customer_lat, customer_lng, customer_lat, distance]);

# Create DataFrame with nearest locations
d = [];
for x in closest_locations.locations_id:
    b = planning[planning.locations_id == x];
    d.append(b);

available_locations = pd.concat(d);
print(available_locations);
