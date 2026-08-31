# ☎️ Telephone Directory System

A menu-driven **Telephone Directory Management System** built with Python and text-file storage.

<p align="center">
  <i>A practical implementation of file handling, record management, validation, and modular programming.</i>
</p>

---

## 📌 About the Project

The **Telephone Directory System** is a terminal-based application developed to manage departments, employees, and telephone records using Python.

The project focuses on understanding how structured data can be stored, retrieved, searched, and managed using **file handling**, without relying on a traditional database.

The application is divided into independent modules for department, employee, and telephone management, with text files used for persistent storage.

---

## ✨ Features

### 🔐 Login
- Employee ID-based login
- Validates users against employee records

### 🏢 Department Management
- Add departments
- Automatic sequential Department Code generation
- Duplicate department validation
- Department record listing

### 👤 Employee Management
- Add employees
- Automatic sequential Employee ID generation
- Employee detail validation
- Department selection using existing Department Codes
- Automatic Department Name association
- Employee record listing

### ☎️ Telephone Directory
- Add telephone numbers for existing employees
- Automatic department-based telephone number generation
- Sequential telephone number allocation
- Employee location and department details retrieved from employee records

### 🔎 Telephone Enquiry
- Search by Employee Name
- Case-insensitive name search
- Search by Telephone Number
- Display corresponding employee and department details

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3** | Application development |
| **Text Files** | Data storage |
| **Git** | Version control |
| **GitHub** | Source code management |

---

## 📂 Project Structure

```text
telephone-directory-system/
│
├── main.py
├── utilities.py
├── dept.py
├── emp.py
├── tel.py
│
├── dept.txt
├── emp.txt
├── tel.txt
│
└── ProjectSpecs_PF.pdf
