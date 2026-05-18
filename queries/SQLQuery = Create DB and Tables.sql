-- Create DB (HospitalDB)

create database HospitalDB ;
use HospitalDB ; 

--------------------------------------------------
--------------------------------------------------

-- Create Tables (10 tables)


-- 1th Table (departments)
create table departments (
      department_id int primary KEY IDENTITY(1,1) ,
      name varchar(100) not null unique , 
      location varchar(100) not null 
);


-- 2the table (doctor)
create table doctors(
    doctor_id int PRIMARY KEY IDENTITY(1,1),
    full_name varchar(150) not null ,
    speciality varchar(100) not null ,
    phone varchar(20)  not null unique ,
    email varchar(100) not null unique ,
    salary decimal(10,2) not null CHECK (salary > 0) ,
    hire_date date default getdate(),
    department_id int not null 

    CONSTRAINT fk_doctors_departments
    foreign key (department_id)
    references departments(department_id) 
);


-- 3th table (patients)
create table patients (
    patient_id int primary key identity(1,1),
    full_name varchar(150) not null ,
    gender varchar(10) check(gender in('male','female')),
    birth_date date not null ,
    phone varchar(20) not null, 
    email varchar(100) not null unique,
    address varchar(255) not null ,
    blood_type varchar(5),
    registration_date date default getdate() 
);

-- 4th table (Appointments)
create table appointments(
    appointment_id int primary key identity(1,1),
    patient_id int not null ,
    doctor_id int not null,
    appointment_date date not null ,
    status varchar(20) default 'Pending' check(status in ('Pending','Completed','Cancelled')),

    constraint fk_appointments_patients
    foreign key (patient_id)
    references patients(patient_id) ,

    constraint fk_appointments_doctors
    foreign key (doctor_id)
    references doctors(doctor_id)
);


-- 5th table (Rooms)
create table rooms(
    room_id int primary key identity(1,1),
    room_number varchar(20) not null unique,
    room_type varchar(50) not null check(room_type in ('ICU','Normal','Private')),
    price_per_day decimal(10,2) check(price_per_day > 0),
    status varchar(20) default 'available' check(status in ('Available','Occupied'))
);


-- 6th table (Admissions)
create table admissions(
     admission_id int primary key identity(1,1),
     patient_id int not null ,
     room_id int not null ,
     admission_date date not null ,
     discharge_date date ,

     constraint fk_admissions_patients
     foreign key (patient_id)
     references patients(patient_id),

     constraint fk_admissions_rooms
     foreign key (room_id)
     references rooms(room_id)
);


-- 7th table (Medicines)
create table medicines (
    medicine_id int primary key identity(1,1),
    medicine_name varchar(150) not null unique ,
    price decimal(10,2) check(price > 0),
    stock int check(stock >= 0)
);


-- 8th table (Prescriptions)
create table prescriptions (
    prescription_id int primary key identity(1,1),
    patient_id int not null ,
    doctor_id int not null ,
    medicine_id int not null ,
    quantity int not null check(quantity > 0),
    prescription_date date default getdate(),
    
    constraint fk_prescriptions_patients
    foreign key (patient_id)
    references patients(patient_id),

    constraint fk_prescriptions_doctors
    foreign key (doctor_id)
    references doctors(doctor_id) ,

    constraint fk_prescriptions_medicines
    foreign key (medicine_id)
    references medicines(medicine_id)
);


-- 9th table (Bills)
create table bills(
    bill_id int primary key identity(1,1),
    patient_id int not null ,
    total_amount decimal(10,2) check(total_amount >= 0),
    bill_date date default getdate(),
    payment_status varchar(20) default 'Unpaid'
    check(payment_status in('Paid','Unpaid','Pending')),

    constraint fk_bills_patients
    foreign key (patient_id)
    references patients(patient_id)
);

-- 10th table (Payments)
create table payments(
    payment_id int primary key identity(1,1),
    bill_id int not null,
    amount decimal(10,2) check(amount > 0),
    payment_method varchar(50) check(payment_method in ('Cash', 'Credit Card', 'Insurance', 'Online')),
    payment_date date default getdate(),

    constraint fk_payments_bills
    foreign key (bill_id)
    references bills(bill_id)

);