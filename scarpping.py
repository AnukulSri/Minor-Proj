import streamlit as st
import pandas as pd
from dputils import scrape as sc

st.markdown("<h1 style='text-align:center;'>Web Scrapper</h1>",unsafe_allow_html=True)
with st.form("Search"):
   query = st.text_input("Enter a Product name")
   btn = st.form_submit_button("Submit") 

menu_choices = ['Amazon Store', 'FlipKart Store','Compare Product'] # creating the choices for user 
choice = st.sidebar.radio('Select an option from the menu', menu_choices)


##############################################

if choice == menu_choices[0]:
 url=f'https://www.amazon.in/s?k={query}'
 print(url)
 soup = sc.get_webpage_data(url)

 st.markdown("<h3>At Amazon</h3>",unsafe_allow_html=True)
# target
 target = {'tag':'div', 'attrs':{ 'class': 's-main-slot s-result-list s-search-results sg-row'}}
# items
 items = {'tag':'div', 'attrs':{ 'class': 's-result-item'}}
#delivery
#delivery={'tag':'div','attrs':{'class':'a-row s-align-children-center'}}
# heading
 title = {'tag':'h2','attrs':{'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}}
# price
 price = {'tag':'span','attrs':{'class':'a-price-whole'}}
 rating = {'tag':'div','attrs':{'class':'a-section a-spacing-none a-spacing-top-micro'}}

 output = sc.extract_many(soup,
        target=target, 
        items=items,
        title=title, 
        price=price, 
        rating=rating)


 if btn:
  df= pd.DataFrame(output)
  df
 st.markdown("---")

###########################################################

if choice == menu_choices[1]:
 st.markdown("<h3>At Flipkart</h3>",unsafe_allow_html=True)

 Flip_url=f'https://www.flipkart.com/search?q={query}'
 print(Flip_url)
 soup1 = sc.get_webpage_data(Flip_url)

 target = {'tag': 'div','attrs':{'class':'_1YokD2 _3Mn1Gg'}}
 items = {'tag': 'div','attrs':{'class':'_1AtVbE col-12-12'}}
 title = {'tag': 'div','attrs':{'class':'_4rR01T'}}
 price = {'tag': 'div','attrs':{'class':'_30jeq3 _1_WHN1'}}
 rating = {'tag': 'div','attrs':{'class':'_3LWZlK'}}
#link = {'tag': 'a','attrs':{'class':'_1fQZEK'},'output':'href'}

 Flip_output = sc.extract_many(soup1,
             target=target,
             items=items,
             title = title,
             price=price,
             rating=rating) 
 if btn:
    fk_df = pd.DataFrame(Flip_output)
    fk_df
 st.markdown("---")
#######################################################

if choice==menu_choices[2]:
  st.markdown("<h3>At Amazon</h3>",unsafe_allow_html=True)
  url=f'https://www.amazon.in/s?k={query}'
  print(url)
  soup = sc.get_webpage_data(url)

  target = {'tag':'div', 'attrs':{ 'class': 's-main-slot s-result-list s-search-results sg-row'}}
  items = {'tag':'div', 'attrs':{ 'class': 's-result-item'}}
 #delivery={'tag':'div','attrs':{'class':'a-row s-align-children-center'}}
  title = {'tag':'h2','attrs':{'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'}}
  price = {'tag':'span','attrs':{'class':'a-price-whole'}}
  rating = {'tag':'div','attrs':{'class':'a-section a-spacing-none a-spacing-top-micro'}}

  output = sc.extract_many(soup,
        target=target, 
        items=items,
        title=title, 
        price=price, 
        rating=rating)


  if btn:
   df= pd.DataFrame(output)
   df
  st.markdown("---")

  st.markdown("<h3>At Flipkart</h3>",unsafe_allow_html=True)

  Flip_url=f'https://www.flipkart.com/search?q={query}'
  print(Flip_url)
  soup1 = sc.get_webpage_data(Flip_url)

  target = {'tag': 'div','attrs':{'class':'_1YokD2 _3Mn1Gg'}}
  items = {'tag': 'div','attrs':{'class':'_1AtVbE col-12-12'}}
  title = {'tag': 'div','attrs':{'class':'_4rR01T'}}
  price = {'tag': 'div','attrs':{'class':'_30jeq3 _1_WHN1'}}
  rating = {'tag': 'div','attrs':{'class':'_3LWZlK'}}
#link = {'tag': 'a','attrs':{'class':'_1fQZEK'},'output':'href'}

  Flip_output = sc.extract_many(soup1,
             target=target,
             items=items,
             title = title,
             price=price,
             rating=rating) 
  if btn:
    fk_df = pd.DataFrame(Flip_output)
    fk_df
  st.markdown("---")