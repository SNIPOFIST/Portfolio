import streamlit as st


# Background pg_bg =
pg_bk = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url('https://c1.wallpaperflare.com/preview/373/217/83/guitarist-guitar-player-wallpaper-music-wallpapers.jpg');
background-size: cover;
}
</style>"""

# st.markdown(pg_bk,unsafe_allow_html=True)
st.set_page_config(page_title="Hari Ram Selvaraj's Certifications", page_icon="moon", layout="wide", initial_sidebar_state="expanded")

col_1, col_2, col_3 = st.columns(3)
# Header 
with col_1:
    pass

with col_2:
    st.title(":gray[Hari Ram Selvaraj's Certifications]")
    st.write("")
    st.write("")
    st.write("")

with col_3:
    pass

st.container()
st.subheader(":violet[Linkedin learning Certificates]",divider="orange")
st.write("")
col_1, col_2  = st.columns(2)

with col_1:
    st.markdown("* _Machine learning with Python foundations - [Link](https://www.linkedin.com/learning/certificates/958effb68d60d8eb7d5aed777329ce29b2fcb8dee96ae79493a81c4963deccd5)_")
    st.write("")
    st.markdown(" * _Supervised Learning essential training - [Link](https://www.linkedin.com/learning/certificates/887a8df68b0b7cacef02b424cc414a1411cf7e4ffd28af09207d3e5dd9b06742)_")
    st.write("")
    st.markdown(" * _NumPy essential training : 1 foundations of NumPy - [Link](https://www.linkedin.com/learning/certificates/04d58be1733fafc8b87fe62c2ba7374ef202df94431aaeb31c9f51b84c62ae0a)_")
    st.write("")
    st.markdown(" * _Learning Data Analytics : 1 Learnig foundations Data Analytics - [Link](https://www.linkedin.com/learning/certificates/b8f0d2ad129865a47aa6604578a6a1debcb87a4a482fe026b66b9d05521910c1)_")
    st.write("")
    st.markdown(" * _Introduction to career skills in Data Analytics - [Link](https://www.linkedin.com/learning/certificates/bd8ee7019ef6712874a23bee76b0e9dc6958ad92731c160ce9305b1c61ca4c82)_")
    st.write("")
    st.markdown(" * _Using Python for Automation - [Link](https://www.linkedin.com/learning/certificates/066e62a10b830c723f6498ab72d9edc764397b1e62f243b95adac18918ae3b3a)_")
    st.write("")
    st.markdown("*  _Webscraping with Python - [Link](https://www.linkedin.com/learning/certificates/091397f3df9bc23c6163292b90a664c077607b92e5b440fed747222e5cb1881a)_")
    st.write("")
    st.markdown(" * _Postman Essential Training- [Link](https://www.linkedin.com/learning/certificates/d103a6e405615c142d3d6099b9dff59fe01998884a8520a00fd644ba9a2ed9ce)_")
    st.write("")
    st.markdown(" * _Jmeter: Performance and Load Testing - [Link](https://www.linkedin.com/learning/certificates/7b0fda82a4ce4051883a6e196ac608e088b3fbb8144392ac922529262d4eb8a8)_")



with col_2:
    

    # Machine learning  
    st.caption(":green[Skills learnt] -  Random forest and logical regression algorithm, Algorithm bias detection,  ")

    # Supervised Machine Learning 
    st.write("")
    st.write("")  
    st.caption(":green[Skills learnt] -  Feature engineering, Data imputation and tailoring high effective datasets")

    # Numpy training  
    st.write("")
    st.caption(":green[Skills learnt] -  Multi dimensional array operations, Data Manipulations")

    st.write("")
    st.write("")
    # Learning data analytics 
    st.caption(":green[Skills learnt] -  Data interpretation, Data trimming, data visualisation techniques, Data selection  ")

    st.write("")
    # Introduction to career in data analytics automation 
    st.caption(":green[Skills learnt] -  Data analysis, Data Visualisation ")

    st.write("")
    st.write("")
    # Python for automation 
    st.caption(":green[Skills learnt] -  Automation tools - scrapy, beautifulsoup, requests HTTP methods, and automation techniques")   
    
    # Web scraping 
    st.write("")  
    st.caption(":green[Skills learnt] - API architecture, Response code validation ")
    
    st.write("")
    # Postman essential training   
    st.caption(":green[Skills learnt] - Axes method, Data crawling, Web mining , DOM text mining, Browser Automation")

    # Jmeter
    st.write("")
    st.caption(":green[Skills learnt] -  creation and execution of threads, Dahboard conversion of recieved responses")

st.write("")
st.write("")
st.subheader("Google - fundamentals in digital marketing ",divider="orange")
st.write("")
st.markdown("* _Fundamentals of Digital Mareting by Google - Digital Garage 2022_ ")
st.write("")
st.write("")


st.subheader("Other certificates",divider="violet")
st.write("")
st.markdown("* _Python Language 2019 - Aspire Solutions_ ")
st.write("")
st.markdown("* _Machine Learning 2019 - Aspire Solutions_ ")
st.write("")
st.markdown("* _Artificial intelligence 2020 - Aspire Solutions_ ")
st.write("")
st.markdown("* _Web Development with Kotlin and Android Studio 2021 - Aspire Solutions_ ")

st.write("")




