# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:53:52 2022

@author: user
"""

from tkinter import *
from tkinter import ttk
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import seaborn as sns




#function 1 for Life expectancy

def Life():
    app = dash.Dash()

    df = pd.read_csv(
        "https://raw.githubusercontent.com/ThuwarakeshM/geting-started-with-plottly-dash/main/life_expectancy.csv"
    )

    fig = px.scatter(
        df,
        x="GDP",
        y="Life expectancy",
        size="Population",
        color="continent",
        hover_name="Country",
        log_x=True,
        size_max=60,
    )

    app.layout = html.Div([dcc.Graph(id="life-exp-vs-gdp", figure=fig)])


    if __name__ == "__main__":
        app.run_server(debug=True)
    







#function 2 for Bill and Tip
def bt():

    app = dash.Dash(__name__)

    diamonds = sns.load_dataset("diamonds")

    scatter = px.scatter(
       data_frame=diamonds,
       x="price",
       y="carat",
       color="cut",
       title="Carat vs. Price of Diamonds",
       width=600,
       height=400,
    )
    histogram = px.histogram(
       data_frame=diamonds,
       x="price",
       title="Histogram of Diamond prices",
       width=600,
       height=400,
    )
    violin = px.violin(
       data_frame=diamonds,
       x="cut",
       y="price",
       title="Violin Plot of Cut vs. Price",
       width=600,
       height=400,
    )

    left_fig = html.Div(children=dcc.Graph(figure=scatter))
    right_fig = html.Div(children=dcc.Graph(figure=histogram))

    upper_div = html.Div([left_fig, right_fig], style={"display": "flex"})
    central_div = html.Div(
       children=dcc.Graph(figure=violin),
       style={"display": "flex", "justify-content": "center"},
    )
    app.layout = html.Div([upper_div, central_div])




    app = dash.Dash(name="my_first_dash_app")

    tips = px.data.tips()

    fig = px.scatter(tips, x="total_bill", y="tip")


    app.layout = html.Div([
       dcc.Dropdown(
           options=[
               {'label': 'FC Barcelona', 'value': 'FCB'},
               {'label': 'Real Madrid', 'value': 'RM'},
               {'label': 'Manchester United', 'value': 'MU'}
           ],
           multi=True,
           value="FCB"
       )
    ], style={"width": 200})


    app.layout = html.Div(children=[
       html.H1(children='Hello Dash'),  # Create a title with H1 tag

       html.Div(children='''
           Dash: A web application framework for your data.
       '''),  # Display some text

       dcc.Graph(
           id='example-graph',
           figure=fig
       )  # Display the Plotly figure
    ])

    if __name__ == '__main__':
       app.run_server(debug=True) # Run the Dash app
    


#driver code and GUI 



main_screen=Tk()
main_screen.title('DATA ANALYTICS')
main_screen.geometry('5000x5000')

frame=Frame(main_screen)
frame.pack()


label= Label(frame,text="DASHBOARD FOR VARIOUS GENERAL LIFE PURPOSES",justify=LEFT,bg='blue',font='1100')
label.pack(side=LEFT)


sep =ttk.Separator(main_screen,orient='horizontal')
sep.pack(fill='x')


labelframe = LabelFrame(main_screen, text="DATA ANALYTICS DASHBOARD")
labelframe.pack(fill="both", expand="yes")




button1=Button(labelframe,text="LIFE EXPECTANCY DASHBOARD",font='1400',command=Life)
button1.pack()

button2=Button(labelframe,text="BILL AND TIP",font='1400',command=bt)
button2.pack()



main_screen.mainloop()