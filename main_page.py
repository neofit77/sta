import streamlit as st
import pandas as pd
import numpy as np


st.subheader('Nova aplikacija')
st.markdown("# main page 🎈")
st.sidebar.markdown("# main page 🎈")

df = pd.read_excel('test.xlsx')
A=5
B=10
df['lat'] = df['C']/1
df['lon'] = df['D']/1
st.header('DATAFRAME')
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
st.text_input("Your name", key="name")
# You can access the value at any point with:
s = st.session_state.name
st.write(f'Moje ime je {s}')

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
st.bar_chart(df)
d = st.checkbox('Provera')
st.write(f'{d}')

option = st.selectbox(
    'Which number do you like best?',
     df['C'])

'You selected: ', option

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

st.sidebar.write(f'Trenutna vrednost je za kontakt {add_selectbox}, a za slajder {add_slider[0]}')
st.dataframe(df.style.highlight_max(axis=1))
st.map(df)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

import streamlit as st
import time



# Add a placeholder
c = st.text('Ucitavanje')
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  #latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

c.text('Ucitavanje zavrseno')

