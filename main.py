from fastapi import FastAPI
from database import get_connection


# App instance
app = FastAPI()

###############################
# Home
###############################
@app.get("/")
def home():
    return {"message" : "This is ths hospital system which you can from it access hospital database"}




###############################
# Doctors
###############################
@app.get("/doctors")
def show_doctors():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM hospital.doctors")

    doctors = cursor.fetchall()

    doctors_list = []

    for doctor in doctors:

        doctors_list.append({

            "doctor_id": doctor[0],
            "full_name": doctor[1],
            "speciality": doctor[2],
            "phone": doctor[3],
            "email": doctor[4],
            "salary": float(doctor[5]),
            "hire_date": str(doctor[6]),
            "department_id": doctor[7]

        })

    cursor.close()
    conn.close()

    return {"doctors": doctors_list}

# add new doctor
@app.post("/doctors")
def add_doctor(doctor_data : dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """insert into hospital.doctors ( full_name , speciality ,   phone ,email, salary ,hire_date , department_id)
    values (?,?,?,?,?,?,?)"""

    cursor.execute(query , (doctor_data["full_name"],doctor_data["speciality"],doctor_data["phone"],doctor_data["email"],doctor_data["salary"],doctor_data["hire_date"],doctor_data["department_id"],))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message" : "New doctor added successfully!"}

# delete doctor 
@app.delete("/doctors/{doctor_name}")
def delete_doctor(doctor_name):

    conn = get_connection()
    cursor = conn.cursor()

    query = """delete from hospital.doctors where full_name = ?"""

    cursor.execute(query , doctor_name)

    cursor.commit()

    cursor.close()
    conn.close()

    return {"message" : "Doctor deleted successfully!"}




###############################
# Patients
###############################
#show patients 
@app.get("/patients")
def show_patient():

    conn = get_connection()
    cursor = conn.cursor()

    query = """select * from hospital.patients"""

    cursor.execute(query)
    
    patient_data = cursor.fetchall()
    
    patient_list = []

    for patient in patient_data:
        patient_list.append({
            "patient_id" : patient[0], 
            "full_name" : patient[1], 
            "gender" : patient[2], 
            "birth_of_date" : patient[3],
            "phone" : patient[4], 
            "email" : patient[5], 
            "address" : patient[6], 
            "blood_type" : patient[7], 
            "registiration_date" : patient[8]
        })

    cursor.close()
    conn.close()
    
    return {"patients" : patient_list}

# Add new patient
@app.post("/patients")
def add_patinet(data : dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """insert into hospital.patients (full_name,gender,birth_date,phone,email,address,blood_type)
            values (?,?,?,?,?,?,?)"""
    
    cursor.execute(query  ,(
            data["full_name"],
            data["gender"],
            data["birth_date"],
            data["phone"],
            data["email"],
            data["address"],
            data["blood_type"]
        ))

    conn.commit()

    cursor.close()
    conn.close()

    return {"massege" : "New patient added successfully!"}

# Delete patient
@app.delete("/patient/{patient_name}")
def delete_patient(patient_name):

    conn = get_connection()
    cursor = conn.cursor()

    query = """delete from hospital.patients 
            where full_name = ?"""
    
    cursor.execute(query , (patient_name,))
    
    conn.commit()

    cursor.close()
    conn.close()

    return {"message" : "Patient deleted successfully!"}



###############################
# Departments 
###############################
# Show departments
@app.get("/departments")
def show_department():

    conn = get_connection()
    cursor = conn.cursor()

    query = """select * from hospital.departments"""

    cursor.execute(query)

    data = cursor.fetchall()
    
    department_data = []

    for d in data:
        department_data.append({
            "department_id" : d[0],
            "name" : d[1],
            "location" : d[2]
        })

    cursor.close()
    conn.close()

    return {"department_data" : department_data}

# Add new department 
@app.post("/departments")
def add_department(data : dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """insert into hospital.departments (name , location)
    values (?,?)"""

    cursor.execute(query , (data["name"] , data["location"]))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message" : "Department added successfully!"}

#delete department 
@app.delete("/departments/{name}")
def delete_department(name):

    conn = get_connection()
    cursor = conn.cursor()

    query = """delete from hospital.departments 
            where name = ? """
    
    cursor.execute(query ,  (name,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"Message" : "Department deleted successfully!"}



###############################
# Appointments 
###############################
# Show appointments
@app.get("/appointments")
def show_appointments():

    conn = get_connection()
    cursor = conn.cursor()

    query = """select * from hospital.appointments"""

    cursor.execute(query)

    data = cursor.fetchall()

    data_list = []

    for i in data : 
        data_list.append({
            "appointment_id" : i[0] , 
            "patient_id" : i[1] , 
            "doctor_id_id" : i[2] , 
            "appointment_date" : i[3] , 
            "status" : i[4] 
        })

    cursor.close()
    conn.close()

    return {"data_list" : data_list}

# Add new appointments
@app.post("/appointments")
def add_appointment(data : dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """insert into hospital.appointments (patient_id , doctor_id , appointment_date , status)
    values (?,?,?,?)"""

    cursor.execute(query , (data["patient_id"],data["doctor_id"],data["appointment_date"],data["status"]))

    conn.commit()

    cursor.close()
    conn.close()

# delete an appointment
@app.delete("/appointments/{appointment_date}")
def delete_appointment(appointment_date: str):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM hospital.appointments
    WHERE appointment_date = ?
    """

    cursor.execute(query, (appointment_date,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"Message": "Appointment deleted successfully!"}



###############################
# Rooms
###############################
# Show Rooms
@app.get("/rooms")
def show_room():

    conn = get_connection()
    cursor = conn.cursor()

    query = """select * from hospital.rooms"""

    cursor.execute(query)

    data = cursor.fetchall()
    
    rooms_list = []

    for i in data:
        rooms_list.append({
            "room_id" : i[0],
            "room_number" : i[1],
            "room_type" : i[2],
            "price_per_day" : i[3],
            "status" : i[4]
        })
    
    cursor.close()
    conn.close()

    return {"rooms_list" : rooms_list}

# add rooms
@app.post("/rooms")
def add_medicine(data : dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """insert into hospital.rooms (room_number,room_type,price_per_day,status)
            values (?,?,?,?)"""
    
    cursor.execute(query , (data["room_number"] , data["room_type"] ,data["price_per_day"],data["status"] ))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message" : "New room added successfully!"}  


# delete rooms 
@app.delete("/rooms/{room_number}")
def delete_room(room_number):

    conn = get_connection()
    cursor = conn.cursor()

    query = """delete from hospital.rooms 
            where room_number = ?"""
    
    cursor.execute(query , (room_number,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"Message" : "Room deleted successfully!"}




###############################
# Medicines
###############################
# Show medicine data
@app.get("/medicines")
def show_medicine():

    conn = get_connection()
    cursor = conn.cursor()

    query = """select * from hospital.medicines"""

    cursor.execute(query)
    
    medicine_data = cursor.fetchall()

    medicine_list = []

    for medicine in medicine_data:
        medicine_list.append({
            "medicine_id" : medicine[0],
            "medicine_name" : medicine[1] ,
            "price" : medicine[2],
            "stock" : medicine[3]
        })

    cursor.close()
    conn.close()

    return {"medicine_list" : medicine_list}

# Add new medicine
@app.post("/medicines")
def add_medicine(data : dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """insert into hospital.medicines (medicine_name , price, stock)
            values (?,?,?)"""
    
    cursor.execute(query , (data["medicine_name"] , data["price"] ,data["stock"] ))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message" : "New medicine added successfully!"}

# Delete medicine
@app.delete("/delete/{medicine_name}")
def delete_medicine(medicine_name):

    conn = get_connection()
    cursor = conn.cursor()

    query = """delete from hospital.medicines 
            where medicine_name = ?"""
    
    cursor.execute(query , (medicine_name,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"Message" : "Medicine deleted successfully!"}


###############################
# Prescriptions
###############################
# Show Prescription
@app.get("/prescriptions")
def show_prescription():

    conn = get_connection()
    cursor = conn.cursor()

    query= """select * from hospital.prescriptions"""

    cursor.execute(query)

    data = cursor.fetchall()
    
    prescription_data = []

    for i in data:
        prescription_data.append({
            "prescription_id" : i[0],
            "patient_id" : i[1],
            "doctor_id" : i[2],
            "medicine_id" : i[3],
            "quantity" : i[3],
            "prescription_date" : i[4]
        })
 
    cursor.close()
    conn.close()

    return {"prescription_data":prescription_data}

# Add Prescription
@app.post("/prescriptions")
def add_prescription(data : dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """insert into hospital.prescriptions (patient_id,doctor_id,medicine_id,quantity)
    values (?,?,?,?)"""

    cursor.execute(query , (data["patient_id"] , data["doctor_id"],data["medicine_id"],data["quantity"]))

    conn.commit()

    cursor.close()
    conn.close()

    return {"Message" : "New prescription added successfully!"}

# Delete prescription 
@app.delete("/prescriptions/{patient_id}")
def delete_prescription(patient_id):

    conn = get_connection()
    cursor = conn.cursor()

    query = """delete from hospital.prescriptions
    where patient_id = ?"""

    cursor.execute(query , (patient_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"Message" : "Prescription Deleted successfully!"}




###############################
# Admissions
###############################
@app.get("/admissions")
def show_admission():

    conn = get_connection()
    cursor = conn.cursor()

    query = """select * from hospital.admissions"""

    cursor.execute(query)

    data = cursor.fetchall()

    admission_data = []

    for i in data:
        admission_data.append({
            "admission_id" : i[0],
            "patient_id" : i[1],
            "room_id" : i[2],
            "admission_date" : i[3],
            "discharge_date" : i[4]
        })

    cursor.close()
    conn.close()

    return {"admission_data" :admission_data }


# Add admission
@app.post("/admissions")
def add_admission(data : dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """insert into hospital.admissions (patient_id,room_id,admission_date,discharge_date)
        values (?,?,?,?)"""
    
    cursor.execute(query , (data["patient_id"],data["room_id"],data["admission_date"],data["discharge_date"]))

    conn.commit()

    cursor.close()
    conn.close()

    return {"Message" : "New admission added successfully!"}


# delete admission
@app.delete("/admissions/{patient_id}")
def delete_admission(patient_id):

    conn = get_connection()
    cursor = conn.cursor()

    query = """delete from hospital.admissions 
    where patient_id = ? """

    cursor.execute(query , (patient_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"Message" : "Admission deleted successfully!"}



###############################
# Payments
###############################
# Show payments
@app.get("/payments")
def show_payment():

    conn = get_connection()
    cursor = conn.cursor()
    
    query = """select * from hospital.payments"""

    cursor.execute(query)

    data = cursor.fetchall()

    payments_list = []

    for i in data:
        payments_list.append({
            "payment_id" : i[0],
            "bill_id" : i[1],
            "amount" : i[2],
            "payment_method" : i[3],
            "payment_date" : i[4]
        })

    cursor.close()
    conn.close()

    return {"payments_list" : payments_list}

# Add Payment
@app.post("/payments")
def add_payment(data : dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """insert into hospital.payments (bill_id,amount,payment_method,payment_date)
    values(?,?,?,?)"""

    cursor.execute(query, (data["bill_id"],data["amount"],data["payment_method"],data["payment_date"]))
    
    conn.commit()

    cursor.close()
    conn.close()

    return {"Message" : "New payment added successfully!"}


# Delete Payment
@app.delete("/payments/{payment_id}")
def delete_payment(payment_id : str):

    conn = get_connection()
    cursor = conn.cursor()

    query = """delete from hospital.payments
    where payment_id = ? """

    cursor.execute(query , (payment_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"Message" : "Payment deleted successfully!"}




###############################
# Bills
###############################
# Show bills
@app.get("/bills")
def show_bill():

    conn = get_connection()
    cursor = conn.cursor()

    query = """select * from hospital.bills"""

    cursor.execute(query)

    data = cursor.fetchall()

    bills_data = []

    for i in  data:
        bills_data.append({
            "bill_id" : i[0],
            "patient_id" : i[1], 
            "total_amount" : i[2],
            "bill_date" : i[3],
            "payment_status" : i[4]
        })

    cursor.close()
    conn.close()

    return {"bills_data" : bills_data}
 
# Add new bill
@app.post("/bills")
def add_bill(data : dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """insert into hospital.bills (patient_id, total_amount, bill_date, payment_status)
    values(?,?,?,?)"""

    cursor.execute(query , (data["patient_id"],data["total_amount"],data["bill_date"],data["payment_status"]))
    
    conn.commit()

    cursor.close()
    conn.close()

    return {"Message" : "New bill added successfuly!"}


# Delete bill
@app.delete("/bills/{bill_id}")
def delete_bill(bill_id):

    conn = get_connection()
    cursor = conn.cursor()

    query = """delete from hospital.bills
    where bill_id = ? """

    cursor.execute(query, (bill_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"Message" : "Bill Deleted successfully!"}


