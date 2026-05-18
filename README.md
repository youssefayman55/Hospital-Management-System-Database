# 🏥 Hospital Management System (SQL Server Database Project)

A complete **Hospital Management System Database** built using **Microsoft SQL Server**, designed to simulate real-world hospital operations including patients, doctors, appointments, billing, admissions, prescriptions, and analytics.

This project demonstrates advanced database design concepts such as:
- Relational schema design
- Stored procedures
- Triggers
- Views
- Data integrity constraints
- Realistic hospital workflows

---

## 🚀 Project Overview

The system manages a full hospital workflow:

- Patient registration & management
- Doctor and department structure
- Appointment booking system
- Room admissions & discharge tracking
- Prescription & medicine management
- Billing & payments system
- Automated business logic using triggers

---

## 🏗️ Database Architecture

Built using relational database principles with strong relationships between entities.

### Main Entities:
- Patients
- Doctors
- Departments
- Appointments
- Rooms
- Admissions
- Medicines
- Prescriptions
- Bills
- Payments

---

## 🗄️ Tech Stack

- 🗃️ Database: :contentReference[oaicite:0]{index=0}  
- 🧠 Language: SQL (DDL + DML + T-SQL)
- ⚙️ Tools: SQL Server Management Studio (SSMS)

---

## 📊 Database Schema (Tables)

The system contains **10 core tables**:

### 👨‍⚕️ Core Tables
- `departments`
- `doctors`
- `patients`
- `appointments`
- `rooms`
- `admissions`
- `medicines`
- `prescriptions`
- `bills`
- `payments`

---

## 🔗 Relationships

- Each doctor belongs to a department
- Appointments link patients with doctors
- Admissions link patients with rooms
- Prescriptions link patients, doctors, and medicines
- Bills are generated per patient
- Payments are linked to bills

---

## ⚙️ Stored Procedures

The system includes reusable business logic procedures:

### 👤 Patient Management
- `sp_AddPatient` → Add new patient

### 📅 Appointment System
- `sp_BookAppointment` → Book appointment
- `sp_CancelAppointment` → Cancel appointment

### 👨‍⚕️ Doctor Management
- `sp_AddNewDoctor` → Add new doctor

### 💊 Medical Operations
- `sp_AddPrescription` → Add prescription

### 💰 Billing System
- `sp_CreateBill` → Generate patient bill

### 🏥 Admissions
- `sp_CreateAdmission` → Admit patient to room

---

## ⚡ Triggers (Automated Logic)

The system uses triggers to automate operations:

### 💊 Medicine Stock Control
- Automatically reduces medicine stock after prescription

### 💰 Billing Automation
- Updates bill status automatically after payment

### 🛏️ Room Management
- Marks room as **Occupied** when patient is admitted
- Frees room when patient is discharged

---

## 📈 Views (Reporting Layer)

Pre-built analytical views for reporting:

### 👨‍⚕️ Doctor Information
- `v_DoctorInfo` → Full doctor details with department

### 📅 Patient Appointments
- `v_PatientAppointments` → Appointment history report

### 💰 Billing Summary
- `v_BillingSummary` → Patient billing overview

### 🏥 Room Status
- `v_RoomStatus` → Live room occupancy tracking

---

## 📥 Sample Data

The database includes realistic seed data:

- 5 Departments
- 5 Doctors
- 5 Patients
- Rooms (ICU, Private, Normal)
- Medicines inventory
- Appointments records
- Admissions history
- Bills & payments

---

## 🧠 Key Features

✔ Fully normalized relational database  
✔ Real-world hospital workflow simulation  
✔ Automated business logic (Triggers)  
✔ Reusable stored procedures  
✔ Analytical reporting views  
✔ Data integrity with constraints  
✔ Scalable schema design  

---

## 📌 Example Use Cases

- Hospital patient management system
- Clinic appointment booking system
- Medical billing system
- Room & admission tracking system
- Pharmacy stock management system

---

## 🚀 How to Run This Project

### 1️⃣ Open SQL Server
Start :contentReference[oaicite:1]{index=1}

--- 

### 2️⃣ Create Database : 

  CREATE DATABASE HospitalDB;

--- 

3️⃣ Run Scripts

Execute scripts in this order:

  => Tables creation script
  
  => Stored procedures script
  
  => Triggers script
  
  =>  Views script
  
  =>  Insert data script
  
---

🎯 Key Highlights : 

  => Enterprise-level database design
  
  => Real hospital workflow simulation
  
  => Advanced SQL concepts (procedures, triggers, views)
  
  => Clean relational schema
  
  => Production-style database structure


👨‍💻 Author   : Youssef Ayman
  
  Computer Science & Artificial Intelligence Engineer
  
  Specialized in Data Science, Backend Systems, and Database Design
  







  
