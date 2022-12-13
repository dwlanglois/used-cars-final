"""This file contains all the functions that will be used in my final project. These functions
are kept separately because the main file will include only the streamlit code and this file is for the
back end code."""

import pandas as pd
import random as r


def read_file(filename='cl_used_cars_7000_sample.csv'):  # has a default parameter but not in use
    df = pd.read_csv(filename, engine="pyarrow")
    return df


### Map Function ###
def mapping(dataframe):
    df = dataframe[['lat', 'long']]
    df = df[(df.lat > 0) & (df.long <-57)]
    df.dropna(axis=0, inplace=True, how='any')
    df = df.rename(columns={'lat': 'latitude', 'long': 'longitude'})
    return df


#### QUERY 1 FUNCTIONS ####
def age_of_sale(data_frame):
    daf = data_frame[['year', 'id']]
    daf = daf[(daf.year >= 2000)]
    daf['year'] = daf['year'].astype(int)
    daf['year'] = daf['year'].astype(str)
    daf = daf.groupby(['year'])['id'].count()
    return daf


#### QUERY 2 FUNCTIONS ####
# NOTE ON ROBUST: internet indicates that 300k miles is basically the maximum age of a car, with the number of vehicles
#     over that are exceedingly rare and/or rebuilt into a new car. I choose 400k to eliminate unreliable data. And at
#     least 100_000 miles because I only care about cars nearing the end of their lifespan.
def robust_average(data_frame):
    daf = data_frame[['id', 'manufacturer', 'odometer']]   # records with odometer NaN are omitted
    daf = daf[(daf.odometer <= 400_000) & (daf.odometer >= 150_000) & (daf.manufacturer != "")]
    daf2 = daf.groupby('manufacturer').agg(mean_odometer=('odometer', 'mean'),
                                           max_odometer=('odometer', 'max'))
    daf2.rename(columns={'mean_odometer': 'Average Mileage'
                         , 'max_odometer': 'Highest Mileage'}, inplace=True)
    return daf2.sort_values(['Average Mileage'], ascending=False)


def robust_count_100(data_frame):
    daf = data_frame[['manufacturer', 'odometer']]   # records with odometer NaN are omitted
    daf = daf[(daf.odometer <= 400_000) & (daf.odometer >= 100_000) & (daf.manufacturer != "")]
    daf.dropna(subset = "manufacturer", inplace=True)
    daf100 = daf.groupby('manufacturer').agg(count_manufacturer=('manufacturer', 'count'))
    daf100.rename(columns={'count_manufacturer': 'Count of listings with >100,000 miles'}, inplace=True)
    return daf100.sort_values(['Count of listings with >100,000 miles'], ascending=False)


def robust_count_150(data_frame):
    daf = data_frame[['manufacturer', 'odometer']]
    daf = daf[(daf.odometer <= 400_000) & (daf.odometer >= 150_000) & (daf.manufacturer != "")]
    daf150 = daf.groupby('manufacturer').agg(count_manufacturer=('manufacturer', 'count'))
    daf150.rename(columns={'count_manufacturer': 'Count of listings with >150,000 miles'}, inplace=True)
    return daf150.sort_values(['Count of listings with >150,000 miles'], ascending=False)


def robust_count_200(data_frame):
    daf = data_frame[['manufacturer', 'odometer']]
    daf = daf[(daf.odometer <= 400_000) & (daf.odometer >= 200_000) & (daf.manufacturer != "")]
    daf200 = daf.groupby('manufacturer').agg(count_manufacturer=('manufacturer', 'count'))
    daf200.rename(columns={'count_manufacturer': 'Count of listings with >200,000 miles'}, inplace=True)
    return daf200.sort_values(['Count of listings with >200,000 miles'], ascending=False)


#### QUERY 3 FUNCTIONS ####
def make_selections(index_range, count):
    selections_set = set()
    while len(selections_set) < count:      # loop that iterates through items in the set
        x = r.randint(0, index_range)
        selections_set.add(x)
    selections = list(selections_set)       # This code uses a set, and a list
    return selections


def fetch_records(dataf, selections):
    daf = dataf.iloc[selections]
    ret_daf = daf[['url', 'description']]
    return ret_daf


