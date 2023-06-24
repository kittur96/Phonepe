import os
import json
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import streamlit as st
import matplotlib.pyplot as plt
import folium
from PIL import Image
import plotly.express as px
from streamlit_folium import folium_static
def app():
   # Change the background color to purple
   st.markdown(
    """
    <style>
    body {
        background-color: purple;
    }
    </style>
    """,
    unsafe_allow_html=True
)  
# Aggregated for transactions
   directory = r'G:/phonepe/pulse/data'  # the actual path to your folder

   data_list = []

   # Looping over all the state folders
   for state_dir in os.listdir(os.path.join(directory, 'G:/phonepe/pulse/data/aggregated/transaction/country/india/state')):
      state_path = os.path.join(directory,'G:/phonepe/pulse/data/aggregated/transaction/country/india/state',state_dir)
      if os.path.isdir(state_path):

   #         loop all over the folders
       for year_dir in os.listdir(state_path):
         year_path = os.path.join(state_path , year_dir)
         if os.path.isdir(year_path):
               for json_file in os.listdir(year_path):
                  if json_file.endswith('.json'):
                     with open(os.path.join(year_path, json_file)) as file:
                           data = json.load(file)
                           
                           #Extract the data fromt the json file
                           for transct_data in data['data']['transactionData']:
                              dict={"States":state_dir,
                                    "Transaction_year":year_dir,
                                    "Quaters":int(json_file.split('.')[0]),
                                    "Transaction_type":transct_data['name'],
                                    "Transaction_count":transct_data['paymentInstruments'][0]['count'],
                                    "Transaction_amount":transct_data['paymentInstruments'][0]['amount'],
                                    }
                              data_list.append(dict)
                  
   df1 = pd.DataFrame(data_list)
   

   # The os.listdir() function is a built-in Python function 
   # that returns a list of all the files and directories present in a specified directory.


   # The os.path.isdir() function is a method in the os.path module 
   # of Python that checks whether a given path is a directory or not.

   # The os.path.join() function is a method in the os.path module of Python that combines one or more path components into a 
   #single path. It intelligently handles the differences in path separators (/ or \) based on the underlying operating system.
   # for Users

   # Aggregated for users

   directory = r'G:/phonepe/pulse/data/aggregated/user/country/india/state'  

   l = []
   for state_dir in os.listdir(directory):
      state_path = os.path.join(directory,state_dir) 
      if os.path.isdir(state_path):
         for json_file in os.listdir(state_path):
               if json_file.endswith('.json'): 
                  with open(os.path.join(state_path,json_file),'r') as f:
                     data = json.load(f)
                     if isinstance(data,list):
                           l +=data
                     else:    
                           l.append(data)
         if l:
               df2 = pd.json_normalize(l)
               df2['subfolder'] = state_dir
               df2['subsubfolder']='state'
               
   df2=pd.DataFrame(data_list)           
   

   # Map for Transactions

   directory = r'G:/phonepe/pulse/data'  # the actual path to your folder

   data_list = []

   # Looping over all the state folders
   for state_dir in os.listdir(os.path.join(directory, 'G:/phonepe/pulse/data/map/transaction/hover/country/india/state')):
      state_path = os.path.join(directory,'G:/phonepe/pulse/data/map/transaction/hover/country/india/state',state_dir)
      if os.path.isdir(state_path):

   #         loop all over the year folder
       for year_dir in os.listdir(state_path):
         year_path = os.path.join(state_path , year_dir)
         if os.path.isdir(year_path):
               
               #loop all over the json files....
               for json_file in os.listdir(year_path):
                  if json_file.endswith('.json'):
                     with open(os.path.join(year_path, json_file)) as file:
                           data = json.load(file)
                           
                           #Extract the data fromt the json file
                           for hover_data in data['data']['hoverDataList']:
                              dict={"States":state_dir,
                                    "Transaction_year":year_dir,
                                    "Quaters":int(json_file.split('.')[0]),
                                    "Districts":hover_data['name'],
                                    "Transaction_type":hover_data['metric'][0]['type'],
                                    "Transaction_count":hover_data['metric'][0]['count'],
                                    "Transaction_amount":hover_data['metric'][0]['amount'],
                                    }
                              data_list.append(dict)
                  
   df3 = pd.DataFrame(data_list)
   

   # Map for users

   directory = r'G:/phonepe/pulse/data'  # the actual path to your folder

   data_list = []

   # Looping over all the state folders
   for state_dir in os.listdir(os.path.join(directory, 'G:/phonepe/pulse/data/map/user/hover/country/india/state')):
      state_path = os.path.join(directory,'G:/phonepe/pulse/data/map/user/hover/country/india/state',state_dir)
      if os.path.isdir(state_path):

   #         loop all over the year folder
       for year_dir in os.listdir(state_path):
         year_path = os.path.join(state_path , year_dir)
         if os.path.isdir(year_path):
               
               #loop all over the json files....
               for json_file in os.listdir(year_path):
                  if json_file.endswith('.json'):
                     with open(os.path.join(year_path, json_file)) as file:
                           data = json.load(file)
                           
                           #Extract the data fromt the json file
                           for district,values in data['data']['hoverData'].items():
                              dict={"States":state_dir,
                                    "Transaction_year":year_dir,
                                    "Quaters":int(json_file.split('.')[0]),
                                    "Districts":district,
                                    "Registered_users":values['registeredUsers']
                                    }
                              data_list.append(dict)
                  
   df4 = pd.DataFrame(data_list)
   

   # top transactions

   directory = r'G:/phonepe/pulse/data'  # the actual path to your folder

   data_list = []

   # Looping over all the state folders
   for state_dir in os.listdir(os.path.join(directory, 'G:/phonepe/pulse/data/top/transaction/country/india/state')):
      state_path = os.path.join(directory,'G:/phonepe/pulse/data/top/transaction/country/india/state',state_dir)
      if os.path.isdir(state_path):

   #         loop all over the year folder
       for year_dir in os.listdir(state_path):
         year_path = os.path.join(state_path , year_dir)
         if os.path.isdir(year_path):
               
               #loop all over the json files....
               for json_file in os.listdir(year_path):
                  if json_file.endswith('.json'):
                     with open(os.path.join(year_path, json_file)) as file:
                           data = json.load(file)
                           
                           #Extract the data fromt the json file
                           for dis in data['data']['districts']:
                              dict={"States":state_dir,
                                    "Transaction_year":year_dir,
                                    "Quaters":int(json_file.split('.')[0]),
                                    "Districts":dis['entityName'],
                                    "Transaction_type":dis['metric']['type'],
                                    "Transaction_count":dis['metric']['count'],
                                    "Transaction_amount":dis['metric']['amount'],
                                    }
                              data_list.append(dict)
                  
   df5 = pd.DataFrame(data_list)
   

   # top users

   directory = r'G:/phonepe/pulse/data'  # the actual path to your folder

   data_list = []

   # Looping over all the state folders
   for state_dir in os.listdir(os.path.join(directory, 'G:/phonepe/pulse/data/top/user/country/india/state')):
      state_path = os.path.join(directory,'G:/phonepe/pulse/data/top/user/country/india/state',state_dir)
      if os.path.isdir(state_path):

   #         loop all over the year folder
       for year_dir in os.listdir(state_path):
         year_path = os.path.join(state_path , year_dir)
         if os.path.isdir(year_path):
               
               #loop all over the json files....
               for json_file in os.listdir(year_path):
                  if json_file.endswith('.json'):
                     with open(os.path.join(year_path, json_file)) as file:
                           data = json.load(file)
                           
                           #Extract the data fromt the json file
                           for district in data['data']['districts']:
                              dict={"States":state_dir,
                                    "Transaction_year":year_dir,
                                    "Quaters":int(json_file.split('.')[0]),
                                    "Districts":district['name'] if 'name' in district else district['pincode'],
                                    "Registered_users":district['registeredUsers']
                                    }
                              data_list.append(dict)
                  
   df6 = pd.DataFrame(data_list)
   

   # ************Database connection******************
   # Create a MySQL database connection
   database_connection_url = 'mysql+pymysql://{username}:{password}@{host}/{database_name}'
   connection_string = database_connection_url.format(
   username = 'root',
   password = '12345',
   host = 'localhost',
   database_name = 'phonepe'
   )
   engine = sqlalchemy.create_engine(connection_string)

   # Session = sessionmaker(bind=engine)
   # session = Session()

   df1.to_sql('agg_tran',con=engine , if_exists='append',index=False)
   df2.to_sql('agg_user',con=engine , if_exists='append',index=False)
   df3.to_sql('map_tran',con=engine , if_exists='append',index=False)
   df4.to_sql('map_user',con=engine , if_exists='append',index=False)
   df5.to_sql('top_tran',con=engine , if_exists='append',index=False)
   df6.to_sql('top_user',con=engine , if_exists='append',index=False)

   engine.dispose()   



      # Create a sidebar navigation menu

   menu = ["About", "Home", "Contact Us","Insights about phonepe data"]
   choice = st.sidebar.selectbox("Menu", menu)
   
      # Render content based on menu selection
   if choice == "About":
         st.title("About")  
         st.write("""PhonePe is an Indian digital payments and financial services company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer.The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016.
      The PhonePe app is available in 11 Indian languages.Using PhonePe, users can send and receive money, recharge mobile, DTH, data cards, make utility payments, pay at shops, invest in tax saving funds, liquid funds, buy insurance, mutual funds, and digital gold.
      PhonePe is accepted as a payment option by over 3.5 crore offline and online merchant outlets, constituting 99% of pin codes in the country. The app served more than 10 crore users as of June 2018, processed 500 crore transactions by December 2019,[20] and crossed 10 crore transactions a day in April 2022. It currently has over 44 crore registered users with over 20 crore monthly active users.
      PhonePe is licensed by the Reserve Bank of India for the issuance and operation of a Semi Closed Prepaid Payment system with Authorisation Number: 75/2014 dated 22 August 2014.""")
         
         col1,col2,col3=st.columns(3)
         with col1:
            st.image(Image.open(r"C:\Users\vaibh\Downloads\sameer.jpg"),width =200)
            st.markdown("<p style='text-align: center;'><b>Sameer Nigam(CEO)</b></p>", unsafe_allow_html=True)
            st.write("Sameer Nigam founded PhonePe in 2015 and serves as its Chief Executive Officer. Before PhonePe, he served as the SVP Engineering and VP Marketing at Flipkart. His Flipkart journey started in 2011 when the company acquired his earlier startup - Mime360, a digital media distribution platform. Sameer has also served as the Director of Product Management at Shopzilla Inc, where he built the company's proprietary shopping search engine. In 2009, he won the coveted Wharton Venture Award, bestowed by the prestigious Wharton Business School. He holds an MBA from the Wharton Business School (University of Pennsylvania), USA, and a Master’s degree in Computer Science from the University of Arizona, Tucson-USA.")
         with col2:
            st.image(Image.open(r"C:\Users\vaibh\Downloads\rahul.jpg"),width =200)   
            st.markdown("<p style='text-align: center;'><b>Rahul Chari(CTO)</b></p>", unsafe_allow_html=True)
            st.write("Rahul Chari is the Chief Technology officer at PhonePe. He comes with two decades of experience spanning embedded systems, enterprise software development, e-commerce platforms and apps. Prior to PhonePe he was working as the VP Engineering at Flipkart and was responsible for building the best-in-class supply chain system for e-commerce. He joined Flipkart in 2011 through the acquisition of Mallers Inc where he served as the Chief Technology Officer and built Mime360, their flagship product. Prior to Mallers, Rahul was with the Data Center Business Unit at Cisco Systems where he was part of the team that developed the market changing MDS 9000 family of SAN switches. He is named on multiple storage virtualization related patents. Rahul holds a Masters degree in Computer Science from Purdue University, USA and a Bachelor's degree in Computer Engineering from Bombay (Mumbai) University, India (Gold Medalist).")

         with col3:
            st.image(Image.open(r"C:\Users\vaibh\Downloads\burzin.jpg"),width =200) 
            st.markdown("<p style='text-align: center;'><b>Burzin Engineer(CRO)</b></p>", unsafe_allow_html=True)
            st.write("Burzin is the Chief Reliability Officer at PhonePe. He has more than 25 years of experience in the dot-com space. During his stint at PhonePe, he has built web scale infrastructure and led multiple engineering projects including running and building PhonePe's web serving layer, cloud systems, network, storage and CDN. He’s passionate about building software at scale. Previously, he helped build Mime360, the flagship product at Mallers Inc. He set up their web services, Internal-IT, Application Engineering, Storage Networks and Configuration Services. While at Mallers Inc, he helped redesign the company’s infrastructure for unprecedented growth (100% year over). He holds a Master of Science in Computer Science from the University of Southern California.")
         st.download_button("Download the app now","https://www.phonepe.com/app-download/")   
      

         # logo_image = r"C:\Users\vaibh\Downloads\pp.jpg" # Replace with the path to your logo image file
         # st.image(logo_image, width=200)

   elif choice == "Home":
         tname = 'agg_tran'
         query = f"Select * from {tname}"
         state_data= pd.read_sql_query(query,engine)
         # st.write(state_data)
         col1,col2= st.columns(2)
         with col2:
          st.video(r"C:\Users\vaibh\Downloads\phonepe.mp4")
         col1.image(Image.open(r"C:\Users\vaibh\Downloads\phonepe.png"),width =200)
         col1.write("<span style='font-size: 35px; color: purple; font-weight: bold;'>Simple, Fast & Secure</span>", unsafe_allow_html=True)
         col1.write("#### One app for all things money.")
         col1.write("###### Pay bills, recharge, send money, buy gold, invest and shop at your favourite stores.")
         col1.write("--------------------------------------------------------------------------------------")
         col1.write("#### Pay whenever you like, wherever you like.")
         col1.write('###### Choose from options like UPI, the PhonePe wallet or your Debit and Credit Card.')
         col1.write("--------------------------------------------------------------------------------------")
         col1.write('#### Find all your favourite apps on PhonePe Switch.')
         col1.write("###### Book flights, order food or buy groceries. Use all your favourite apps without downloading them.")
         df = pd.DataFrame(state_data ,columns=['States','Transaction_year','Quaters','Transaction_type','Transaction_count','Transaction_amount'])
         fig=px.choropleth(df,locations="States",scope="asia",color='States',hover_name="States",
         title="Live Geo visualization of India")
         st.plotly_chart(fig)

   elif choice == "Contact Us":
         col1,col2,col3 =st.columns(3)
         with col3:
            st.write("Name: Vaibhav Singh")
         # email =(f'{"For any queries kindly reach out to me on Email I'd: "}   {"Vaibhav31595@gmail.com"}')
            
            st.write("Description: Data Scientist enthusiast...!")
            social_media  = {
               "Github" :"https://github.com/kittur96",
               "Linkedin"   :"https://www.linkedin.com/in/vaibhav-singh-2b1125159",
               "Hackerrank"  : "https://www.hackerrank.com/vaibhav31595?hr_r=1"
               
            }
         
         with col1:
            st.image(Image.open(r"C:\Users\vaibh\Downloads\phonepe.png"),width =100)
         with col2:
            st.markdown("<h2 style='text-align: center; color: purple;'>Phonepe Pluse data Visualization</h2>", unsafe_allow_html=True)
            st.write("The goal of this project is to extract data from phonepe pulse Github repository into our local directory,transform and clean the data and tranfer the data into mysql database using Streamlit application and pyplot graphs in python,the dashboard will display interactive and visually appealing,with several dropdown options for users to get insights about phonepe data over past years and based on that they can take decision which helps them to increase the profit of their business,its user friendly dashboard which requires zero technical knowledge...")
            st.write("-----------")
            cols =st.columns(len(social_media))
            for index,(platform,link) in enumerate(social_media.items()):
               cols[index].write(f"[{platform}]()")
            st.write("Email: Vaibhav31595@gmail.com")

   else: 
         st.write("Welcome to statistics of phonepe")
         options=['Top 10 states which have highest transaction all time?',
                                       'Total transactions happened yearwise?',
                                       'Top 10 states which have highest no.of users all the time?',
                                       'Category wise transaction',
                                       'Top 10 highest district transaction?',
                                       'Top 10 lowest district transaction?',
                                       'None']
         selected_option = st.selectbox("choose the questions",options,index=6)
         if selected_option =='None':
            pass
         elif  selected_option == 'Top 10 states which have highest transaction all time?':
            st.write('Top 10 states which have highest transaction all time?')
            query1 = "SELECT States, sum(Transaction_amount)/10000000 as Total_transaction_cr FROM top_tran group by States order by Total_transaction_cr desc limit 10;"
            df1 =pd.read_sql_query(query1,con =engine)
            col1,col2 = st.columns(2)
            with col1:
             st.table(df1)
            with col2: 
               # st.title("Top 10 states which have highest transaction all time")
               st.bar_chart(data=df1,x='States',y='Total_transaction_cr')
            # Create a map centered around India
            map_center = [20.5937, 78.9629]
            m = folium.Map(location=map_center, zoom_start=5)

         elif selected_option == 'Total transactions happened yearwise?':
            st.write('Total transactions happened yearwise?')
            query2 = "SELECT Transaction_year,sum(Transaction_amount)/10000000 as total_amt_in_cr FROM top_tran group by Transaction_year;"
            df2 =pd.read_sql_query(query2,con =engine)
            col1,col2 = st.columns(2)
            with col1:
             st.table(df2)
            with col2: 
              st.bar_chart(data=df2,x='Transaction_year',y='total_amt_in_cr')

         elif selected_option == 'Top 10 states which have highest no.of users all the time?':
            st.write('Top 10 states which have highest no.of users all the time?')
            query3 = "SELECT distinct States,MAX(Registered_users) as reg_users from  top_user group by States order by reg_users desc LIMIT 10 "
            df3 =pd.read_sql_query(query3,con =engine)
            col1,col2=st.columns(2)
            with col1:
             st.table(df3)
            with col2:
             st.bar_chart(data=df3,x='States',y='reg_users')

         elif selected_option == 'Category wise transaction':
            st.write('Category wise transaction')
            query4 = "SELECT Transaction_type,sum(Transaction_amount)/10000000 as max_tran from agg_user group by Transaction_type order by max_tran desc limit 10 "
            df4 =pd.read_sql_query(query4,con =engine) 
            col1,col2 =st.columns(2)
            with col1:      
             st.table(df4) 
            with col2: 

             st.bar_chart(data=df4,x='Transaction_type',y='max_tran')

         elif selected_option == 'Top 10 highest district transaction?':
            st.write('Top 10 highest district transaction?')
            query5 = "SELECT distinct Districts, sum(Transaction_amount)/10000000  as Trans_in_cr from top_tran group by Districts order by  Trans_in_cr desc limit 10 "
            df5 =pd.read_sql_query(query5,con =engine)
            col1,col2 = st.columns(2)
            with col1:
             st.table(df5)   
            with col2:  
             st.bar_chart(data=df5,x='Districts',y='Trans_in_cr')

         else:
            st.write('Top 10 lowest district transaction?')
            query6 = "SELECT distinct Districts, sum(Transaction_amount)/10000000  as Trans_in_cr from top_tran group by Districts order by  Trans_in_cr asc limit 10  "
            df6=pd.read_sql_query(query6,con =engine)
            col1,col2=st.columns(2)
            with col1:
             st.table(df6)     
            with col2:
               st.bar_chart(data=df6,x='Districts',y='Trans_in_cr')
           
# Mainfunction execution of program will starts from here only....          
if __name__ == '__main__':
    app()           