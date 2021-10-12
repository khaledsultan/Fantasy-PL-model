import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Fantasy Premier League Prediction Model')
df = pd.read_csv('pred.csv')
df.dropna(inplace = True)
df['value'] = df['value']*0.1
df['prediction'] = round(df['prediction'])

st.image('FPL.png')

st.header('What is Fantasy ?')

st.subheader('Fantasy is an online game in which players collect points based on how real life footballers perform each week.You need to fill your team with all the positions and you are not allowed to simply buy 11 strikers who score goals every weekend. You need goalkeepers, defenders and midfielders too, plus one substitute for each position. 3 players are the maximum from one club.')

st.image('myteam.png')

st.header('How do the points work ?')

st.subheader('Each position on the pitch comes with its own points system. The goalkeepers and defenders are most commonly rewarded for things such as saving a penalty (5 points) or keeping a clean sheet (4 points); midfielders for setting up a goal (3); and strikers for scoring (4).')
st.subheader('It is also worth noting that players can lose points for negative actions in real-life, such as getting sent off (-3 points) or missing a penalty (-2).')
st.image('points.png')

st.header('Buying and selling players')
st.subheader('At the start of the game, you are given £100m to spend on your team. This has to cover the cost of all 15 players (including subs), so spend it wisely! You can not simply buy the best players as that will be too expensive. You need to balance your team with hotshots and cheaper buys.')
st.subheader('Each player has a value, based on how many FPL players buy him , and this value can increase or decrease.') 

st.header('Important Rules !!')
st.subheader('1. The captain of your team will have the double points.')
st.subheader('2. You can only replace one player for each week.')

st.header('So let me help you with my model .')


df

st.subheader('Choose three players !')
Player_1 = st.selectbox('Select the first player', df['name'].unique())


Player_2 = st.selectbox('Select the second player', df['name'].unique())


Player_3 = st.selectbox('Select the third player', df['name'].unique())


df_1 =df.loc[df.name==Player_1,['name','team','prediction']]
df_2 =df.loc[df.name==Player_2,['name','team','prediction']]
df_3 =df.loc[df.name==Player_3,['name','team','prediction']]

frames = [df_1, df_2,df_3]
result = pd.concat(frames)

st.subheader('Here you can choose your captain !')
x=result.sort_values('prediction',ascending=False)
x





st.title('Who to buy for the next round ?')

st.subheader('Give me position  : ')
position = st.selectbox('position', df['position'].unique())
st.subheader('Give me bugdet range :')

price_range = [[3.5,5],[5,7],[7,10],[10,13]]
selected_range = st.selectbox('price', price_range)
choice =df.loc[(df.position==position) & (df.value>=selected_range[0])& (df.value<selected_range[1]) ,['name','team','prediction','position','value']]

#choice =df.loc[(df.position==position)& (df.value>=price_range[0])  ,['name','team','prediction']]
#st.write(price_range[1][0])
st.subheader('You have to buy one of these players for the next round !')

st.write(choice.sort_values('prediction',ascending=False))

st.header('Tech stack ')
st.subheader('Python')
st.subheader('Pandas ')
st.subheader('Numpy')
st.subheader('Visual Studio ')
st.subheader('Streamlit ')
st.write('My data source :https://github.com/vaastav/Fantasy-Premier-League')



