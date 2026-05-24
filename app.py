import streamlit as st 
import pandas as pd
import requests 


st.set_page_config(
    page_title="Hospital Management System!",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Title
st.title("🏥 Hospital Management System")


url = " http://127.0.0.1:8000"

menu = st.sidebar.selectbox("menu" , ["Home" , "Doctors" , "Patients", "Departments" , "Appointments" ,"Rooms" ,"Medicines" ,"Prescriptions" , "Admissions", "Payments", "Bills"])


###############################
# Home
###############################
if menu == "Home":

    response = requests.get(f"{url}/")

    if response.status_code == 200:

        data = response.json()

        st.markdown("---")

        st.info(data["message"])

        st.subheader("Available Modules")

        st.write("✅ Doctors")
        st.write("✅ Patients")
        st.write("✅ Departments")
        st.write("✅ Appointments")
        st.write("✅ Rooms")
        st.write("✅ Medicines")
        st.write("✅ Prescriptions")
        st.write("✅ Admissions")
        st.write("✅ Payments")
        st.write("✅ Bills")

    else:

        st.error("Failed to load home page!")


###############################
# Doctors
###############################
if menu == "Doctors":

    st.header("Doctor Information")

    if st.button("Load Doctors"):

        response = requests.get(f"{url}/doctors")

        if response.status_code == 200:

            data = response.json()["doctors"]

            df = pd.DataFrame(data)

            st.dataframe(df, width='stretch')

        else:
            st.error("Failed to load doctors data")

    # Add new doctor 
    st.header("Add new doctor!")

    with st.form("Add doctor"):
        full_name = st.text_input("Full Name")
        speciality = st.selectbox("Speciality",["Cardiologist","Neurologist","Orthopedic Surgeon","Pediatrician","Dermatologist","Neurologist"])
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        salary = st.number_input("Salary")
        hire_date = st.date_input("Hire Date")
        department_id = st.number_input("Department ID", step=1)

        submitted = st.form_submit_button("Add doctor")

        if submitted :
            doctor_data = {
                "full_name" : full_name,
                "speciality" : speciality,
                "phone" : phone,
                "email" : email,
                "salary" : float(salary),
                "hire_date" : str(hire_date),
                "department_id" : department_id,
            }
            response = requests.post(f"{url}/doctors" , json = doctor_data)

            if response.status_code == 200 : 
                st.success("New doctor Added successfully!")
            else:
                st.error("Falied to add new doctor ,Try again Please!")


    # Delete doctor 
    st.header("Delete Doctor")

    with st.form("delete doctor"):
        full_name = st.text_input("Full Name")

        submitted = st.form_submit_button("Delete")
    
    if submitted :

        response = requests.delete( f"{url}/doctors/{full_name}")

        if response.status_code == 200 : 
            
            st.success("Doctor deleted successfully!")
        else:
            st.error("Failed to delete doctor , Try again!")



###############################
# Patients
###############################
if menu == "Patients":

    st.header("Patients Info")

    # show patients information
    st.subheader("Patient data")
    
    response = requests.get(f"{url}/patients")

    if st.button("Refresh Data"):

        if response.status_code == 200 : 

            data = response.json()["patients"]

            data = pd.DataFrame(data)

            st.dataframe(data , width='stretch')
        else:
            st.error("Failed to load patients data , Try again")

    
    # Add new patinet 
    st.header("Add new patinet")

    with st.form("Add Patient"):
        full_name = st.text_input("Full Name")
        gender = st.selectbox("Gender" , ["Male" ,"Female"])
        birth_date = st.date_input("Birth Date")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        address = st.text_input("Address")
        blood_type = st.selectbox("Blood Type" , ["A","A+","A-","B","B+","B-","AB","AB+","AB-"])

        submitted = st.form_submit_button("Add Patient")

    if submitted: 

        data = {
            "full_name" : full_name , 
            "gender" : gender , 
            "birth_date": str(birth_date), 
            "phone" : phone , 
            "email" : email , 
            "address" : address , 
            "blood_type" : blood_type , 
        }
        response = requests.post(f"{url}/patients" , json = data)

        if response.status_code == 200 :
            st.success("New patient added successfully!")
        else:
            st.error("Failed to add new patient")
 
    # delete patient 
    st.header("Delete Patient")

    with st.form("delete patinet"):
        full_name = st.text_input("Full Name")

        submitted = st.form_submit_button("Delete")

    if submitted :

        response = requests.delete(f"{url}/patient/{full_name}")

        if response.status_code == 200 :
            st.success("Patient deleted successfully!")
        else:
            st.error("Failed to delete patient")



###############################
# Departments 
###############################
if menu == "Departments":

    # Show departments
    st.header("Departments Info")

    if st.button("Show"):

        response = requests.get(f"{url}/departments")

        if response.status_code == 200 : 

            data = response.json()["department_data"]

            data = pd.DataFrame(data)

            st.dataframe(data ,width='stretch')
        else:
            st.error("Failed to show departments")
    

    # Add new department 
    st.header("Add new department")

    with st.form("Add Department"):
        department_name = st.text_input("Department Name")
        location = st.text_input("Location")

        submitted = st.form_submit_button("Add")

    if submitted : 
        
        data = {
            "name" : department_name,
            "location" :  location 
        }
        response = requests.post(f"{url}/departments" , json =data)

        if response.status_code == 200 :
            st.success("Department added successfully!")
        else:
            st.error("Failed to add new department")


    # Delete department 
    st.header("Delete Department")

    with st.form("Delete Department"):
        name = st.text_input("Department Name")

        submitted = st.form_submit_button("Delete")

    if submitted:

        response = requests.delete(f"{url}/departments/{name}")

        if response.status_code == 200 :
            st.success("Department deleted successfully!")
        else:
            st.error("Failed to delete department, Try again!")


###############################
# Appointments 
###############################
if menu == "Appointments" :
    st.header("Appointments Info")

    # Show appointments
    st.subheader("Show Appointments")

    if st.button("Show"):
        response = requests.get(f"{url}/appointments")

        if response.status_code == 200:

            data = response.json()["data_list"]

            data = pd.DataFrame(data)

            st.dataframe(data , width='stretch' )
        else:
            st.error("Failed to load appointments")
        
    # Add new appointment
    st.subheader("Add New Appointment")

    with st.form("Add Appointment"):
        patient_id = st.number_input("Patient ID" , step = 1)
        doctor_id = st.number_input("Doctor ID" , step = 1)
        appointment_date = st.date_input("Appointment Date")
        status = st.selectbox("Select" , ["Pending" , "Complete","Cancelled"])
        
        submitted= st.form_submit_button("Add")

    if submitted:
        data = {
            "patient_id" : patient_id,
            "doctor_id" : doctor_id,
            "appointment_date" : str(appointment_date),
            "status" : status
        }

        response = requests.post(f"{url}/appointments" , json= data)

        if response.status_code == 200:
            st.success("Appointment added successfully!")
        else:
            st.error("Failed to add appointment!")

    # delete appointment
    st.header("Delete Appointment")

    with st.form("Delete Appointment"):
        appointment_date = st.date_input("Appointment Date")

        submitted = st.form_submit_button("Delete")

    if submitted:

        response = requests.delete(
            f"{url}/appointments/{appointment_date}"
        )

        if response.status_code == 200:
            st.success("Appointment deleted successfully!")

        else:
            st.error("Failed to delete appointment")


###############################
# Rooms
###############################
if menu == "Rooms" :
    st.header("Rooms Information")

    # Show Rooms
    st.subheader("Show rooms")
    
    if st.button("Show"):

        response = requests.get(f"{url}/rooms")

        if response.status_code == 200:

            data = response.json()["rooms_list"]

            data = pd.DataFrame(data)

            st.dataframe(data , width='stretch' )
        else:
            st.error("Failed to load rooms information")

    # add rooms
    st.subheader("Add New Room")

    with st.form("Add New Room"):
        room_number = st.text_input("Room Number")
        room_type = st.selectbox("Select" , ("Normal" , "Private" ,"ICU"))
        price_per_day = st.number_input("Price Per Day")
        status = st.selectbox("Select" , ("Available","Occupied"))
        
        submitted = st.form_submit_button("Add")

    if submitted:
        data = {
            "room_number" : room_number,
            "room_type" : room_type,
            "price_per_day" : price_per_day,
            "status" : status, 
        }

        response = requests.post(f"{url}/rooms" , json= data)

        if response.status_code == 200:
            st.success("New room added successfully!")
        else:
            st.error("Failed to add new room")


    # delete rooms 
    st.header("Delete Room")

    with st.form("Delete Room"):
        room_number = st.text_input("Room Number")

        submitted = st.form_submit_button("Delete")

    if submitted : 
        response = requests.delete(f"{url}/rooms/{room_number}")

        if response.status_code == 200 :
            st.success("Room deleted successfully!")
        
        else:
            st.error("Falied to delete Room ,Try again!")





###############################
# Medicines
###############################
if menu == "Medicines":
    
    # Show medicine stock
    st.header("Medicines Stock")

    if st.button("Show"):

        response  = requests.get(f"{url}/medicines")

        data = response.json()["medicine_list"]

        data = pd.DataFrame(data)

        st.dataframe(data , width='stretch')
    else:
        st.error("Failed to show medicine data!")



    # Add new medicine
    st.header("Add Medicines")
    with st.form("Add Medicines"):

        medicine_name = st.text_input("Medicine Name")
        medicine_price = st.text_input("Price")
        stock = st.text_input("Stock")

        submitted = st.form_submit_button("Add")

    if submitted:
        medicine_info = {
            "medicine_name" : medicine_name ,
            "price" : medicine_price ,
            "stock" : stock
        }

        response = requests.post(f"{url}/medicines" , json = medicine_info)

        if response.status_code == 200 : 
            st.success("Nem medicine added successfully!")
        else:
            st.error("Failed to add new medicine , Try again")

    
    # Delete medicine 
    st.header("Delete Medicine")

    with st.form("Delete medicine"):
        medicine_name = st.text_input("Medicine Name")

        submitted = st.form_submit_button("Delete")

    if submitted : 
        response = requests.delete(f"{url}/delete/{medicine_name}")

        if response.status_code == 200 :
            st.success("Medicine deleted successfully!")
        
        else:
            st.error("Falied to delete medicine ,Try again!")


###############################
# Prescriptions
###############################
if menu == "Prescriptions" : 
    st.header("Prescriptions Info")

    # Show Prescriptions
    if st.button("Show"):

        response = requests.get(f"{url}/prescriptions")

        if response.status_code == 200 :

            data = response.json()["prescription_data"]

            data = pd.DataFrame(data)

            st.dataframe(data , width='stretch')
        else:
            st.error("Failed to load prescriptions info")

    
    # Add Prescription 
    st.header("Add Prescription")

    with st.form("Add Prescription"):
        patient_id = st.number_input("Patient ID" , step = 1)
        doctor_id = st.number_input("Doctor ID" , step = 1)
        medicine_id = st.number_input("Medicine ID" , step = 1)
        quantity = st.number_input("Quantity" , step = 1)

        submitted = st.form_submit_button("Add")

    if submitted:
        data = {
            "patient_id" : patient_id,
            "doctor_id" : doctor_id,
            "medicine_id" : medicine_id,
            "quantity" : quantity,
        }
        
        response = requests.post(f"{url}/prescriptions" , json = data)

        if response.status_code == 200 :
            st.success("Prescription added successfully!")
        else:
            st.error("Failed to add prescription")


    # Delete prescription 

    st.header("Delete Prescription")
    with st.form("Delete Prescription"):
        patient_id = st.number_input("Patient ID" , step = 1)

        submitted = st.form_submit_button("Delete")

    if submitted:

        response = requests.delete(f"{url}/prescriptions/{patient_id}")

        if response.status_code == 200 : 
            st.success("Prescription deleted successfully!")
        else:
            st.error("Failed to delete prescription")



###############################
# Amissions
###############################
if menu == "Admissions" : 
    st.header("Admissions Info")

    # Show admissions
    st.header("Show Admissions")
    if st.button("Show"):

        response = requests.get(f"{url}/admissions")

        if response.status_code == 200 :

            data = response.json()["admission_data"]

            data = pd.DataFrame(data)

            st.dataframe(data , width='stretch')
        else:
            st.error("Faile to load admissions information")


    # Add admission
    st.header("Add New Admission")

    with st.form("Add New Admission"):
        patient_id = st.number_input("Patient ID" , step = 1)
        room_id = st.number_input("Room ID" , step = 1)
        admission_date = st.date_input("Admission Date")
        discharge_date = st.date_input("Discharge Date" )

        submitted = st.form_submit_button("Add")

    if submitted:

        data = {
            "patient_id" : patient_id,
            "room_id" : room_id,
            "admission_date" : str(admission_date),
            "discharge_date" : str(discharge_date)
        }
        response = requests.post(f"{url}/admissions" , json= data)

        if response.status_code == 200 : 
            st.success("New admission added successfully!")
        else:
            st.error("Failed to add new admission")

    # delete admission
    st.header("Delete Admission")

    with st.form("Delete Admission"):
        patient_id = st.number_input("Patient ID" , step = 1)

        submitted = st.form_submit_button("Delete")

    if submitted:
        response = requests.delete(f"{url}/admissions/{patient_id}")

        if response.status_code == 200 :
            st.success("Admission deleted successfully!")
        else:
            st.success("Failed to delete admission!")



###############################
# Payments
###############################
if menu == "Payments" :
    st.header("Payments Info")

    # Show payments
    st.subheader("Show Payments")

    if st.button("Show"):

        response = requests.get(f"{url}/payments")

        if response.status_code == 200 : 

            data = response.json()["payments_list"]

            data = pd.DataFrame(data)

            st.dataframe(data ,  width='stretch')
        else:
            st.error("Failed to load payments info!")

    # Add Payment
    st.subheader("Add Payment")

    with st.form("Add Payment"):
        bill_id = st.number_input("Bill ID" , step = 1)
        amount = st.number_input("Amount")
        payment_method = st.selectbox("Select" , ("Cash","Credit Card","Online","Insurance"))
        payment_date = st.date_input("Payment Date")

        submitted = st.form_submit_button("Add")

    if submitted:
        data = {
            "bill_id" : bill_id,
            "amount" : amount, 
            "payment_method" : payment_method,
            "payment_date" : str(payment_date)
        }

        response = requests.post(f"{url}/payments" , json=data)

        if response.status_code == 200: 
            st.success("Payment added successfully!")
        else:
            st.error("Failed to add payment!")

    # Delete Payment
    st.subheader("Delete Payment")

    with st.form("Delete Payment"):
        payment_id = st.number_input("Payment ID" , step= 1)

        submitted = st.form_submit_button("Delete")

    if submitted:

        response = requests.delete(f"{url}/payments/{payment_id}")
        
        if response.status_code == 200:

            st.success("Payment deleted successfully!")
        else:
            st.error("Failed to delete payment!")


###############################
# Bills
###############################
if menu == "Bills" : 

    st.header("Bills Info")

    # Show bills
    st.subheader("Show Bills Information")

    if st.button("Show"):
        response = requests.get(f"{url}/bills")

        if response.status_code == 200 :

            data = response.json()["bills_data"]

            data = pd.DataFrame(data)

            st.dataframe(data , width= 'stretch')
        else:
            st.error("Failed to load bills information")

    # Add new bill
    st.subheader("Add New Bill")

    with st.form("Add New Bill"):
        patient_id = int(st.number_input("Patient ID", step=1))
        total_amount = float(st.number_input("Total Amount"))
        bill_date = st.date_input("Bill Date")
        payment_status = st.selectbox("Select" , ("Pending","Paid","Unpaid"))
        
        submitted = st.form_submit_button("Add")

    if submitted:
        data = {
            "patient_id" : patient_id,
            "total_amount" : total_amount,
            "bill_date" : str(bill_date),
            "payment_status" : payment_status
        }

        response = requests.post(f"{url}/bills" , json=data)

        if response.status_code == 200:
            st.success("Bill added successfully!")
        else:
            st.error("Failed to add new bill")
            st.write(response.text)


    # Delete bill
    st.subheader("Delete Bills")

    with st.form("Delete Bill"):
        bill_id = st.number_input("Bill ID" , step =1)

        submitted = st.form_submit_button("Delete")

    if submitted:

        response= requests.delete(f"{url}/bills/{bill_id}")

        if response.status_code == 200:
            st.success("Bill deleted successfully!")
        else:
            st.error("Failed to delete bill!")

