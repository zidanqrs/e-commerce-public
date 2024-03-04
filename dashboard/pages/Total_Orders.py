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
orders_merge['Month'] = [x.month_name() for x in orders_merge['order_purchase_timestamp']]

custom_month_order = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]


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

    month_count_df = pd.DataFrame({
    'Month' : orders_2016['Month'],
    'Year' : orders_2016['Year']
    })

    month_count_df['Month'] = pd.Categorical(month_count_df['Month'], categories=custom_month_order, ordered=True)
    sorted_month_count_df = month_count_df[month_count_df['Year'] == 2016].sort_values(['Year', 'Month'])
    sorted_month_count_df = sorted_month_count_df.sort_values('Month')

    col1,col2=st.columns([10,10])

    with col1:
        fig1 = go.Figure()

        fig1 = px.histogram(day_orders_series,  
        category_orders={'x': day_orders_series.value_counts().index},
        labels={'x': 'Order Status', 'y': 'Count'})

        fig1.update_layout(
        title='Total Orders by Day of Week in 2016',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        col1.plotly_chart(fig1,use_container_width=True)

    with col2:
        fig2 = go.Figure()

        fig2 = px.histogram(day_orders_series,  
        category_orders={'x': day_orders_series.value_counts().index},
        labels={'x': 'Order Status', 'y': 'Count'})

        fig2.update_layout(
        title='Total Orders by Time of Day in 2016',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        col2.plotly_chart(fig2,use_container_width=True)

    with st.container():
        fig3 = go.Figure()

        fig3 = px.histogram(sorted_month_count_df['Month'],  
        category_orders={'x': sorted_month_count_df['Month'].value_counts().index},
        labels={'x': 'Month', 'y': 'Count'})
        
        fig3.update_layout(
        title='Total Orders by Month of Years in 2016',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        st.plotly_chart(fig3,use_container_width=True)

if selected == '2017':
    orders_2017 = orders_merge[orders_merge['Year'] == 2017]

    order_time_of_day = [get_time_of_day(x) for x in orders_2017['order_purchase_timestamp']]
    day_orders = [x.day_name() for x in orders_2017['order_purchase_timestamp']]

    order_time_of_day_series = pd.Series(order_time_of_day)
    day_orders_series = pd.Series(day_orders)

    month_count_df = pd.DataFrame({
    'Month' : orders_2017['Month'],
    'Year' : orders_2017['Year']
    })

    month_count_df['Month'] = pd.Categorical(month_count_df['Month'], categories=custom_month_order, ordered=True)
    sorted_month_count_df = month_count_df[month_count_df['Year'] == 2017].sort_values(['Year', 'Month'])
    sorted_month_count_df = sorted_month_count_df.sort_values('Month')

    col1,col2=st.columns([10,10])

    with col1:
        fig1 = go.Figure()

        fig1 = px.histogram(day_orders_series,  
        category_orders={'x': day_orders_series.value_counts().index},
        labels={'x': 'Order Status', 'y': 'Count'})

        fig1.update_layout(
        title='Total Orders by Day of Week in 2017',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        col1.plotly_chart(fig1,use_container_width=True)

    with col2:
        fig2 = go.Figure()

        fig2 = px.histogram(day_orders_series,  
        category_orders={'x': day_orders_series.value_counts().index},
        labels={'x': 'Order Status', 'y': 'Count'})

        fig2.update_layout(
        title='Total Orders by Time of Day in 2017',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        col2.plotly_chart(fig2,use_container_width=True)

    with st.container():
        fig3 = go.Figure()

        fig3 = px.histogram(sorted_month_count_df['Month'],  
        category_orders={'x': sorted_month_count_df['Month'].value_counts().index},
        labels={'x': 'Month', 'y': 'Count'})
        
        fig3.update_layout(
        title='Total Orders by Month of Years in 2017',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        st.plotly_chart(fig3,use_container_width=True)

if selected == '2018':
    orders_2018 = orders_merge[orders_merge['Year'] == 2018]

    order_time_of_day = [get_time_of_day(x) for x in orders_2018['order_purchase_timestamp']]
    day_orders = [x.day_name() for x in orders_2018['order_purchase_timestamp']]

    order_time_of_day_series = pd.Series(order_time_of_day)
    day_orders_series = pd.Series(day_orders)

    month_count_df = pd.DataFrame({
    'Month' : orders_2018['Month'],
    'Year' : orders_2018['Year']
    })

    month_count_df['Month'] = pd.Categorical(month_count_df['Month'], categories=custom_month_order, ordered=True)
    sorted_month_count_df = month_count_df[month_count_df['Year'] == 2018].sort_values(['Year', 'Month'])
    sorted_month_count_df = sorted_month_count_df.sort_values('Month')

    col1,col2=st.columns([10,10])

    with col1:
        fig1 = go.Figure()

        fig1 = px.histogram(day_orders_series,  
        category_orders={'x': day_orders_series.value_counts().index},
        labels={'x': 'Order Status', 'y': 'Count'})

        fig1.update_layout(
        title='Total Orders by Day of Week in 2018',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        col1.plotly_chart(fig1,use_container_width=True)

    with col2:
        fig2 = go.Figure()

        fig2 = px.histogram(day_orders_series,  
        category_orders={'x': day_orders_series.value_counts().index},
        labels={'x': 'Order Status', 'y': 'Count'})

        fig2.update_layout(
        title='Total Orders by Time of Day in 2018',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        col2.plotly_chart(fig2,use_container_width=True)

    with st.container():
        fig3 = go.Figure()

        fig3 = px.histogram(sorted_month_count_df['Month'],  
        category_orders={'x': sorted_month_count_df['Month'].value_counts().index},
        labels={'x': 'Month', 'y': 'Count'})
        
        fig3.update_layout(
        title='Total Orders by Month of Years in 2018',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        st.plotly_chart(fig3,use_container_width=True)

if selected == 'All':
    orders_all = orders_merge

    order_time_of_day = [get_time_of_day(x) for x in orders_all['order_purchase_timestamp']]
    day_orders = [x.day_name() for x in orders_all['order_purchase_timestamp']]

    order_time_of_day_series = pd.Series(order_time_of_day)
    day_orders_series = pd.Series(day_orders)

    month_count_df = pd.DataFrame({
    'Month' : orders_all['Month'],
    'Year' : orders_all['Year']
    })

    month_count_df['Month'] = pd.Categorical(month_count_df['Month'], categories=custom_month_order, ordered=True)
    sorted_month_count_df = month_count_df.sort_values(['Year', 'Month'])
    sorted_month_count_df = sorted_month_count_df.sort_values('Month')

    col1,col2=st.columns([10,10])

    with col1:
        fig1 = go.Figure()

        fig1 = px.histogram(day_orders_series,  
        category_orders={'x': day_orders_series.value_counts().index},
        labels={'x': 'Order Status', 'y': 'Count'})

        fig1.update_layout(
        title='Total Orders by Day of Week in 2016-2018',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        col1.plotly_chart(fig1,use_container_width=True)

    with col2:
        fig2 = go.Figure()

        fig2 = px.histogram(day_orders_series,  
        category_orders={'x': day_orders_series.value_counts().index},
        labels={'x': 'Order Status', 'y': 'Count'})

        fig2.update_layout(
        title='Total Orders by Time of Day in 2016-2018',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        col2.plotly_chart(fig2,use_container_width=True)

    with st.container():
        fig3 = go.Figure()

        #fig3 = px.histogram(sorted_month_count_df['Month'],  
        #category_orders={'x': sorted_month_count_df['Month'].value_counts().index},
        #labels={'x': 'Month', 'y': 'Count'})
        
        fig3.add_trace(go.Histogram(
            x=sorted_month_count_df.loc[sorted_month_count_df['Year']==2016,'Month'],
            name='2016', # name used in legend and hover labels
            marker_color='#50C4ED',
            opacity=0.75
        ))

        fig3.add_trace(go.Histogram(
            x=sorted_month_count_df.loc[sorted_month_count_df['Year']==2017,'Month'],
            name='2017', # name used in legend and hover labels
            marker_color='#387ADF',
            opacity=0.75
        ))

        fig3.add_trace(go.Histogram(
            x=sorted_month_count_df.loc[sorted_month_count_df['Year']==2018,'Month'],
            name='2018', # name used in legend and hover labels
            marker_color='#333A73',
            opacity=0.75
        ))

        fig3.update_layout(
        title='Total Orders by Month of Years in 2016-2018',
        xaxis_title='Order Status',
        yaxis_title='Count',
        template='plotly_white',
        width=1000,height=600
    )
        
        st.plotly_chart(fig3,use_container_width=True)