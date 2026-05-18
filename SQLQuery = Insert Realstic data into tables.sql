--  Use the HospitalDB database 
use HospitalDB ;


-- =======================================
-- insert data into department table 
-- =======================================
insert into hospital.departments (name , location)
values 
('Cardiology', 'First Floor'),
('Neurology', 'Second Floor'),
('Orthopedics', 'Third Floor'),
('Pediatrics', 'Fourth Floor'),
('Dermatology', 'Fifth Floor');

select * from hospital.departments;


-- =========================================
-- INSERT INTO doctors
-- =========================================
INSERT INTO hospital.doctors
(full_name, speciality, phone, email, salary, hire_date, department_id)
VALUES
('Ahmed Hassan', 'Cardiologist', '01010000001', 'ahmed.hassan@hospital.com', 25000, '2022-01-15', 1),
('Sara Mohamed', 'Neurologist', '01010000002', 'sara.mohamed@hospital.com', 27000, '2021-06-20', 2),
('Omar Ali', 'Orthopedic Surgeon', '01010000003', 'omar.ali@hospital.com', 30000, '2020-03-10', 3),
('Mona Ibrahim', 'Pediatrician', '01010000004', 'mona.ibrahim@hospital.com', 22000, '2023-02-01', 4),
('Youssef Adel', 'Dermatologist', '01010000005', 'youssef.adel@hospital.com', 24000, '2021-09-18', 5);

select * from hospital.doctors;



-- =========================================
-- INSERT INTO patients
-- =========================================
INSERT INTO hospital.patients
(full_name, gender, birth_date, phone, email, address, blood_type)
VALUES
('Mahmoud Tarek', 'Male', '1995-04-10', '01120000001', 'mahmoud@gmail.com', 'Cairo', 'A+'),
('Nour Hany', 'Female', '2000-08-15', '01120000002', 'nour@gmail.com', 'Giza', 'B+'),
('Karim Adel', 'Male', '1988-11-22', '01120000003', 'karim@gmail.com', 'Alexandria', 'O+'),
('Salma Ashraf', 'Female', '1999-01-05', '01120000004', 'salma@gmail.com', 'Mansoura', 'AB+'),
('Hassan Ali', 'Male', '1975-06-30', '01120000005', 'hassan@gmail.com', 'Aswan', 'A-');

select * from hospital.patients;

-- =========================================
-- INSERT INTO rooms
-- =========================================
INSERT INTO hospital.rooms
(room_number, room_type, price_per_day, status)
VALUES
('R101', 'Normal', 500, 'Available'),
('R102', 'Private', 1200, 'Occupied'),
('R103', 'ICU', 2500, 'Occupied'),
('R104', 'Normal', 500, 'Available'),
('R105', 'Private', 1500, 'Available');

select * from hospital.rooms ; 


-- =========================================
-- INSERT INTO medicines
-- =========================================
INSERT INTO hospital.medicines
(medicine_name, price, stock)
VALUES
('Paracetamol', 25.50, 200),
('Amoxicillin', 45.00, 150),
('Ibuprofen', 30.00, 180),
('Vitamin C', 20.00, 300),
('Insulin', 150.00, 80);


select * from hospital.medicines;


-- =========================================
-- INSERT INTO appointments
-- =========================================
INSERT INTO hospital.appointments
(patient_id, doctor_id, appointment_date, status)
VALUES
(1, 1, '2026-05-15 10:00:00', 'Completed'),
(2, 2, '2026-05-15 11:00:00', 'Pending'),
(3, 3, '2026-05-16 09:30:00', 'Completed'),
(4, 4, '2026-05-16 12:00:00', 'Cancelled'),
(5, 5, '2026-05-17 02:00:00', 'Pending');

select * from hospital.appointments;


-- =========================================
-- INSERT INTO admissions
-- =========================================
INSERT INTO hospital.admissions
(patient_id, room_id, admission_date, discharge_date)
VALUES
(1, 2, '2026-05-01', '2026-05-05'),
(2, 3, '2026-05-03', NULL),
(3, 1, '2026-05-07', '2026-05-10');

select * from hospital.admissions ;



-- =========================================
-- INSERT INTO prescriptions
-- =========================================
INSERT INTO hospital.prescriptions
(patient_id, doctor_id, medicine_id, quantity, prescription_date)
VALUES
(1, 1, 1, 2, '2026-05-15'),
(2, 2, 2, 1, '2026-05-15'),
(3, 3, 3, 3, '2026-05-16'),
(4, 4, 4, 2, '2026-05-16'),
(5, 5, 5, 1, '2026-05-17');

select * from hospital.prescriptions ;


-- =========================================
-- INSERT INTO bills
-- =========================================
INSERT INTO hospital.bills
(patient_id, total_amount, bill_date, payment_status)
VALUES
(1, 1500, '2026-05-05', 'Paid'),
(2, 3200, '2026-05-06', 'Pending'),
(3, 900, '2026-05-10', 'Paid'),
(4, 700, '2026-05-12', 'Unpaid'),
(5, 4500, '2026-05-13', 'Pending');

select * from hospital.bills ; 


-- =========================================
-- INSERT INTO payments
-- =========================================
INSERT INTO hospital.payments
(bill_id, payment_date, amount, payment_method)
VALUES
(1, '2026-05-05', 1500, 'Cash'),
(2, '2026-05-06', 1000, 'Credit Card'),
(3, '2026-05-10', 900, 'Online'),
(5, '2026-05-13', 2000, 'Insurance');

select * from hospital.payments ; 



