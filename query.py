import mysql.connector as sqlcon
mycon=sqlcon.connect(host="localhost",user="tut",passwd="tut123",database="dbmsclg")

if mycon.is_connected():
    print("Successfully Connected")

ak=mycon.cursor()

queries=[
        "SELECT StudentName FROM STUDENT INNER JOIN ENROLLMENT ON STUDENT.RollNo = ENROLLMENT.RollNo",
"SELECT SocName FROM SOCIETY",
"SELECT StudentName FROM STUDENT WHERE StudentName LIKE 'A%'",
"SELECT * FROM STUDENT WHERE Course = 'computer science' OR Course = 'chemistry'",
"SELECT StudentName FROM STUDENT WHERE (RollNo LIKE 'X%' OR RollNo LIKE 'Z%') AND RollNo LIKE '%9'",
"SELECT * FROM SOCIETY WHERE TotalSeats > :N",
"UPDATE SOCIETY SET MentorName = :Harry WHERE SocID = :SS002",
"SELECT SocName FROM SOCIETY INNER JOIN ENROLLMENT ON SOCIETY.SocID = ENROLLMENT.SID GROUP BY SocID HAVING COUNT(*) > 5",
"SELECT StudentName FROM STUDENT INNER JOIN ENROLLMENT ON STUDENT.RollNo = ENROLLMENT.RollNo WHERE SID = (SELECT SocID FROM SOCIETY WHERE SocName = 'NSS') ORDER BY DOB ASC LIMIT 1",
"SELECT SocName FROM SOCIETY INNER JOIN ENROLLMENT ON SOCIETY.SocID = ENROLLMENT.SID GROUP BY SocID ORDER BY COUNT(*) DESC LIMIT 1",
"SELECT SocName FROM SOCIETY INNER JOIN ENROLLMENT ON SOCIETY.SocID = ENROLLMENT.SID GROUP BY SocID ORDER BY COUNT(*) ASC LIMIT 2",
"SELECT StudentName FROM STUDENT WHERE RollNo NOT IN (SELECT RollNo FROM ENROLLMENT)",
"SELECT StudentName FROM ENROLLMENT GROUP BY RollNo HAVING COUNT(*) >= 2",
"SELECT SocName FROM SOCIETY INNER JOIN ENROLLMENT ON SOCIETY.SocID = ENROLLMENT.SID GROUP BY SocID HAVING COUNT(*) = (SELECT MAX(CountSoc) FROM (SELECT COUNT(*) AS CountSoc FROM ENROLLMENT GROUP BY SID) AS Temp)",
"SELECT StudentName, SocName FROM STUDENT LEFT JOIN ENROLLMENT ON STUDENT.RollNo = ENROLLMENT.RollNo LEFT JOIN SOCIETY ON ENROLLMENT.SID = SOCIETY.SocID WHERE SID IS NOT NULL",
"SELECT StudentName FROM STUDENT INNER JOIN ENROLLMENT ON STUDENT.RollNo = ENROLLMENT.RollNo INNER JOIN SOCIETY ON ENROLLMENT.SID = SOCIETY.SocID WHERE SocName IN ('Debating', 'Dancing', 'Sashakt')",
"SELECT SocName FROM SOCIETY WHERE MentorName LIKE '%Gupta%'",
"SELECT SocName FROM SOCIETY GROUP BY SocID HAVING COUNT(*) <= 0.1 * TotalSeats",
"SELECT SocName, (TotalSeats - COUNT(ENROLLMENT.SID)) AS VacantSeats FROM SOCIETY LEFT JOIN ENROLLMENT ON SOCIETY.SocID = ENROLLMENT.SID GROUP BY SOCIETY.SocID",
"UPDATE SOCIETY SET TotalSeats = TotalSeats * 1.1",
"ALTER TABLE ENROLLMENT ADD EnrollmentFees ENUM('yes', 'no') DEFAULT 'no'",
"UPDATE ENROLLMENT SET DateOfEnrollment = '2018-01-15' WHERE SID = 's1'; UPDATE ENROLLMENT SET DateOfEnrollment = CURRENT_DATE() WHERE SID = 's2'; UPDATE ENROLLMENT SET DateOfEnrollment = '2018-01-02' WHERE SID = 's3'",
"CREATE VIEW Society_Enrollment_Count AS SELECT SOCNAME, COUNT(ENROLLMENT.SID) AS TotalEnrolled FROM SOCIETY LEFT JOIN ENROLLMENT ON SOCIETY.SocID = ENROLLMENT.SID GROUP BY SOCIETY.SocID",
"SELECT StudentName FROM STUDENT WHERE RollNo IN (SELECT RollNo FROM ENROLLMENT GROUP BY RollNo HAVING COUNT(*) = (SELECT COUNT(*) FROM SOCIETY))",
"SELECT COUNT(*) FROM SOCIETY INNER JOIN ENROLLMENT ON SOCIETY.SocID = ENROLLMENT.SID GROUP BY SOCIETY.SocID HAVING COUNT(*) > 5",
"ALTER TABLE STUDENT ADD MobileNumber VARCHAR(10) DEFAULT '9999999999'",
"SELECT COUNT(*) FROM STUDENT WHERE DATEDIFF(CURRENT_DATE(), DOB) / 365 > 20",
"SELECT StudentName FROM STUDENT INNER JOIN ENROLLMENT ON STUDENT.RollNo = ENROLLMENT.RollNo WHERE YEAR(DOB) = 2001",
"SELECT COUNT(*) FROM SOCIETY WHERE SocName LIKE 'S%' AND SocName LIKE '%t' GROUP BY SocID HAVING COUNT(*) >= 5",
"SELECT SOCIETY.SocName, MentorName, TotalSeats, COUNT(ENROLLMENT.SID) AS TotalEnrolled, (TotalSeats - COUNT(ENROLLMENT.SID)) AS UnfilledSeats FROM SOCIETY LEFT JOIN ENROLLMENT ON SOCIETY.SocID = ENROLLMENT.SID GROUP BY SOCIETY.SocID"
    
    ]

