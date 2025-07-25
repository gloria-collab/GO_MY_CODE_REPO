-- Create Tables
CREATE TABLE Department (
    Num_S SERIAL PRIMARY KEY,
    Label VARCHAR(50) NOT NULL,
    Manager_Name VARCHAR(100) NOT NULL
);

CREATE TABLE Employee (
    Num_E SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Position VARCHAR(50) NOT NULL,
    Salary DECIMAL(10,2) NOT NULL,
    Department_Num_S INT REFERENCES Department(Num_S) ON DELETE SET NULL
);

CREATE TABLE Project (
    Num_P SERIAL PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Start_Date DATE NOT NULL,
    End_Date DATE NOT NULL,
    Department_Num_S INT REFERENCES Department(Num_S) ON DELETE SET NULL
);

CREATE TABLE Employee_Project (
    Employee_Num_E INT REFERENCES Employee(Num_E) ON DELETE CASCADE,
    Project_Num_P INT REFERENCES Project(Num_P) ON DELETE CASCADE,
    Role VARCHAR(100) NOT NULL,
    PRIMARY KEY (Employee_Num_E, Project_Num_P)
);

-- Insert Records into Department
INSERT INTO Department (Num_S, Label, Manager_Name) VALUES
(1, 'IT', 'Alice Johnson'),
(2, 'HR', 'Bob Smith'),
(3, 'Marketing', 'Clara Bennett');

-- Insert Records into Employee
INSERT INTO Employee (Num_E, Name, Position, Salary, Department_Num_S) VALUES
(101, 'John Doe', 'Developer', 60000.00, 1),
(102, 'Jane Smith', 'Analyst', 55000.00, 2),
(103, 'Mike Brown', 'Designer', 50000.00, 3),
(104, 'Sarah Johnson', 'Data Scientist', 70000.00, 1),
(105, 'Emma Wilson', 'HR Specialist', 52000.00, 2);

-- Insert Records into Project
INSERT INTO Project (Num_P, Title, Start_Date, End_Date, Department_Num_S) VALUES
(201, 'Website Redesign', '2024-01-15', '2024-06-30', 1),
(202, 'Employee Onboarding', '2024-03-01', '2024-09-01', 2),
(203, 'Market Research', '2024-02-01', '2024-07-31', 3),
(204, 'IT Infrastructure Setup', '2024-04-01', '2024-12-31', 1);

-- Insert Records into Employee_Project
INSERT INTO Employee_Project (Employee_Num_E, Project_Num_P, Role) VALUES
(101, 201, 'Frontend Developer'),
(104, 201, 'Backend Developer'),
(102, 202, 'Trainer'),
(105, 202, 'Coordinator'),
(103, 203, 'Research Lead'),
(101, 204, 'Network Specialist');INSERT INTO Employee_Project (Employee_Num_E, Project_Num_P, Role) VALUES
(101, 201, 'Frontend Developer'),
(104, 201, 'Backend Developer'),
(102, 202, 'Trainer'),
(105, 202, 'Coordinator'),
(103, 203, 'Research Lead'),
(101, 204, 'Network Specialist');

-- Update Role of Employee_Num_E = 101 in Employee_Project
UPDATE Employee_Project
SET Role = 'Full Stack Developer'
WHERE Employee_Num_E = 101;

-- Delete Employee with Num_E = 103 and cascade delete their project assignments
DELETE FROM Employee WHERE Num_E = 103;