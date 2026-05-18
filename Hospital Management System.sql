CREATE TABLE [departments] (
  [department_id] int PRIMARY KEY,
  [name] nvarchar(255),
  [location] nvarchar(255)
)
GO

CREATE TABLE [doctors] (
  [doctor_id] int PRIMARY KEY,
  [full_name] nvarchar(255),
  [specialty] nvarchar(255),
  [phone] nvarchar(255),
  [salary] decimal,
  [department_id] int
)
GO

CREATE TABLE [patients] (
  [patient_id] int PRIMARY KEY,
  [full_name] nvarchar(255),
  [gender] nvarchar(255),
  [birth_data] date,
  [phone] nvarchar(255),
  [address] nvarchar(255),
  [blood_type] nvarchar(255)
)
GO

CREATE TABLE [appointments] (
  [appointment_id] int PRIMARY KEY,
  [patient_id] int,
  [doctor_id] int,
  [appointment_date] datetime,
  [status] nvarchar(255)
)
GO

CREATE TABLE [rooms] (
  [room_id] int,
  [room_number] nvarchar(255),
  [room_type] nvarchar(255),
  [price_per_day] decimal,
  [status] nvarchar(255)
)
GO

CREATE TABLE [admissions] (
  [admission_id] int PRIMARY KEY,
  [patient_id] int,
  [room_id] int,
  [admiddion_date] date,
  [discharge] date
)
GO

CREATE TABLE [prescriptions] (
  [prescription_id] int PRIMARY KEY,
  [patient_id] int,
  [doctor_id] int,
  [medicine_id] int,
  [quantity] int,
  [prescription_date] date
)
GO

CREATE TABLE [bills] (
  [bill_id] int PRIMARY KEY,
  [patient_id] int,
  [total_amount] decimal,
  [bill_date] date,
  [payment_status] nvarchar(255)
)
GO

ALTER TABLE [doctors] ADD FOREIGN KEY ([department_id]) REFERENCES [departments] ([department_id])
GO

ALTER TABLE [appointments] ADD FOREIGN KEY ([patient_id]) REFERENCES [patients] ([patient_id])
GO

ALTER TABLE [appointments] ADD FOREIGN KEY ([doctor_id]) REFERENCES [doctors] ([doctor_id])
GO

ALTER TABLE [admissions] ADD FOREIGN KEY ([patient_id]) REFERENCES [patients] ([patient_id])
GO

ALTER TABLE [admissions] ADD FOREIGN KEY ([room_id]) REFERENCES [rooms] ([room_id])
GO

ALTER TABLE [prescriptions] ADD FOREIGN KEY ([patient_id]) REFERENCES [patients] ([patient_id])
GO

ALTER TABLE [prescriptions] ADD FOREIGN KEY ([doctor_id]) REFERENCES [doctors] ([doctor_id])
GO

ALTER TABLE [bills] ADD FOREIGN KEY ([patient_id]) REFERENCES [patients] ([patient_id])
GO
