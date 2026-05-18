use HospitalDB ;

-- ===================================================
-- Stored Proceduers 
-- ===================================================

-- Procedure 1 ==> Add New Patient 
create procedure hospital.sp_AddPatient
	@full_name varchar(150),
	@gender varchar(10) ,
	@birth_date date , 
	@phone varchar(20) ,
	@email varchar(100) , 
	@address varchar(255) ,
	@blood_type varchar(5)

as
begin
    insert into hospital.patients (full_name ,gender , birth_date , phone ,email ,address ,blood_type )
    values (@full_name,@gender,@birth_date,@phone,@email,@address,@blood_type)
end ;


exec hospital.sp_AddPatient
	@full_name = 'mohamed ahmed' ,
	@gender  = 'male',
	@birth_date  = '1995-06-16', 
	@phone  = 01500000004,
	@email  = 'mohamed@gmail.com', 
	@address =  'Cairo',
	@blood_type = 'A+';


update hospital.patients 
set   phone = '01520000001'
where  full_name = 'mohamed ahmed' ;


select * from hospital.patients ;



-- ==========================================================



-- Procedure 2 ==> Book Appointment
create procedure hospital.sp_BookAppointment
	@patient_id int ,
	@doctor_id int , 
	@appointment_date date 
as 
begin 
    insert into hospital.appointments (patient_id , doctor_id , appointment_date, status )
	values (@patient_id , @doctor_id , @appointment_date, 'Pending')
end ;

exec hospital.sp_BookAppointment 
	@patient_id = 6 ,
    @doctor_id =4,
	@appointment_date = '2026-05-15';


select * from hospital.appointments ;



-- ==================================================



-- Procedur 3 ==> Cancel Appointment 
create procedure hospital.sp_CancelAppointment
	@appointment_id int 
as 
begin
	update appointments
	set status = 'Cancelled'
	where appointment_id =@appointment_id;
end ;

exec hospital.sp_CancelAppointment
	@appointment_id = 7 ;

select * from hospital.appointments ;



-- =================================================



-- Procedure 4 ==> Add Prescription
create procedure hospital.sp_AddPrescription
	@patient_id int ,
	@doctor_id int ,
	@medicine_id int ,
	@quantity int 
as
begin
	insert into hospital.prescriptions (patient_id , doctor_id , medicine_id , quantity)
	values (@patient_id , @doctor_id , @medicine_id , @quantity )
end;


exec hospital.sp_AddPrescription
	@patient_id = 2 ,
	@doctor_id =3 ,
	@medicine_id = 4 ,
	@quantity = 2 

exec hospital.sp_AddPrescription
	@patient_id = 1 ,
	@doctor_id = 2 ,
	@medicine_id = 5 ,
	@quantity = 5


select * from hospital.medicines ;
select * from hospital.prescriptions ;


-- ================================================



-- Procedure 5 ==> Add New Doctor 
create procedure hospital.sp_AddNewDoctor
	@full_name varchar(100) ,
	@speciality varchar(100), 
	@phone varchar(20) ,
	@email varchar(150) ,
	@salary decimal(10,2) ,
	@department_id int 
as 
begin
	insert into hospital.doctors (full_name , speciality , phone , email , salary ,department_id)
	values (@full_name , @speciality ,@phone ,@email , @salary  ,@department_id)
end;

exec hospital.sp_AddNewDoctor
	@full_name = 'Mohamed Ayman' ,
	@speciality = 'Neurologist' ,
	@phone = '0150000006',
	@email = 'mohamed.ayman@gmail.com',
	@salary = 27000.00 ,
	@department_id = 2 ;


select * from hospital.departments ;
select * from hospital.doctors ;


-- ===========================================


-- Procedure 6 ==> Create Bills 
create procedure hospital.sp_CreateBill
	@patient_id int , 
	@amount decimal(10,2) ,
	@payment_status varchar(20) 
as 
begin 
	insert into hospital.bills (patient_id , total_amount , payment_status)
	values (@patient_id , @amount ,@payment_status)
end;

exec hospital.sp_CreateBill 
	@patient_id = 5 ,
	@amount = 1350, 
	@payment_status = 'Unpaid'

select * from hospital.bills ;


-- ==============================================


-- Procedure 7 ==> Create Admission
create procedure hospital.sp_CreateAdmission
	@patient_id int ,
	@room_id int ,
	@admission_date date ,
	@discharge_date date 
as
begin 
	insert into hospital.admissions (patient_id , room_id , admission_date ,discharge_date)
	values (@patient_id, @room_id , @admission_date ,@discharge_date)
end;

exec hospital.sp_CreateAdmission 
	@patient_id = 1,
	@room_id  = 4 ,
	@admission_date  = '2026-05-12' ,
	@discharge_date = '2026-05-27' ;

select * from hospital.admissions ;