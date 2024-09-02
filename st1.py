import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')  #标题文字,加黑大写

#------------------------------------------
st.write('Hello,*World!*:sunglasses:')   #用Markdown语法来显示文字
st.write(1234)
#------------------------------------------

df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]})
st.write(df)
#------------------------------------------

st.write('Below is a Dataframe:',df,'Above is a dataframe.')

df2=pd.DataFrame(np.random.randn(200,3),
                 columns=['a','b','c'])

c=alt.Chart(df2).mark_circle().encode(x='a',y='b',size='c',color='c',tooltip=['a','b','c'])
st.write(c)

#------------------------------------------
st.markdown("*Streamlit* is **really cool** ***cool***.")
st.markdown('''
:red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
 :grey[prtty] :rainbow[colors] and :blue-background[hightlight] text.''')
multi='''If you end a line with two apaces,
a soft return is used for the next line.

Two(or more) newline characters in a row will result in a hard return.'''

st.markdown(multi)



