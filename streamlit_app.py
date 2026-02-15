# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col
from snowflake.connector.pandas_tools import write_pandas
import requests
import pandas as pd


# Write directly to the app
st.title(f":cup_with_straw: Customize your smoothie! :cup_with_straw:")
st.write(
  """Choose the fruits you want in your custom Smoothie!
  """
)

name_on_order = st.text_input("Name on Smoothie:")
st.write("The name on your Smoothie will be: ", name_on_order)

cnx = st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))

# st.dataframe(data=my_dataframe, use_container_width=True)

ingredient_list = st.multiselect(
                  'Choose up to 5 ingredients:'
                  , my_dataframe
                  , max_selections = 5
                  )

if(ingredient_list):
    ingredients_string = ''

    for fruit_chosen in ingredient_list:
        ingredients_string += fruit_chosen + ' '
        st.subheader(fruit_chosen + ' Nutrition Information')
        my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""
        smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/" + fruit_chosen)
        sf_df = st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)    
    #st.write(my_insert_stmt)
    #st.stop()

    #if ingredients_string:
    #    session.sql(my_insert_stmt).collect()
    #    st.success('Your Smoothie is ordered!', icon="✅")
   
  
    time_to_insert = st.button('Submit Order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered, ' + name_on_order + '!', icon="✅")




data = [
    {"id":1,"name":"Apple","family":"Rosaceae","genus":"Malus","order":"Rosales",
     "carbs":14.8,"fat":0.21,"protein":0.19,"sugar":12.2},
    {"id":2,"name":"Banana","family":"Musaceae","genus":"Musa","order":"Zingiberales",
     "carbs":23,"fat":0.29,"protein":0.74,"sugar":15.8},
    {"id":3,"name":"Blueberry","family":"Ericaceae","genus":"Vaccinium","order":"Ericales",
     "carbs":14.6,"fat":0.31,"protein":0.7,"sugar":9.36},
    {"id":4,"name":"Cherry","family":"Rosaceae","genus":"Prunus","order":"Rosales",
     "carbs":16.2,"fat":0.19,"protein":1.04,"sugar":1.4444444444444444},
    {"id":5,"name":"Dragonfruit","family":"Cactaceae","genus":"Selenicereus","order":"Caryophyllales",
     "carbs":16.24,"fat":0.21,"protein":0.68,"sugar":None},
    {"id":6,"name":"Elderberry","family":"Adoxaceae","genus":"Sambucus","order":"Dipsacales",
     "carbs":18.4,"fat":0.5,"protein":0.66,"sugar":None},
    {"id":7,"name":"Figs","family":"Moraceae","genus":"Ficus","order":"Rosales",
     "carbs":63.9,"fat":0.92,"protein":3.3,"sugar":47.9},
    {"id":8,"name":"Guava","family":"Myrtaceae","genus":"Psidium","order":"Myrtales",
     "carbs":14.3,"fat":0.95,"protein":2.55,"sugar":None},
    {"id":9,"name":"Honeydew","family":"Cucurbitaceae","genus":"Cucumis","order":"Cucurbitales",
     "carbs":8.15,"fat":0.22,"protein":0.53,"sugar":7.03},
    {"id":10,"name":"Jackfruit","family":"Moraceae","genus":"Artocarpus","order":"Rosales",
     "carbs":23.9,"fat":0.14,"protein":0.36,"sugar":None},
    {"id":11,"name":"Kiwi","family":"Apterygidae","genus":"Apteryx","order":"Apterygiformes",
     "carbs":13.8,"fat":0.64,"protein":1.01,"sugar":8.56},
    {"id":12,"name":"Lime","family":"Rutaceae","genus":"Citrus","order":"Sapindales",
     "carbs":10.5,"fat":0.2,"protein":0.7,"sugar":None},
    {"id":13,"name":"Mango","family":"Anacardiaceae","genus":"Mangifera","order":"Sapindales",
     "carbs":17.4,"fat":0.68,"protein":0.69,"sugar":11.1},
    {"id":14,"name":"Nectarine","family":"Rosaceae ","genus":"Prunus","order":"Rosales",
     "carbs":9.18,"fat":0.28,"protein":1.06,"sugar":7.89},
    {"id":15,"name":"Orange","family":"Rutaceae ","genus":"Citrus","order":"Sapindales",
     "carbs":11.8,"fat":0.15,"protein":0.91,"sugar":8.57},
    {"id":16,"name":"Papaya","family":" ","genus":"","order":" ",
     "carbs":10.8,"fat":0.26,"protein":0.47,"sugar":7.82},
    {"id":17,"name":"Quince","family":"Rosaceae","genus":"","order":"Rosales",
     "carbs":15.3,"fat":0.1,"protein":0.4,"sugar":None},
    {"id":18,"name":"Raspberry","family":"Rosaceae","genus":"Rubus","order":"Rosales",
     "carbs":12.9,"fat":0.19,"protein":1.01,"sugar":2.68},
    {"id":19,"name":"Strawberry","family":"Rosaceae","genus":"Fragaria","order":"Rosales",
     "carbs":7.96,"fat":0.22,"protein":0.64,"sugar":4.86},
    {"id":20,"name":"Tangerine","family":"Rutaceae","genus":"Citrus","order":"Rosales",
     "carbs":13.3,"fat":0.31,"protein":0.81,"sugar":None},
    {"id":21,"name":"Ugli Fruit (Jamaican Tangelo)","family":"Rutaceae","genus":"Citrus","order":"Rosales",
     "carbs":None,"fat":None,"protein":None,"sugar":None},
    {"id":22,"name":"Vanilla Fruit","family":"Orchidaceae","genus":"Vanilla","order":"Asparagales",
     "carbs":None,"fat":None,"protein":None,"sugar":None},
    {"id":23,"name":"Watermelon","family":"Cucurbitaceae","genus":"Citrullus","order":"Cucurbitales",
     "carbs":7.55,"fat":0.15,"protein":0.61,"sugar":6.2},
    {"id":24,"name":"Ximenia (Hog Plum)","family":"Olacaceae","genus":"Ximenia","order":"Santalales",
     "carbs":None,"fat":None,"protein":None,"sugar":None},
    {"id":25,"name":"Yangmei (Waxberry)","family":"Myricaceae","genus":"Myrica","order":"Fagales",
     "carbs":None,"fat":None,"protein":None,"sugar":None},
    {"id":26,"name":"Ziziphus Jujube","family":"Rhamnaceae","genus":"Ziziphus","order":"Rosales",
     "carbs":20.2,"fat":0.2,"protein":1.2,"sugar":None}
]

df = pd.DataFrame(data)

cnx = st.connection("snowflake")
session = cnx._instance.connect()   # <-- this is the correct one

success, nchunks, nrows, output = write_pandas(
    conn=session,
    df=df,
    table_name="FRUITS_TABLE",
    auto_create_table=True,
    overwrite=True
)

st.write("Upload complete:", success)
st.write("Rows written:", nrows)



