iiimport mysql.connector as sqlcon
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


""" 
1. Retrieve names of students enrolled in any society. 
2. Retrieve all society names. 
3. Retrieve students' names starting with letter ‘A’. 
4. Retrieve students' details studying in courses ‘computer science’ or ‘chemistry’. 
5. Retrieve students’ names whose roll no either starts with ‘X’ or ‘Z’ and ends with ‘9’ 6. Find society details with more than N TotalSeats where N is to be input by the user 7. Update society table for mentor name of a specific society 8. Find society names in which more than five students have enrolled 9. Find the name of youngest student enrolled in society ‘NSS’ 10. Find the name of most popular society (on the basis of enrolled students) 11. Find the name of two least popular societies (on the basis of enrolled students) 12. Find the student names who are not enrolled in any society 13. Find the student names enrolled in at least two societies 14. Find society names in which maximum students are enrolled 15. Find names of all students who have enrolled in any society and society names in which at least one student has enrolled 16. Find names of students who are enrolled in any of the three societies ‘Debating’, ‘Dancing’ and ‘Sashakt’. 
17. Find society names such that its mentor has a name with ‘Gupta’ in it. 18. Find the society names in which the number of enrolled students is only 10% of its capacity. 
19. Display the vacant seats for each society. 
20. Increment Total Seats of each society by 10% 21. Add the enrollment fees paid (‘yes’/’No’) field in the enrollment table. 
22. Update date of enrollment of society id ‘s1’ to ‘2018-01-15’, ‘s2’ to current date and ‘s3’ to ‘2018-01-02’. 
23. Create a view to keep track of society names with the total number of students enrolled in it. 
24. Find student names enrolled in all the societies. 
25. Count the number of societies with more than 5 students enrolled in it 26. Add column Mobile number in student table with default value ‘9999999999’ 27. Find the total number of students whose age is > 20 years. 
28. Find names of students who are born in 2001 and are enrolled in at least one society. 
29. Count all societies whose name starts with ‘S’ and ends with ‘t’ and at least 5 students are enrolled in the society. 
30. Display the following information: 
Society name Mentor name Total Capacity Total Enrolled Unfilled Seats







### Basics of Computer Networks

1. **What is a computer network?**
   - A computer network is a group of interconnected devices that can communicate and share resources such as files, printers, and internet connections.

2. **What are the different types of networks?**
   - **LAN (Local Area Network):** A network confined to a small geographic area, like a single building.
   - **MAN (Metropolitan Area Network):** Spans a city or a large campus.
   - **WAN (Wide Area Network):** Covers a broad area, such as multiple cities or countries.
   - **PAN (Personal Area Network):** A small network for personal devices, like Bluetooth connections.

3. **Define the terms: bandwidth, latency, and throughput.**
   - **Bandwidth:** The maximum rate of data transfer across a network path.
   - **Latency:** The time it takes for data to travel from the source to the destination.
   - **Throughput:** The actual rate at which data is successfully transferred over the network.

4. **What is the difference between a hub, a switch, and a router?**
   - **Hub:** A basic networking device that broadcasts data to all devices in a network segment.
   - **Switch:** A device that forwards data only to the specific device(s) intended, based on MAC addresses.
   - **Router:** A device that routes data between different networks, typically using IP addresses.

5. **Explain the OSI model and its layers.**
   - **OSI (Open Systems Interconnection) Model:** A conceptual framework used to understand and implement standard protocols in networking, consisting of seven layers:
     1. Physical
     2. Data Link
     3. Network
     4. Transport
     5. Session
     6. Presentation
     7. Application

6. **What is the TCP/IP model and how does it differ from the OSI model?**
   - **TCP/IP Model:** A four-layered suite of protocols that governs the internet and similar networks:
     1. Link
     2. Internet
     3. Transport
     4. Application
   - **Difference:** The OSI model is a theoretical model with seven layers, while the TCP/IP model is a practical framework with four layers, designed specifically for real-world networking.

### Network Topologies

1. **What are the different types of network topologies?**
   - **Star:** All devices are connected to a central hub.
   - **Ring:** Each device is connected to two other devices, forming a circular pathway.
   - **Bus:** All devices share a single communication line or cable.
   - **Mesh:** Devices are interconnected with many redundant interconnections.
   - **Tree:** A combination of star and bus topologies with hierarchical connections.
   - **Hybrid:** A mix of two or more different types of topologies.

2. **What are the advantages and disadvantages of a mesh topology?**
   - **Advantages:** High redundancy and reliability, failure of one link doesn't affect the network.
   - **Disadvantages:** High cost and complexity of installation and maintenance.

### Network Devices

1. **What is a network interface card (NIC)?**
   - A hardware component that connects a computer to a network.

2. **Explain the role of a modem in a network.**
   - A modem (modulator-demodulator) converts digital data from a computer into an analog signal for transmission over telephone lines and vice versa.

3. **What is a firewall and how does it work?**
   - A firewall is a security device that monitors and controls incoming and outgoing network traffic based on predetermined security rules, acting as a barrier between a trusted network and untrusted networks.

4. **What is the purpose of a DNS server?**
   - A DNS (Domain Name System) server translates domain names (like www.example.com) into IP addresses that computers use to identify each other on the network.

### IP Addressing and Subnetting

1. **What is an IP address?**
   - An IP (Internet Protocol) address is a unique identifier assigned to each device connected to a network, used for addressing and routing data.

2. **Differentiate between IPv4 and IPv6.**
   - **IPv4:** Uses 32-bit addresses, allowing for about 4.3 billion unique addresses.
   - **IPv6:** Uses 128-bit addresses, allowing for a vastly larger number of unique addresses (approximately 340 undecillion).

3. **Explain the concept of subnetting.**
   - Subnetting divides a larger network into smaller, more manageable subnetworks, which can improve performance and security.

4. **What is a subnet mask?**
   - A subnet mask is a 32-bit number that divides an IP address into network and host portions.

5. **How do you calculate the number of subnets and hosts per subnet?**
   - Number of subnets: \( 2^n \) where \( n \) is the number of bits borrowed for subnetting.
   - Number of hosts per subnet: \( 2^m - 2 \) where \( m \) is the number of bits left for host addresses.

### Protocols

1. **What are network protocols?**
   - Network protocols are standardized rules for formatting and processing data across a network.

2. **Explain the functions of TCP and UDP.**
   - **TCP (Transmission Control Protocol):** Ensures reliable, ordered, and error-checked delivery of data.
   - **UDP (User Datagram Protocol):** Provides a connectionless, lightweight, and faster data transfer without guaranteed delivery.

3. **What is the difference between HTTP and HTTPS?**
   - **HTTP (HyperText Transfer Protocol):** Used for transferring web pages over the internet, not secure.
   - **HTTPS (HTTP Secure):** HTTP with encryption (SSL/TLS) for secure communication over the internet.

4. **Describe the DHCP process.**
   - **DHCP (Dynamic Host Configuration Protocol):** Automatically assigns IP addresses and other network configuration parameters to devices. The process involves:
     1. Discovery: Client broadcasts a DHCPDISCOVER message.
     2. Offer: Server responds with a DHCPOFFER.
     3. Request: Client requests the offered address with a DHCPREQUEST.
     4. Acknowledge: Server sends a DHCPACK to confirm.

5. **What is the purpose of ICMP?**
   - **ICMP (Internet Control Message Protocol):** Used for sending error messages and operational information, such as unreachable hosts or network diagnostics (e.g., ping).

### Wireless Networking

1. **What is Wi-Fi and how does it work?**
   - Wi-Fi is a wireless networking technology that allows devices to connect to a network using radio waves. It operates within the IEEE 802.11 standards.

2. **What are the different Wi-Fi standards?**
   - IEEE 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, 802.11ax.

3. **What is the difference between 2.4 GHz and 5 GHz Wi-Fi frequencies?**
   - **2.4 GHz:** Longer range, more interference, fewer channels.
   - **5 GHz:** Shorter range, less interference, more channels, faster speeds.

### Network Security

1. **What are the common types of network security attacks?**
   - **Phishing:** Fraudulent attempts to obtain sensitive information.
   - **DDoS (Distributed Denial of Service):** Overloading a network/service to make it unavailable.
   - **Man-in-the-Middle:** Intercepting communication between two parties.

2. **What is encryption and why is it important?**
   - Encryption transforms data into a coded format to prevent unauthorized access, ensuring confidentiality and data integrity.

3. **Explain the concept of a VPN (Virtual Private Network).**
   - A VPN creates a secure, encrypted connection over a less secure network, such as the internet, to protect data and privacy.

### Network Configuration and Management

1. **What is a MAC address?**
   - A MAC (Media Access Control) address is a unique identifier assigned to a network interface card (NIC) for communications at the data link layer.

2. **How does NAT (Network Address Translation) work?**
   - NAT translates private IP addresses within a local network to a public IP address for internet communication and vice versa, enabling multiple devices to share a single public IP.

3. **What is port forwarding?**
   - Port forwarding directs external network traffic to a specific internal IP address and port within a local network.

4. **Explain the process of packet switching.**
   - Packet switching divides data into packets that are sent independently over the network and reassembled at the destination, improving network efficiency and resilience.

### Hands-On Questions

1. **Can you configure a basic IP addressing scheme for a small network?**
   - Example: Assign IP addresses within the range 192.168.1.2 to 192.168.1.254 with a subnet mask of 255.255.255.0.

2. **Demonstrate how to set up a secure Wi-Fi network.**
   - Configure the router to use WPA3 encryption, set a strong password, disable WPS, and change the default SSID and admin credentials.

3. **Show how to use Wireshark to capture and analyze network traffic.**
   - Open Wireshark, select the appropriate network interface, start the capture, filter traffic based on protocols or IP addresses, and analyze the packet details for troubleshooting.

### Advanced Topics

1. **Explain VLAN (Virtual LAN) and its advantages.**
   - A VLAN partitions a physical network into multiple logical networks, improving security, reducing broadcast traffic, and simplifying management.

2.






### Basics of Computer Networks

1. **What is a computer network?**
   - A computer network is a group of interconnected devices that can communicate and share resources such as files, printers, and internet connections.

2. **What are the different types of networks?**
   - **LAN (Local Area Network):** A network confined to a small geographic area, like a single building.
   - **MAN (Metropolitan Area Network):** Spans a city or a large campus.
   - **WAN (Wide Area Network):** Covers a broad area, such as multiple cities or countries.
   - **PAN (Personal Area Network):** A small network for personal devices, like Bluetooth connections.

3. **Define the terms: bandwidth, latency, and throughput.**
   - **Bandwidth:** The maximum rate of data transfer across a network path.
   - **Latency:** The time it takes for data to travel from the source to the destination.
   - **Throughput:** The actual rate at which data is successfully transferred over the network.

4. **What is the difference between a hub, a switch, and a router?**
   - **Hub:** A basic networking device that broadcasts data to all devices in a network segment.
   - **Switch:** A device that forwards data only to the specific device(s) intended, based on MAC addresses.
   - **Router:** A device that routes data between different networks, typically using IP addresses.

5. **Explain the OSI model and its layers.**
   - **OSI (Open Systems Interconnection) Model:** A conceptual framework used to understand and implement standard protocols in networking, consisting of seven layers:
     1. Physical
     2. Data Link
     3. Network
     4. Transport
     5. Session
     6. Presentation
     7. Application

6. **What is the TCP/IP model and how does it differ from the OSI model?**
   - **TCP/IP Model:** A four-layered suite of protocols that governs the internet and similar networks:
     1. Link
     2. Internet
     3. Transport
     4. Application
   - **Difference:** The OSI model is a theoretical model with seven layers, while the TCP/IP model is a practical framework with four layers, designed specifically for real-world networking.

### Network Topologies

1. **What are the different types of network topologies?**
   - **Star:** All devices are connected to a central hub.
   - **Ring:** Each device is connected to two other devices, forming a circular pathway.
   - **Bus:** All devices share a single communication line or cable.
   - **Mesh:** Devices are interconnected with many redundant interconnections.
   - **Tree:** A combination of star and bus topologies with hierarchical connections.
   - **Hybrid:** A mix of two or more different types of topologies.

2. **What are the advantages and disadvantages of a mesh topology?**
   - **Advantages:** High redundancy and reliability, failure of one link doesn't affect the network.
   - **Disadvantages:** High cost and complexity of installation and maintenance.

### Network Devices

1. **What is a network interface card (NIC)?**
   - A hardware component that connects a computer to a network.

2. **Explain the role of a modem in a network.**
   - A modem (modulator-demodulator) converts digital data from a computer into an analog signal for transmission over telephone lines and vice versa.

3. **What is a firewall and how does it work?**
   - A firewall is a security device that monitors and controls incoming and outgoing network traffic based on predetermined security rules, acting as a barrier between a trusted network and untrusted networks.

4. **What is the purpose of a DNS server?**
   - A DNS (Domain Name System) server translates domain names (like www.example.com) into IP addresses that computers use to identify each other on the network.

### IP Addressing and Subnetting

1. **What is an IP address?**
   - An IP (Internet Protocol) address is a unique identifier assigned to each device connected to a network, used for addressing and routing data.

2. **Differentiate between IPv4 and IPv6.**
   - **IPv4:** Uses 32-bit addresses, allowing for about 4.3 billion unique addresses.
   - **IPv6:** Uses 128-bit addresses, allowing for a vastly larger number of unique addresses (approximately 340 undecillion).

3. **Explain the concept of subnetting.**
   - Subnetting divides a larger network into smaller, more manageable subnetworks, which can improve performance and security.

4. **What is a subnet mask?**
   - A subnet mask is a 32-bit number that divides an IP address into network and host portions.

5. **How do you calculate the number of subnets and hosts per subnet?**
   - Number of subnets: \( 2^n \) where \( n \) is the number of bits borrowed for subnetting.
   - Number of hosts per subnet: \( 2^m - 2 \) where \( m \) is the number of bits left for host addresses.

### Protocols

1. **What are network protocols?**
   - Network protocols are standardized rules for formatting and processing data across a network.

2. **Explain the functions of TCP and UDP.**
   - **TCP (Transmission Control Protocol):** Ensures reliable, ordered, and error-checked delivery of data.
   - **UDP (User Datagram Protocol):** Provides a connectionless, lightweight, and faster data transfer without guaranteed delivery.

3. **What is the difference between HTTP and HTTPS?**
   - **HTTP (HyperText Transfer Protocol):** Used for transferring web pages over the internet, not secure.
   - **HTTPS (HTTP Secure):** HTTP with encryption (SSL/TLS) for secure communication over the internet.

4. **Describe the DHCP process.**
   - **DHCP (Dynamic Host Configuration Protocol):** Automatically assigns IP addresses and other network configuration parameters to devices. The process involves:
     1. Discovery: Client broadcasts a DHCPDISCOVER message.
     2. Offer: Server responds with a DHCPOFFER.
     3. Request: Client requests the offered address with a DHCPREQUEST.
     4. Acknowledge: Server sends a DHCPACK to confirm.

5. **What is the purpose of ICMP?**
   - **ICMP (Internet Control Message Protocol):** Used for sending error messages and operational information, such as unreachable hosts or network diagnostics (e.g., ping).

### Wireless Networking

1. **What is Wi-Fi and how does it work?**
   - Wi-Fi is a wireless networking technology that allows devices to connect to a network using radio waves. It operates within the IEEE 802.11 standards.

2. **What are the different Wi-Fi standards?**
   - IEEE 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, 802.11ax.

3. **What is the difference between 2.4 GHz and 5 GHz Wi-Fi frequencies?**
   - **2.4 GHz:** Longer range, more interference, fewer channels.
   - **5 GHz:** Shorter range, less interference, more channels, faster speeds.

### Network Security

1. **What are the common types of network security attacks?**
   - **Phishing:** Fraudulent attempts to obtain sensitive information.
   - **DDoS (Distributed Denial of Service):** Overloading a network/service to make it unavailable.
   - **Man-in-the-Middle:** Intercepting communication between two parties.

2. **What is encryption and why is it important?**
   - Encryption transforms data into a coded format to prevent unauthorized access, ensuring confidentiality and data integrity.

3. **Explain the concept of a VPN (Virtual Private Network).**
   - A VPN creates a secure, encrypted connection over a less secure network, such as the internet, to protect data and privacy.

### Network Configuration and Management

1. **What is a MAC address?**
   - A MAC (Media Access Control) address is a unique identifier assigned to a network interface card (NIC) for communications at the data link layer.

2. **How does NAT (Network Address Translation) work?**
   - NAT translates private IP addresses within a local network to a public IP address for internet communication and vice versa, enabling multiple devices to share a single public IP.

3. **What is port forwarding?**
   - Port forwarding directs external network traffic to a specific internal IP address and port within a local network.

4. **Explain the process of packet switching.**
   - Packet switching divides data into packets that are sent independently over the network and reassembled at the destination, improving network efficiency and resilience.

### Hands-On Questions

1. **Can you configure a basic IP addressing scheme for a small network?**
   - Example: Assign IP addresses within the range 192.168.1.2 to 192.168.1.254 with a subnet mask of 255.255.255.0.

2. **Demonstrate how to set up a secure Wi-Fi network.**
   - Configure the router to use WPA3 encryption, set a strong password, disable WPS, and change the default SSID and admin credentials.

3. **Show how to use Wireshark to capture and analyze network traffic.**
   - Open Wireshark, select the appropriate network interface, start the capture, filter traffic based on protocols or IP addresses, and analyze the packet details for troubleshooting.

### Advanced Topics

1. **Explain VLAN (Virtual LAN) and its advantages.**
   - A VLAN partitions a physical network into multiple logical networks, improving security, reducing broadcast traffic, and simplifying management.

2.





### Protocols in Networking

Protocols are sets of rules that govern data communications. They define how data is formatted, transmitted, and received to ensure reliable and efficient communication between devices in a network. Here are some key protocols used in networking:

#### Application Layer Protocols
1. **HTTP (HyperText Transfer Protocol)**
   - **Function:** Used for transferring web pages on the internet.
   - **Port:** 80
   - **Description:** An application-layer protocol for transmitting hypertext via web browsers and web servers.

2. **HTTPS (HTTP Secure)**
   - **Function:** Secure version of HTTP, encrypting data for secure communication.
   - **Port:** 443
   - **Description:** Uses SSL/TLS to encrypt data, ensuring secure transactions over the internet.

3. **FTP (File Transfer Protocol)**
   - **Function:** Transfers files between a client and server.
   - **Ports:** 20 (data transfer), 21 (control)
   - **Description:** Allows users to upload, download, and manage files on remote servers.

4. **SMTP (Simple Mail Transfer Protocol)**
   - **Function:** Sends emails from a client to a server or between servers.
   - **Port:** 25
   - **Description:** Used for sending email messages to email servers and between email servers.

5. **IMAP (Internet Message Access Protocol)**
   - **Function:** Retrieves emails from a server, allowing management of email on the server.
   - **Port:** 143 (non-encrypted), 993 (encrypted)
   - **Description:** Allows users to access and manage their email directly on the mail server.

6. **POP3 (Post Office Protocol version 3)**
   - **Function:** Retrieves emails from a server to a client.
   - **Port:** 110 (non-encrypted), 995 (encrypted)
   - **Description:** Downloads emails from the server to the client, usually deleting them from the server.

#### Transport Layer Protocols
1. **TCP (Transmission Control Protocol)**
   - **Function:** Provides reliable, ordered, and error-checked delivery of data.
   - **Description:** Establishes a connection between sender and receiver, ensuring data integrity and proper sequencing.

2. **UDP (User Datagram Protocol)**
   - **Function:** Provides a connectionless service for fast, but unreliable, data transmission.
   - **Description:** Used for applications where speed is critical and error correction can be handled by the application, such as streaming media.

#### Network Layer Protocols
1. **IP (Internet Protocol)**
   - **Function:** Routes packets of data from the source to the destination.
   - **Description:** IP addresses and routes data packets, ensuring they reach the correct destination.

2. **ICMP (Internet Control Message Protocol)**
   - **Function:** Sends error messages and operational information.
   - **Description:** Used for diagnostics and network troubleshooting, such as the `ping` command.

3. **ARP (Address Resolution Protocol)**
   - **Function:** Maps IP addresses to MAC addresses.
   - **Description:** Resolves IP addresses to hardware (MAC) addresses, enabling proper packet delivery on a local network.

#### Data Link Layer Protocols
1. **Ethernet**
   - **Function:** Defines how data is transmitted over a physical medium in a local area network (LAN).
   - **Description:** Uses MAC addresses to ensure that data is sent to the correct device on the same network.

2. **PPP (Point-to-Point Protocol)**
   - **Function:** Provides a standard method for transporting multi-protocol data over point-to-point links.
   - **Description:** Used for direct communication between two network nodes, typically for internet dial-up connections.

#### Other Important Protocols
1. **DNS (Domain Name System)**
   - **Function:** Translates domain names to IP addresses.
   - **Port:** 53
   - **Description:** Converts human-readable domain names (e.g., www.example.com) into IP addresses.

2. **DHCP (Dynamic Host Configuration Protocol)**
   - **Function:** Automatically assigns IP addresses and network configuration parameters.
   - **Port:** 67 (server), 68 (client)
   - **Description:** Simplifies network administration by automatically assigning IP addresses to devices.

3. **SNMP (Simple Network Management Protocol)**
   - **Function:** Manages and monitors network devices.
   - **Port:** 161
   - **Description:** Used for collecting information and configuring network devices like routers, switches, and servers.

4. **Telnet**
   - **Function:** Provides command-line interface access to remote computers.
   - **Port:** 23
   - **Description:** Used for remote management of network devices, though it lacks encryption and is often replaced by SSH.

5. **SSH (Secure Shell)**
   - **Function:** Provides secure command-line interface access to remote computers.
   - **Port:** 22
   - **Description:** Encrypts data to provide secure communication over an insecure network.

Understanding these protocols and their functions is essential for managing and troubleshooting network communications effectively.
"""
