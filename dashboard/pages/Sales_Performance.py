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
    page_title="Sales Performance",
)

# Load Data
st.title("E-Commerce Sales Performance")
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

if selected == "2016":
    orders_2016 = orders_merge[orders_merge['Year'] == 2016]
    orders_2016['year_month'] =orders_2016['order_purchase_timestamp'].apply(to_year_month)
    orders_2016['year_month'] = pd.to_datetime(orders_2016['year_month'], format='%b-%Y')
    total_order =orders_2016['year_month'].value_counts().sort_index().reset_index()
    total_order.columns = ['Date', 'Count']
    total_order['Date'] = total_order['Date'].apply(to_year_month)
    total_income = orders_2016[['year_month', 'payment_value']].groupby(by='year_month').sum().sort_index().reset_index()
    total_income['year_month'] = total_income['year_month'].apply(to_year_month)

    col1, col2 = st.columns(2)

    with col1:
        n_orders = orders_2016['order_status'].count()
        st.metric("Total orders", value=n_orders)
    
    #with col2:
    #    total_revenue = format_currency(tingkat_penjualan_2016.payment_value.sum(), "AUD", locale='es_CO') 
     #   st.metric("Total Revenue", value=total_revenue)

    with st.container():
        fig1 = go.Figure()

        fig1 = px.histogram(orders_2016['order_status'],  
             category_orders={'order_status': orders['order_status'].value_counts().index},
             labels={'order_status': 'Status', 'count': 'Count'})

        fig1.update_layout(
            title='Histogram of Order Status in 2016',
            xaxis_title='Order Status',
            yaxis_title='Count',
            template='plotly_white',
        )

        st.plotly_chart(fig1)

  
    with st.container():
        fig2 = go.Figure()

        fig2 = px.line(total_order, x="Date", y="Count")
        
        fig2.update_layout(
            title='Total Orders E-Commerce in 2016',
            xaxis_title='Date',
            yaxis_title='Count',
            template='plotly_white',
        )

        st.plotly_chart(fig2)

    with st.container():
        fig3 = go.Figure()

        fig3 = px.line(total_income, x="year_month", y="payment_value")
        
        fig3.update_layout(
            title='Total Income E-Commerce in 2016-2018',
            xaxis_title='Date',
            yaxis_title='Income',
            template='plotly_white',
        )

        st.plotly_chart(fig3)

elif selected == "2017":
    orders_2017 = orders_merge[orders_merge['Year'] == 2017]
    orders_2017['year_month'] =orders_2017['order_purchase_timestamp'].apply(to_year_month)
    orders_2017['year_month'] = pd.to_datetime(orders_2017['year_month'], format='%b-%Y')
    total_order =orders_2017['year_month'].value_counts().sort_index().reset_index()
    total_order.columns = ['Date', 'Count']
    total_order['Date'] = total_order['Date'].apply(to_year_month)
    total_income = orders_2017[['year_month', 'payment_value']].groupby(by='year_month').sum().sort_index().reset_index()
    total_income['year_month'] = total_income['year_month'].apply(to_year_month)

    col1, col2 = st.columns(2)

    with col1:
        n_orders = orders_2017['order_status'].count()
        st.metric("Total orders", value=n_orders)

    with st.container():
        fig1 = go.Figure()

        fig1 = px.histogram(orders_2017['order_status'],  
             category_orders={'order_status': orders['order_status'].value_counts().index},
             labels={'order_status': 'Status', 'count': 'Count'})

        fig1.update_layout(
            title='Histogram of Order Status in 2017',
            xaxis_title='Order Status',
            yaxis_title='Count',
            template='plotly_white',
        )

        st.plotly_chart(fig1)

    with st.container():
        fig2 = go.Figure()

        fig2 = px.line(total_order, x="Date", y="Count")
        
        fig2.update_layout(
            title='Total Orders E-Commerce in 2017',
            xaxis_title='Date',
            yaxis_title='Count',
            template='plotly_white',
        )

        st.plotly_chart(fig2)

    with st.container():
        fig3 = go.Figure()

        fig3 = px.line(total_income, x="year_month", y="payment_value")
        
        fig3.update_layout(
            title='Total Income E-Commerce in 2016-2018',
            xaxis_title='Date',
            yaxis_title='Income',
            template='plotly_white',
        )

        st.plotly_chart(fig3)

