import streamlit as st

def calculate_bmi(weight, height):

    bmi = weight / (height ** 2)

    return round(bmi, 2)

def main():

    st.title("💪 BMI Calculator")

    st.write("Check your Body Mass Index (BMI)")

    weight = st.number_input("Enter your weight (kg)", min_value=1.0)

    height = st.number_input("Enter your height (m)", min_value=0.1)

    if st.button("Calculate BMI"):

        bmi = calculate_bmi(weight, height)
        
        st.success(f"Your BMI is: {bmi}")

        if bmi < 18.5:
            st.warning("You are Underweight.")
        elif 18.5 <= bmi < 24.9:
            st.info("You are Normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are Overweight.")
        else:
            st.error("You are Obese.")

 # Footer
    st.divider()

    st.markdown("""
                
    <div style="text-align: center; color: #718096;">
        © 2024 Python Web App | Made by Tayyab Aziz | MIT License | Version 1.1.0
    </div>
                
    """, unsafe_allow_html=True)

if __name__ == "__main__":

    main()