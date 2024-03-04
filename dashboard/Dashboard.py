import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.figure_factory as ff
import streamlit as st
import altair as alt
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image
import os

st.set_page_config(
    page_title="Brazilian E-Commerce Public Dataset",
    page_icon="📊",
)

st.title("Dashboard E-Commerce Dataset")

with st.sidebar:
    selected = option_menu(
        menu_title="DASHBOARD",
        options=["Homepage","Dataset Overview","About"],
        
    )

if selected == "Homepage":
    left_co, cent_co,last_co = st.columns((1,6,1))
    path = os.path.dirname(__file__)
    img_path = path+'/image/image1.png'
    image = Image.open(img_path)
    resized_image = image.resize((1000, 750))
    with cent_co:
        st.image(resized_image )

    col1, col2 = st.columns(2)

    with col1:
        st.write('''This project is an interactive dashboard built using
                 Streamlit. The dashboard uses the Brazilian E-Commerce Public
                 Dataset by Olis as its data source. This dataset contains
                 information about e-commerce transactions in Brazil and
                 provides an overview of online buying trends and patterns in
                 the country.''')
        
    with col2:
        st.write('''In this dashboard, an attractive and interactive data 
                 visualization is created. This visualization will help to 
                 understand various aspects of e-commerce sales in Brazil.''')
        
elif selected == "Dataset Overview":
    st.write('The dataset used is the E-Commerce Public Dataset.')
    st.write('In this dataset contain information that has been collected from transaction in Brazil between 2016 and 2018.')
    st.write("There's few data on this dataset:")
    st.write("- Customers : Contains information about the customer, such as the customer ID, customer name, and customer location (city and state).")
    st.write("- Geolocation : Contains geographic information about city and states in Brazil. It will help to visualize and analysis based on location.")
    st.write("- Order Items : Contains detail information about each item that has been brought from order, such as ID Product, Price, Amount Purchased, etc.")
    st.write("- Orders : Contains information about orders, such as Order ID, Order Status, Date Purchase, Date Approval, Delivery Time")
    
    # Load Data
    path = os.path.dirname(__file__)
    data_path = path+'/../data/'
    customer = pd.read_csv(f'{data_path}customers_dataset.csv')
    geolocation = pd.read_csv(f'{data_path}geolocation_dataset.csv')
    order_items = pd.read_csv(f'{data_path}order_items_dataset.csv')
    order_payments = pd.read_csv(f'{data_path}order_payments_dataset.csv')
    order_reviews = pd.read_csv(f'{data_path}order_reviews_dataset.csv')
    orders = pd.read_csv(f'{data_path}orders_dataset.csv')
    product_category = pd.read_csv(f'{data_path}product_category_name_translation.csv')
    products = pd.read_csv(f'{data_path}products_dataset.csv')
    sellers = pd.read_csv(f'{data_path}sellers_dataset.csv')

    # Making Data Overview
    overview_data = pd.DataFrame({
    "Datasets" : ['customer','geolocation','order_items','order_payments','order_reviews','orders','product_category','products','sellers'],
    
    "nrows" : [len(customer),len(geolocation),len(order_items),len(order_payments),len(order_reviews),len(orders),len(product_category),len(products),len(sellers)],
    
    'ncols' : [customer.shape[1],geolocation.shape[1],order_items.shape[1],order_payments.shape[1],order_reviews.shape[1],orders.shape[1],product_category.shape[1],products.shape[1],sellers.shape[1]],
    
    'NA amount' : [customer.isna().sum().sum(),
                    geolocation.isna().sum().sum(),
                    order_items.isna().sum().sum(),
                    order_payments.isna().sum().sum(),
                    order_reviews.isna().sum().sum(),
                    orders.isna().sum().sum(),
                    product_category.isna().sum().sum(),
                    products.isna().sum().sum(),
                    sellers.isna().sum().sum()],
    
    'NA columns' : [list(customer.columns[customer.isna().sum() > 0]),
                    list(geolocation.columns[geolocation.isna().sum() > 0]),
                    list(order_items.columns[order_items.isna().sum() > 0]),
                    list(order_payments.columns[order_payments.isna().sum() > 0]),
                    list(order_reviews.columns[order_reviews.isna().sum() > 0]),
                    list(orders.columns[orders.isna().sum() > 0]),
                    list(product_category.columns[product_category.isna().sum() > 0]),
                    list(products.columns[products.isna().sum() > 0]),
                    list(sellers.columns[sellers.isna().sum() > 0])]
                                        })
    
    st.dataframe(overview_data)

elif selected == "About":
    left_co, cent_co,last_co = st.columns((1,6,1))
    path = os.path.dirname(__file__)
    img_path = path+'/image/bangkit.png'
    image = Image.open(img_path)
    resized_image = image.resize((1200, 750))
    with cent_co:
        st.image(resized_image, caption='Bangkit Academy 2024 By Google, GoTo, Traveloka \n Source: https://www.dicoding.com/blog/daftar-bangkit-2021/', )
    
    st.write('This project was done in order to participate in the MSIB program at Kampus Merdeka')
    st.write('The name of the activity that I participated in from the MSIB program is Bangkit Academy 2024 By Google, GoTo, Traveloka, which took the Machine Learning learning path.')
    st.write('This Dashboard project is to complete the course organized through the dicoding platform, namely "Belajar Analisis Data dengan Python Course".')