for query in queries:
    ak.execute(query)

    results=ak.fetchall()

    for row in results:
        print(row)


ak.close()
mycon.close()




















































































































"""
--  Creating Database Company
  CREATE DATABASE company;

--  to connect to database in command line client 
  USE company;


--  Creating Tables in Company  Database.

--  1. Creating employee Table-- 
  create Table employee(
  fname varchar(15) not null,
  minit char,
  lname varchar(15) not null,
  ssn char(9) not null,
  DOB Date,
  address varchar(30),
  sex char,
  salary Decimal(10,2),
  super_ssn char(9),
  dnumber int not null,
  primary key(ssn)
  );

-- 2. Creating department Table
  create table department(
  dname varchar(15) not null,
  dnumber int not null,
  mgr_ssn char(9) not null,
  mgr_start_date Date,
  primary key(dnumber),
  unique(dname),
  foreign key(mgr_ssn) references employee(ssn)
  );

-- 3. Creating Dept_Location Table
  create table dept_locations(
  dnumber int not null,
  dlocation varchar(15),
  primary key(dnumber,dlocation),
  foreign key(dnumber) references department(dnumber)
  );

-- 4. Creating project Table
  create table project(
  pname varchar(15),
  pnumber int,
  plocation varchar(15),
  dnumber int,
  primary key(pnumber),
  unique(pname),
  foreign key(dnumber) references department(dnumber)
  );

-- 5. Creating Works_on Table
  create table works_on(
  ssn char(9) not null,
  pnumber int not null,
  hours decimal(3,1) not null,
  primary key(ssn,pnumber),
  foreign key(ssn) references employee(ssn),
  foreign key(pnumber) references project(pnumber)
  );

-- 6 Creating Dependent Table
  create table dependent(
  ssn char(9),
  dependent_name varchar(15),
  sex char,
  DOB date,
  relationship varchar(8),
  primary key(ssn,dependent_name),
  foreign key(ssn) references employee(ssn)
  );

  --  Insert data into employee table
--  Insert data into employee table
INSERT INTO employee
VALUES
('John', 'B', 'Smith', '123456789', '1965-01-09', '731 Fondren, Houston, TX', 'M', 30000, '333445555', 5),
('Franklin', 'T', 'Wong', '333445555', '1955-12-08', '638 Voss, Houston, TX', 'M', 40000, '888665555', 5),
('Alicia', 'J', 'Zelaya', '999887777', '1968-01-19', '3321 Castle, Spring, TX', 'F', 25000, '333445555', 4),
('Jennifer', 'S', 'Wallace', '987654321', '1941-06-20', '291 Berry, Bellaire, TX', 'F', 43000, '888665555', 4),
('Ramesh', 'K', 'Narayan', '666884444', '1962-09-15', '975 Fire Oak, Humble, TX', 'M', 38000, '333445555', 5),
('Joyce', 'A', 'English', '453453453', '1972-07-31', '5631 Rice, Houston, TX', 'F', 55000, NULL, 1),
('Ahmad', 'V', 'Jabbar', '987987987', '1969-03-29', '980 Dallas, Houston, TX', 'M', 25000, '888665555', 4),
('James', 'E', 'Borg', '888665555', '1937-11-10', '450 Stone, Houston, TX', 'M', 25000, '333445555', 5);


--  Insert data into department table
INSERT INTO department
VALUES
('Research', 5, '333445555', '1988-05-22'),
('Administration', 4, '987654321', '1995-01-01'),
('Headquarters', 1, '888665555', '1981-06-19');

--  Insert data into DEPT_LOCATIONS table
INSERT INTO dept_locations
VALUES
(1, 'Houston'),
(5, 'Houston'),
(5, 'Sugarland'),
(5, 'Bellaire'),
(4, 'Stafford');

--  Insert data into WORKS_ON table
INSERT INTO works_on
VALUES
('123456789', 1, 32.567),
('123456789', 2, 7.5),
('666884444', 3, 40.0),
('453453453', 1, 20.0),
('453453453', 2, 20.0),
('333445555', 2, 10.0),
('333445555', 3, 10.0),
('333445555', 10, 10.0),
('333445555', 20, 10.0),
('333445555', 30, 30.0),
('987654321', 30, 5.0),
('987654321', 20, 15.0);

--  Insert data into project table
INSERT INTO project
VALUES
('ProductX', 1, 'Bellaire', 5),
('ProductY', 2, 'Sugarland', 5),
('ProductZ', 3, 'Houston', 5),
('Computerization', 10, 'Stafford', 4),
('Reorganization', 20, 'Houston', 1),
('Newbenefits', 30, 'Stafford', 5);

--  Insert data into DEPENDENT table
INSERT INTO dependent
VALUES
('333445555', 'Alice', 'F', '1986-04-05', 'Daughter'),
('333445555', 'Theodore', 'M', '1983-10-25', 'Son'),
('333445555', 'Joy', 'F', '1958-05-03', 'Spouse'),
('987654321', 'Abner', 'M', '1942-02-28', 'Spouse'),
('123456789', 'Michael', 'M', '1988-01-04', 'Son'),
('123456789', 'Alice', 'F', '1988-12-30', 'Daughter'),
('888665555', 'Elizabeth', 'F', '1967-05-05', 'Spouse');


  -- Queries Executed on Company DataBase from Chapter-7 of Book

  -- 1. Retrieve the names of all employees who do not have supervisors.
  SELECT fname,lname
  FROM employee
  WHERE super_ssn IS NULL;

  -- 2.
  SELECT DISTINCT pnumber
  FROM project
  WHERE pnumber IN
    ( SELECT pnumber
    FROM project, department, employee
    WHERE project.dnumber = department.dnumber AND
    mgr_ssn = ssn AND lname = 'Smith' )
  OR
  pnumber IN
    ( SELECT pnumber
    FROM works_on, employee
    WHERE works_on.ssn = employee.ssn AND lname = 'Smith' );

  -- 3.  Retrieve the name of each employee who has a dependent with the same first name and is the same sex as the employee.
  SELECT fname,lname from employee,dependent
  WHERE dependent.ssn=employee.ssn AND dependent.sex = employee.sex;

  -- 4. Retrieve the names of employees who have no dependents.
  select fname,lname from employee
  where employee.ssn not in (select dependent.ssn from dependent where employee.ssn=dependent.ssn);

  -- 5. List the names of managers who have at least one dependent
  SELECT fname,lname from employee
  WHERE 
  EXISTS (SELECT * FROM department WHERE employee.ssn =department.mgr_ssn) 
  AND
  EXISTS (SELECT * FROM dependent WHERE employee.ssn = dependent.ssn);

  -- 6. Retrieve the name of each employee who works on all the projects controlled by department number 5 
  SELECT fname,lname from employee
 WHERE NOT EXISTS ( 
  ( 
  SELECT pnumber
  FROM project
  WHERE project.dnumber = 5
  )
 EXCEPT ( 
 SELECT pnumber
 FROM works_on
 WHERE employee.ssn = works_on.ssn) 
 );

 -- 7. . Retrieve the Social Security numbers of all employees who work on project numbers 1, 2, or 3.
  SELECT DISTINCT Essn
  FROM WORKS_ON
  WHERE Pno IN (1, 2, 3);

  -- 8. Find the sum of the salaries of all employees, the maximum salary, the minimum salary, and the average salary
  SELECT SUM (Salary), MAX (Salary), MIN (Salary), AVG (Salary)
  FROM EMPLOYEE;

  -- 9. Find the sum of the salaries of all employees of the ‘Research’ department, as well as the maximum salary, the minimum salary, and the average salary in this department.
  SELECT SUM (Salary), MAX (Salary), MIN (Salary), AVG (Salary)
  FROM (EMPLOYEE JOIN DEPARTMENT ON Dno = Dnumber)
  WHERE Dname = ‘Research’;

  -- 10. Retrieve the total number of employees in the company and the number of employees in the ‘Research’ department 
  SELECT COUNT(*) FROM EMPLOYEE;

  SELECT COUNT(*)
  FROM EMPLOYEE, DEPARTMENT
  WHERE DNO = DNUMBER AND DNAME = ‘Research’;

  -- 11. Count the number of distinct salary values in the database.
  SELECT COUNT (Salary)
  FROM EMPLOYEE;

  -- 12. For each department, retrieve the department number, the number of employees in the department, and their average salary
  SELECT Dno, COUNT(*), AVG (Salary)
  FROM EMPLOYEE
  GROUP BY Dno;

  -- 13. For each project, retrieve the project number, the project name, and the number of employees who work on that project.
  SELECT Pnumber, Pname, COUNT(*)
  FROM PROJECT, WORKS_ON
  WHERE Pnumber = Pno
  GROUP BY Pnumber, Pname;

  -- 14.  For each project on which more than two employees work, retrieve the project number, the project name, and the number of employees who work on the project.
  SELECT Pnumber, Pname, COUNT(*)
  FROM PROJECT, WORKS_ON
  WHERE Pnumber = Pno
  GROUP BY Pnumber, Pname
  HAVING COUNT(*) > 2;

  -- 15. . For each project, retrieve the project number, the project name, and the number of employees from department 5 who work on the project.
  SELECT Pnumber, Pname, COUNT(*)
  FROM PROJECT, WORKS_ON, EMPLOYEE
  WHERE Pnumber = Pno AND Ssn = Essn AND Dno = 5
  GROUP BY Pnumber, Pname;

  -- 16.  For each department that has more than five employees, retrieve the department number and the number of its employees who are making more than $40,000.
  SELECT Dno, COUNT(*)
  FROM EMPLOYEE
  WHERE Salary>40000 AND Dno IN
  ( SELECT Dno
  FROM EMPLOYEE
  GROUP BY Dno
  HAVING COUNT(*) > 5);
"""
