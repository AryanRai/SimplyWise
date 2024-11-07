# SimplyWise Shop Management System
Inventory Management Software/Web App using Python, SQL, eel, HTML and Javascript.

**SimplyWise** is a digital shop management system that centralizes customer records, transactions, inventory, and billing. It is designed to make business operations efficient, organized, and data-driven for small to medium-sized stores.
![91](https://github.com/AryanRai/ComputerSciProj/assets/31175254/825a2abc-8a1c-4893-b1ce-6a118f3f813e)
## Main Features

1. **Customer & Transaction Management**: Record customer details and track transaction history.
2. **Inventory Control**: Monitor stock levels and receive low-stock alerts.
3. **Analytics & Reporting**: Visualize sales trends and analyze customer behavior.
4. **Billing & Invoicing**: Generate invoices and manage payment records.
5. **Task Management**: Organize daily tasks and set reminders.
6. **User Access Control**: Define roles and permissions for team members.

## Home Page Sections

1. **Dashboard**: Overview of sales, recent activity, and inventory alerts.
2. **My Store**: Add and edit products, monitor inventory, and organize categories.
3. **Analytics**: Track sales trends, product performance, and customer demographics.
4. **To-Do**: Create, prioritize, and set reminders for tasks.
5. **Users**: Manage roles and permissions, monitor user activity.
6. **Billing**: Generate and track invoices, view billing history.

---


# Setup Guide

## Prerequisites

1. Python 3.7 or higher

-   MySQL Server

-   Required Python packages:
    
    pip  install  eel  mysql-connector-python
    

## Installation & Setup

-   Database Setup

-   Install MySQL Server

-   Create a root user with password 'root'

-   The application will automatically create the required database and tables

2. Application Files

-   Clone/download all project files

-   Ensure the following directory structure:
    
    SimplyWise/
    
    ├── main_sql.py
    
    ├── main_web.py
    
    ├── web/
    
    │ ├── login.html
    
    │ ├── main.html
    
    │ ├── inventory.html
    
    │ ├── transactions.html
    
    │ ├── todo.html
    
    │ ├── users.html
    
    │ ├── billing.html
    
    │ ├── mainstyle.css
    
    │ ├── mainscript.js
    
    │ ├── Simply.svg
    
    │ └── others/
    
    │ ├── intro.html
    
    │ ├── loginfailed.html
    
    │ ├── style.css
    
    │ ├── script.js
    
    │ └── images/
    

## Running the Application

1. Start the Application

python  main_sql.py

This will launch the web interface in your default browser.

-   Default Login Credentials

-   Username: admin

-   Password: root

## Usage Guide

### 1. Dashboard

-   View key metrics: Sales, Profits, Customers

-   Add custom metrics by clicking the "+" card

-   Edit values by clicking on respective cards

### 2. My Store (Inventory)

-   View all products with details

-   Add new items using "+" button

-   Edit quantities and costs by clicking on values

-   Delete items using trash icon or clicking item name

### 3. Analytics (Transactions)

-   Track all customer transactions

-   Add new transactions using "+" button

-   Update transaction status by clicking status indicator

-   View transaction history with customer details

### 4. Todo

-   Create and manage tasks

-   Toggle task status by clicking

-   Delete completed tasks using trash icon

-   Add new tasks using "+" button

### 5. Users

-   Manage user accounts and permissions

-   Add new users with "+" button

-   Edit passwords and access levels

-   Delete users using trash icon

### 6. Billing

-   Create and manage bills

-   Track item prices and quantities

-   Add new billing entries

-   Update prices automatically from inventory

## Security Features

-   Password-protected login system

-   Access level control for users

-   Secure database connections

-   Session management

## Troubleshooting

-   Database Connection Issues

-   Verify MySQL is running

-   Check credentials in main_sql.py

-   Ensure port 3306 is available

-   Web Interface Issues

-   Check if port 8080 is available

-   Clear browser cache

-   Verify all web files are in correct locations

-   Login Problems

-   Reset to default admin credentials

-   Check database connectivity

-   Verify user table exists

## Support

For additional support or feature requests, please create an issue in the project repository.

## License

This project is licensed under the MIT License - see the LICENSE file for details

SimplyWise simplifies shop management, enabling business owners to focus on growth and customer satisfaction.

Instructions in PDF
Sceenshots-
![88](https://github.com/AryanRai/ComputerSciProj/assets/31175254/8eedb109-f2d4-4760-adce-41c302d81b59)
![90](https://github.com/AryanRai/ComputerSciProj/assets/31175254/b2cb015a-e995-42a2-94b8-62118e07e4a3)
![91](https://github.com/AryanRai/ComputerSciProj/assets/31175254/825a2abc-8a1c-4893-b1ce-6a118f3f813e)
![92](https://github.com/AryanRai/ComputerSciProj/assets/31175254/0dbde71a-220e-41a5-b9c2-6e40c7cbf830)
![93](https://github.com/AryanRai/ComputerSciProj/assets/31175254/050feda7-74f7-4a6c-8073-99f07ae3c633)
