import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import os

st.title('streamlit 超入門')

st.write('DataFrame')

# df = pd.DataFrame(np.random.rand(100,2)/[50, 50] + [35.69, 139.70], columns=['lat','lon'])

# st.dataframe(df.style.highlight_min(), width=200, height=200)
# st.map(df)
st.write(os.getcwd())

img = Image.open('aragaki.jpg')
st.image(img, caption='kuri', use_column_width=True)