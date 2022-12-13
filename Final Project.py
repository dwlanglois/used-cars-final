"""
Class: CS230--Section 1
Name: Daniel Langlois
Description: This is the master file for my Python Final Project. It contains mostly streamlit programming in
order to present the data. It imports final_functions.py in order to use the functions contained therein. The goal
of this project is to analyze data on used cars for sale on craigslist.
I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
"""
import final_functions
import streamlit as st
from PIL import Image as Image

FILENAME = 'cl_used_cars_7000_sample.csv'
DATAFRAME = final_functions.read_file(FILENAME)

#### VARIABLES ####
# Query 1: Age of cars for sale
age_spread = final_functions.age_of_sale(DATAFRAME)

# Query 2: Robustness of Brands
average_high_miles = final_functions.robust_average(DATAFRAME)
chart100 = final_functions.robust_count_100(DATAFRAME)
chart150 = final_functions.robust_count_150(DATAFRAME)
chart200 = final_functions.robust_count_200(DATAFRAME)

# Query 3: Are these listings real?
selections = final_functions.make_selections(len(DATAFRAME), 10)
records_to_test = final_functions.fetch_records(DATAFRAME, selections)


#### STREAMLIT ####
st.title("Used Cars for Sale on Craigslist")
st.header("CS-230 Final Project")
st.subheader("by Dan Langlois, 2022")
st.write("")
st.sidebar.header("Navigate the page")
with st.sidebar:
    st.sidebar.subheader("Which data would you like to display?")
    csv_data = st.checkbox("CSV Dataframe")
    display_map = st.checkbox("Map")
    dis_charts = st.checkbox("Charts")
    audit = st.checkbox("Audit")
    finals = st.checkbox("Happy Finals")

# Display Dataframe
if csv_data:
    st.write("Use this to verify that the csv loaded into the program matches what you want to examine")
    st.dataframe(DATAFRAME, use_container_width=True)

# Display Map
if display_map:
    st.write("**Location of Used Cars for Sale**")
    st.map(final_functions.mapping(DATAFRAME))

# Display Charts
if dis_charts:
    # Chart / Query 1
    st.write("**When is it most likely someone will sell their car?**")
    st.bar_chart(age_spread)
    

    # Chart / Query 2
    st.write("**Which brands produce the longest lasting cars?**")   
    st.write("*Looking to see how many cars each brand has for sale over a x number of miles*")
    robustness_select = st.selectbox("Select to see the number of cars for sale by each brand with at least 100k, 150k, or 200k miles",
    ('100,000+ Miles', '150,000+ Miles', '200,000+ Miles'), label_visibility="visible")
    
    match robustness_select:
        case '100,000+ Miles':
            st.bar_chart(data=chart100, use_container_width=True)
        case '150,000+ Miles':
            st.bar_chart(data=chart150, use_container_width=True)
        case '200,000+ Miles':
            st.bar_chart(data=chart200, use_container_width=True)

# Display Selections
if audit:
    st.write("**Make random selections to test the Existence Assertion over listings**")
    st.dataframe(records_to_test)

# Happy Finals!
if finals:
    image = Image.open('elf.jpeg')
    st.image(image, caption="WHEN FINALS ARE OVER AND YOU CAN ACTUALLY GET EXCITED FOR CHRISTMAS")

