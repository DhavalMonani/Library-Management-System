﻿# Library Management TDD (Incubyte) Kata Solution

Welcome to my solution for the Library Management Kata! This repository showcases the use of Test-Driven Development (TDD) to solve a programming problem, emphasizing small, incremental commits and clear, concise code.

## Table of Contents

- [Problem Statement](#problem-statement)
- [Requirements](#requirements)
- [Solution](#solution)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Directory Structure](#directory structure)
  - [Running Tests](#running-tests)

## Problem Statement

Create a simple library management system that allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books.

### Requirements

- **Add Books**:
  - Users should be able to add new books to the library.
  - Each book should have a unique identifier (e.g., ISBN), title, author, and publication year.

- **Borrow Books**:
  - Users should be able to borrow a book from the library.
  - The system should ensure that the book is available before allowing it to be borrowed.
  - If the book is not available, the system should raise an appropriate error.

- **Return Books**:
  - Users should be able to return a borrowed book.
  - The system should update the availability of the book accordingly.

- **View Available Books**:
  - Users should be able to view a list of all available books in the library.

For a detailed problem statement and requirements, view problem statement file.

## Solution

This project follows TDD principles to solve the kata problem. The solution is built with small, incremental commits, ensuring that each feature is developed and tested in isolation, demonstrating effective TDD practices.

## Features

### User Management

- **add_user**:
  - Adds a new user to the library's user catalog.
  - Validates that the user is not null.
  - Throws an exception if the user already exists.

- **view_user**:
  - Retrieves a user from the library by their username.
  - Returns empty string if the user is not found.

### Book Management

- **add_books**:
  - Allows a user to add a book to the library's inventory.
  - Validates that the user is a librarian.
  - Ensures the book is not null.
  - Throws an exception if the user is unauthorized.

- **view_all_books**:
  - Returns a list of all books currently available in the library.
  - Ensures the list is unmodifiable.

### Borrowing and Returning Books

- **borrow_book**:
  - Allows a user to borrow a book from the library.
  - Validates that the book is not already borrowed.
  - Throws an exception if the book is already borrowed.

- **return_book**:
  - Allows a user to return a borrowed book to the library.
  - Validates that the book was borrowed by the same user.

1. Prerequisites
    Python 3.8+: Ensure Python is installed on your system.

    Code Editor/IDE: Use any editor like VS Code, PyCharm, or Jupyter Notebook.

    Standard Library: The project only uses Python's built-in libraries (no additional installation required).
2. Clone the Repository:
    
    git clone <repository-url>
    cd <repository-folder>

OR
Download ZIP:
Download the project as a ZIP file and extract it to your desired directory.

3. Directory Structure
    LibraryManagement/
    │
    ├── Library.py         # Core Library class and functionality. 
    ├── user.py         # User class with role-based details.
    ├── test_library.py # Unit tests for the project.
    ├── validate_data.py # for validating empty details.
    └── README.md       # Documentation.

4. Running Tests
    1. Run All Tests:
        python -m unittest test_library.py
