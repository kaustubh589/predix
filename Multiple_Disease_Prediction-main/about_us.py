import streamlit as st 


def app():
    
# Create the main header for the about us page
    st.title("About Us")

    # Create a left-side column
    left_column, right_column = st.columns(2)

    # Add information about the company to the left-side column
    left_column.markdown("""
        

        **Mission Statement:** To make people able to predict their own diseases...

        **Vision Statement:** Healthy literate society...

        **About Us:** Welcome To MediPredict, Your Trusted Companion On The Journey To Health And Well-Being....

        **Why Choose Us:**

        - We offer a variety of services.
        - We are dedicated to providing the best quality prediction.
        - We offer competitive pricing.
        - We provide exceptional customer service.

        At MediPredict, We Understand The Importance Of Timely And Accurate Health Predictions. Our Mission Is To Empower Individuals With Valuable Insights Into Their Well-Being, Enabling Proactive Steps Towards A Healthier Life.

        With Cutting-Edge Technology And A Team Of Dedicated Healthcare Professionals, We Specialize In Predicting A Range Of Health Conditions, Including Heart Disease, Brain Tumors, Breast Cancer, Diabetes, And Pneumonia.

        Our Advanced Algorithms Analyze Comprehensive Health Data To Provide You With Reliable Predictions, Allowing For Early Detection And Intervention. But We Are More Than Just A Predictive Platform.

        We Believe In A Holistic Approach To Health, And That's Why We Go Beyond Predictions.

        MediPredict Is Your Partner In Creating Personalized Health Solutions. We Offer Tailored Suggestions And Connect You With The Best Doctors And Healthcare Professionals Specializing In The Identified Conditions.

        Your Well-Being Is Our Priority, And We Strive To Make The Path To Recovery As Seamless As Possible. Join Us In Taking Control Of Your Health Journey.

        Let Predi-X Be Your Guide To A Healthier And Happier Life. Together, We Can Make Informed Decisions And Take Proactive Steps Towards A Future Of Well-Being.

    """)


    st.markdown("""
        # Thankyou For Choosing MediPredict.
    """)
    # Add a map to the right-side column to show the company's location
    
    # Create a separate section for team members
    st.markdown("""
        # Meet the Team
    """)

    # Add team members using the 'card' functionality in Streamlit
    st.markdown("""
        ### Krishna Kesharwani
        ### Kamal Yadav
        ### Archi Jain
        ### Kaustubh Mishra
        ### Astuti Mishra
        **Occupation:** Student
        
    """)

    st.markdown("**Email:** [For any query mail Here](mailto:kamalkanpur01@gmail.com)")