elif selected == "2018":
    orders_2018 = orders_merge[orders_merge['Year'] == 2018]
    orders_2018['year_month'] =orders_2018['order_purchase_timestamp'].apply(to_year_month)
    orders_2018['year_month'] = pd.to_datetime(orders_2018['year_month'], format='%b-%Y')
    total_order = orders_2018['year_month'].value_counts().sort_index().reset_index()
    total_order.columns = ['Date', 'Count']
    total_order['Date'] = total_order['Date'].apply(to_year_month)
    total_income = orders_2018[['year_month', 'payment_value']].groupby(by='year_month').sum().sort_index().reset_index()
    total_income['year_month'] = total_income['year_month'].apply(to_year_month)

    col1, col2 = st.columns(2)

    with col1:
        n_orders = orders_2018['order_status'].count()
        st.metric("Total orders", value=n_orders)

    with st.container():
        fig1 = go.Figure()

        fig1 = px.histogram(orders_2018['order_status'],  
             category_orders={'order_status': orders['order_status'].value_counts().index},
             labels={'order_status': 'Status', 'count': 'Count'})

        fig1.update_layout(
            title='Histogram of Order Status in 2018',
            xaxis_title='Order Status',
            yaxis_title='Count',
            template='plotly_white',
        )

        st.plotly_chart(fig1)

    with st.container():
        fig2 = go.Figure()

        fig2 = px.line(total_order, x="Date", y="Count")
        
        fig2.update_layout(
            title='Total Orders E-Commerce in 2018',
            xaxis_title='Date',
            yaxis_title='Count',
            template='plotly_white',
        )

        st.plotly_chart(fig2)

    with st.container():
        fig3 = go.Figure()

        fig3 = px.line(total_income, x="year_month", y="payment_value")
        
        fig3.update_layout(
            title='Total Income E-Commerce in 2016-2018',
            xaxis_title='Date',
            yaxis_title='Income',
            template='plotly_white',
        )

        st.plotly_chart(fig3)

elif selected == "All":
    orders_all = orders_merge
    orders_all['year_month'] =orders_all['order_purchase_timestamp'].apply(to_year_month)
    orders_all['year_month'] = pd.to_datetime(orders_all['year_month'], format='%b-%Y')
    total_order =orders_all['year_month'].value_counts().sort_index().reset_index()
    total_order.columns = ['Date', 'Count']
    total_order['Date'] = total_order['Date'].apply(to_year_month)
    total_income = orders_all[['year_month', 'payment_value']].groupby(by='year_month').sum().sort_index().reset_index()
    total_income['year_month'] = total_income['year_month'].apply(to_year_month)

    col1, col2 = st.columns(2)

    with col1:
        n_orders = orders_all['order_status'].count()
        st.metric("Total orders", value=n_orders)

    with st.container():
        fig1 = go.Figure()

        fig1 = px.histogram(orders_all['order_status'],
             category_orders={'order_status': orders['order_status'].value_counts().index},
             labels={'order_status': 'Status', 'count': 'Count'})

        fig1.update_layout(
            title='Histogram of Order Status in 2016-2018',
            xaxis_title='Order Status',
            yaxis_title='Count',
            template='plotly_white',
        )

        st.plotly_chart(fig1)

    with st.container():
        fig2 = go.Figure()

        fig2 = px.line(total_order, x="Date", y="Count")
        
        fig2.update_layout(
            title='Total Orders E-Commerce in 2016-2018',
            xaxis_title='Date',
            yaxis_title='Count',
            template='plotly_white',
        )

        st.plotly_chart(fig2)

    with st.container():
        fig3 = go.Figure()

        fig3 = px.line(total_income, x="year_month", y="payment_value")
        
        fig3.update_layout(
            title='Total Income E-Commerce in 2016-2018',
            xaxis_title='Date',
            yaxis_title='Income',
            template='plotly_white',
        )

        st.plotly_chart(fig3)

