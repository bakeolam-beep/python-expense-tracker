Expense Tracker (Python Desktop Application)
Project Overview

The Expense Tracker is a Python desktop application designed to help users record, organize, and visualize their daily expenses.

The application provides a simple graphical interface that allows users to log spending, categorize transactions, and analyze spending behavior through charts.

This project was built as a practical software engineering exercise to demonstrate:

• GUI development
• Data persistence
• Data visualization
• Debugging and software iteration

The application uses Python with Tkinter for the graphical interface and SQLite for storing expense records.

Features

Current features implemented in the application include:

Expense Entry

Users can record new expenses by entering:

Expense category
Amount spent
Description
Date
Expense Storage

All expenses are stored locally using SQLite, ensuring persistent data even after the application closes.

Expense Table View

Users can view all recorded expenses in a structured table format within the application interface.

Data Visualization

The application can generate charts showing how expenses are distributed across categories using Matplotlib.

Expense Management

Users can review and manage previous expense entries easily through the GUI.

Tech Stack

The application is built using the following technologies:

Component	Technology
Programming Language	Python
GUI Framework	Tkinter
Database	SQLite
Data Visualization	Matplotlib
Version Control	Git
Installation

Follow these steps to run the project locally.

1. Clone the repository
git clone https://github.com/yourusername/python-expense-tracker.git
2. Navigate to the project folder
cd python-expense-tracker
3. Install dependencies
pip install matplotlib
4. Run the application
python main.py

The application window should open and allow you to begin recording expenses.

Future Improvements

The following enhancements are planned to improve the application:

Advanced Analytics

Add monthly summaries and financial insights such as:

Monthly spending reports
Category spending breakdown
Expense trends
Export Functionality

Allow users to export expense data to:

CSV files
Excel spreadsheets
Modern User Interface

Upgrade the interface using CustomTkinter for a more modern desktop experience.

Web Application Version

Convert the project into a web-based platform using:

• FastAPI
• React

This would enable multi-device access and cloud storage.

Learning Outcomes

Through this project, I gained practical experience in:

• Building desktop applications
• Designing database-backed systems
• Implementing data visualization
• Debugging GUI applications
• Structuring small-scale software projects
