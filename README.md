# 🎓 Student Management System 🖥️

This is a simple **Student Management System** built using **Core Python**. It's a console-based application that allows users to perform CRUD operations on student records such as adding new students, viewing all students, searching for a student by ID, updating details, and deleting a record.

## 🔧 Tech Stack & Tools

- Core Python
- Object-Oriented Programming (OOP)
- File Handling (`.txt` files)
- Command-Line Interface (CLI)

---

## 📌 Features

✅ Add new student records  
✅ View all student records  
✅ Search student by ID  
✅ Update student details  
✅ Delete student records  
✅ Easy to use CLI interface  

---

## 💡 Concepts Practiced

- Python functions & modular coding  
- Class and object usage  
- File read/write operations  
- Conditional logic and loops  
- Basic input validation  
- Menu-driven interface

---

### MYSQL CODE
USE CafeDB;

CREATE TABLE menu (
     item_id INT AUTO_INCREMENT PRIMARY KEY,
     item_name VARCHAR(100),
     price FLOAT
 );

 CREATE TABLE orders (
     order_id INT AUTO_INCREMENT PRIMARY KEY,
     item_id INT,
     quantity INT,
     total_price DECIMAL(5,2),
     FOREIGN KEY (item_id) REFERENCES menu(item_id)# );

 insert into menu(item_name,price)values
 ('coffee',20),
 ('tea',10),
 ('lemon tea',30);

 SELECT * from menu


