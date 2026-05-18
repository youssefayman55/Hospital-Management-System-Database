-- =====================================
-- Triggers  = These Triggers executes automatically do not need to recall
-- =====================================

-- Trigger 1 ==> Reduce Medicine Stock After Prescription
create trigger hospital.trg_UpdateMedicineStock
on hospital.prescriptions 
after insert 
as
begin 
	update medicines 
	set stock = stock - prescription.quantity
	from medicines 

	inner join inserted prescription
	on medicines.medicine_id = prescription.medicine_id
end;


select * from hospital.medicines ;
select * from hospital.prescriptions ;



-- ===============================================


-- Trigger 2 ==> Auto Update Bill Status When Payment Happens
create trigger hospital.trg_UpdateBillStatus
on hospital.bills
after insert 
as 
begin
	update hospital.bills
	set payment_status = 'Paid' 
	where bill_id in (select bill_id from inserted)
end;


select * from hospital.bills ;

select * from hospital.payments ;

drop trigger hospital.trg_UpdateBillStatus ;


-- ============================================


-- Trigger 3 ==> Update Room Status When Admission Happens
create trigger hospital.trg_UpdateRoomStatus
on hospital.admissions
after insert 
as
begin 
	update hospital.rooms 
	set status = 'Occupied'
	where room_id in (select room_id from inserted) 
end;


select * from hospital.v_RoomStatus;
select * from hospital.admissions ;


-- ==============================================


-- Trigger 4 ==> Free Room When Patient Discharged 
create trigger hospital.trg_FreeRoom
on hospital.admissions
after insert
as
begin 
	update hospital.rooms 
	set status = 'Available' 
	where room_id in ( select room_id from inserted)
end;

select * from hospital.rooms ;
select * from hospital.admissions ;