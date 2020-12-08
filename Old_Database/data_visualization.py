#Imports
import pandas as pd;
import matplotlib.pyplot as plt;

#Dataframes
course_availability = pd.read_csv("../data/course_availability.csv");
locations = pd.read_csv("data/locations.csv");
location_meta = pd.read_csv("data/location_meta.csv");

#Data preparation
course_availability = course_availability.drop(['pontifex_id', 'created_at'], axis=1);

locations = locations[locations.pontifex_active != 1];
locations = locations[locations.pontifex_ids.isnull()];
locations = locations[locations.deleted_at.isnull()];

location_meta = location_meta.drop(['content', 'extras', 'phone', 'email', 'email_attachment', 'created_at', 'updated_at'], axis=1);
location_meta = location_meta[location_meta.persons != 0];




