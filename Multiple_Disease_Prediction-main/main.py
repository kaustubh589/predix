import streamlit as st

from streamlit_option_menu import option_menu


import Home, test, contactus, about_us
st.set_page_config(
        page_title="Welcome to MediPredict",
)



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='MediPredict ',
                options=['Home','Account','About Us','Contact Us'],
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "20px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            Home.app()
        if app == "Account":
            test.app()    
            
        if app == 'About Us':
            about_us.app()
        if app == 'Contact Us':
            contactus.app()    
             
          
             
    run()            
         