
# SimplyWise Shop Management System

**SimplyWise** is an inventory management software/web app that centralizes customer records, transactions, inventory, and billing. It helps business owners efficiently manage operations, monitor sales, and track inventory for small to medium-sized stores.

**Technologies used:**
- Python
- SQL
- Eel (Python web framework)
- HTML, CSS, JavaScript

![SimplyWise Dashboard](https://github.com/AryanRai/ComputerSciProj/assets/31175254/825a2abc-8a1c-4893-b1ce-6a118f3f813e)

## Main Features

1. **Customer & Transaction Management**: Manage customer details and track transaction history.
2. **Inventory Control**: Monitor stock levels and get low-stock alerts.
3. **Analytics & Reporting**: Visualize sales trends and analyze customer behavior.
4. **Billing & Invoicing**: Generate invoices and manage payment records.
5. **Task Management**: Organize daily tasks and set reminders.
6. **User Access Control**: Define roles and permissions for team members.

## Home Page Sections

1. **Dashboard**: Overview of sales, recent activity, and inventory alerts.
2. **My Store**: Add/edit products, monitor inventory, and organize categories.
3. **Analytics**: Track sales trends, product performance, and customer demographics.
4. **To-Do**: Create and manage tasks and reminders.
5. **Users**: Manage roles, permissions, and user activity.
6. **Billing**: Generate and track invoices.

---

# Setup Guide

## Prerequisites

1. **Python 3.7 or higher**
2. **MySQL Server**
3. Required Python packages:
   ```bash
   pip install eel mysql-connector-python
   ```

## Installation & Setup

### Database Setup
1. Install MySQL Server.
2. Create a root user with password `root`.
3. The application will automatically create the required database and tables.

### Application Files

- Clone or download all project files.
- Ensure the following directory structure:

```
SimplyWise/
├── main_sql.py
├── main_web.py
├── web/
│   ├── login.html
│   ├── main.html
│   ├── inventory.html
│   ├── transactions.html
│   ├── todo.html
│   ├── users.html
│   ├── billing.html
│   ├── mainstyle.css
│   ├── mainscript.js
│   ├── Simply.svg
│   └── others/
│       ├── intro.html
│       ├── loginfailed.html
│       ├── style.css
│       ├── script.js
│       └── images/
```

## Running the Application

1. **Start the application:**
   ```bash
   python main_sql.py
   ```
   This will launch the web interface in your default browser.

2. **Default Login Credentials:**
   - Username: `admin`
   - Password: `root`

---

# Usage Guide

### 1. Dashboard
- View key metrics: Sales, Profits, Customers.
- Add custom metrics via the "+" card.
- Edit values by clicking on respective cards.

### 2. My Store (Inventory)
- View all products with details.
- Add new items using the "+" button.
- Edit quantities and costs by clicking values.
- Delete items using the trash icon or clicking item names.

### 3. Analytics (Transactions)
- Track all customer transactions.
- Add new transactions via the "+" button.
- Update transaction status by clicking status indicator.
- View transaction history with customer details.

### 4. To-Do
- Create and manage tasks.
- Toggle task status by clicking.
- Delete completed tasks using the trash icon.
- Add new tasks with the "+" button.

### 5. Users
- Manage user accounts and permissions.
- Add new users with the "+" button.
- Edit passwords and access levels.
- Delete users via the trash icon.

### 6. Billing
- Create and manage bills.
- Track item prices and quantities.
- Add new billing entries.
- Update prices automatically from inventory.

---

# Security Features

- Password-protected login system.
- Access level control for users.
- Secure database connections.
- Session management.

---

# Troubleshooting

### Database Connection Issues
- Verify MySQL is running.
- Check credentials in `main_sql.py`.
- Ensure port 3306 is available.

### Web Interface Issues
- Verify if port 8080 is available.
- Clear your browser cache.
- Ensure all web files are in correct locations.

### Login Problems
- Reset to default admin credentials.
- Check database connectivity.
- Verify the user table exists.

---

# Support

For additional support or feature requests, please create an issue in the project repository.

---

# License

This project is licensed under the MIT License - see the LICENSE file for details.

---

SimplyWise simplifies shop management, allowing business owners to focus on growth and customer satisfaction.

**Instructions in PDF**  
**Screenshots**:

![Screenshot 1](https://github.com/AryanRai/ComputerSciProj/assets/31175254/8eedb109-f2d4-4760-adce-41c302d81b59)  
![Screenshot 2](https://github.com/AryanRai/ComputerSciProj/assets/31175254/b2cb015a-e995-42a2-94b8-62118e07e4a3)  
![Screenshot 3](https://github.com/AryanRai/ComputerSciProj/assets/31175254/825a2abc-8a1c-4893-b1ce-6a118f3f813e)  
![Screenshot 4](https://github.com/AryanRai/ComputerSciProj/assets/31175254/0dbde71a-220e-41a5-b9c2-6e40c7cbf830)  
![Screenshot 5](https://github.com/AryanRai/ComputerSciProj/assets/31175254/050feda7-74f7-4a6c-8073-99f07ae3c633)

--- 

