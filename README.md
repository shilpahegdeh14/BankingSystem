# Banking System Model

## Overview

This project is a model of a banking system implemented using Python Object-Oriented Programming (OOP) techniques. The system includes entities for customers, accounts, employees, and services like loans and credit cards. The data for each entities, for instance, customers, employees are stored in a JSON file, and the application is executable via the command line, accepting user inputs and returning results.
![Banking System Diagram](![Banking_system_OOP_mini_project drawio](https://github.com/user-attachments/assets/3426dfb0-7298-4bb8-b918-d523dfae9715)
)
## Project Structure

- **Entities**:
  - **Customer**: Represents a bank customer with properties such as first name, last name, phone, gender, and address.
  - **Account**: Represents a bank account with properties such as account type (checking/savings), deposit, withdrawal, and balance.
  - **Employee**: Represents a bank employee with relevant properties.
  - **Service**: Represents bank services like loans and credit cards with necessary properties.

- **Data Storage**:
  - Data is stored in a JSON file for persistence.
  
- **Command-Line Interface**:
  - The application is designed to be executed via the command line, accepting user inputs and providing results directly from the command line.

## Getting Started

### Prerequisites

- Python 3.x
- `json` module (included in the Python standard library)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/banking-system.git
   cd banking-system

2. Run the application:
   ```
   python main.py

3. Follow the command-line prompts to interact with the banking system. You can perform operations related to customers, accounts, and services based on the available options.

### Features
- Create and manage customer records.
- Open and manage different types of accounts (checking, savings).
- Perform deposits and withdrawals.
- Manage employee records.
- Handle bank services such as loans and credit cards.
- Store data in a JSON file.
- Exception handling and logging implemented.
