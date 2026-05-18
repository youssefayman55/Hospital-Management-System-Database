-- ==============================================
--  View 1: Doctor Full Info
-- ==============================================
create view hospital.v_DoctorInfo as 
select 
     d.doctor_id ,
     d.full_name as doctor_name ,
     d.speciality , 
     dep.name as department ,
     d.phone ,
     d.email ,
     d.salary 
from hospital.doctors d 
join hospital.departments dep 
on d.department_id = dep.department_id ;

select * from hospital.v_DoctorInfo;





-- ========================================
-- View 2: Patient Appointments Report
-- ========================================
CREATE VIEW hospital.v_PatientAppointments AS
SELECT 
    p.patient_id,
    p.full_name AS patient_name,
    a.appointment_date,
    a.status,
    d.full_name AS doctor_name,
    d.speciality

FROM hospital.appointments a
JOIN hospital.patients p 
ON a.patient_id = p.patient_id

JOIN hospital.doctors d 

ON a.doctor_id = d.doctor_id;

select * from hospital.v_PatientAppointments;




-- ===============================================
-- View 3: Billing Summary
-- ===============================================
CREATE VIEW hospital.v_BillingSummary AS
SELECT 
    b.bill_id,
    p.full_name AS patient_name,
    b.total_amount,
    b.payment_status,
    b.bill_date

FROM hospital.bills b
JOIN hospital.patients p 
ON b.patient_id = p.patient_id;

select * from hospital.v_BillingSummary ;



-- ===========================================
-- View 4: Room Occupancy Status
-- ===========================================
CREATE VIEW hospital.v_RoomStatus AS
SELECT 
    r.room_number,
    r.room_type,
    r.status,
    r.price_per_day,
    p.full_name AS patient_name,
    a.admission_date,
    a.discharge_date

FROM hospital.rooms r
LEFT JOIN hospital.admissions a 
ON r.room_id = a.room_id
LEFT JOIN hospital.patients p 
ON a.patient_id = p.patient_id;

select * from hospital.v_RoomStatus ;