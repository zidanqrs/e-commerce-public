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
    page_title="Total Orders",
)

# Load Data
st.title("E-Commerce Total Orders")
path = os.path.dirname(__file__)
orders_path = path+'/../orders_dataset.csv'
orders = pd.read_csv(orders_path)
payment_path = path+'/../order_payments_dataset.csv'
order_payments = pd.read_csv(payment_path)

# Define Helper Function
def change_to_datetime(df,columns):
    temp = df

    if type(columns) == type(list()):
        for cols in columns:
            temp[cols] = [pd.Timestamp(x) for x in temp[cols]]
    else:
        temp[columns] = [pd.Timestamp(x) for x in temp[columns]]

    return temp

def to_year_month(date):
    return date.strftime('%b-%Y')

def get_time_of_day(input_time):
    hour = input_time.hour

    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Day'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

# Preprocessing and Cleaning Data
orders_merge = pd.merge(orders, order_payments, how = 'inner',on = 'order_id')
orders_date_cols = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']
orders_merge = change_to_datetime(orders_merge, orders_date_cols)
orders_merge['Year'] = [x.year for x in orders_merge['order_purchase_timestamp']]


with st.sidebar:
    selected = option_menu(
        menu_title="Year",
        options=["2016","2017","2018", "All"],
    )

if selected == '2016':
    orders_2016 = orders_merge[orders_merge['Year'] == 2016]

    order_time_of_day = [get_time_of_day(x) for x in orders_2016['order_purchase_timestamp']]
    day_orders = [x.day_name() for x in orders_2016['order_purchase_timestamp']]

    order_time_of_day_series = pd.Series(order_time_of_day)
    day_orders_series = pd.Series(day_orders)

    col1,col2=st.columns([10,10])

    with col1:
        col1.success('First')
        fig1 = go.Figure()

        fig1 = px.histogram(day_orders_series,  
        category_orders={'x': day_orders_series.value_counts().index},
        labels={'x': 'Order Status', 'y': 'Count'})

        fig1.update_layout(
        title='Histogram of Order Status in 2016',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        col1.plotly_chart(fig1,use_container_width=True)

    with col2:
        col2.success('Second')
        fig2 = go.Figure()

        fig2 = px.histogram(day_orders_series,  
        category_orders={'x': day_orders_series.value_counts().index},
        labels={'x': 'Order Status', 'y': 'Count'})

        fig2.update_layout(
        title='Histogram of Order Status in 2016',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        col2.plotly_chart(fig2,use_container_width=True)
        