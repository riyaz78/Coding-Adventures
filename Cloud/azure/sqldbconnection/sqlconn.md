#Azure SQL Database Connection Using Python

This guide describes how to connect to an Azure SQL Database using Python and the 'pyodbc' library.

## Prerequisites

- Python installed on your machine
- An Azure SQL Database
- The 'pyodbc' python package.

## Installation

1. Install the 'pyodbc' package using pip:

```bash
pip install pyodbc
```

2. Install the ODBC server

## Configuration

1. Obtain your Azure SQL Database connection details (server name, database name, username and password)
2. Find your database's ODBC connection string from the Azure Portal.

## Usage

1. Replace the placeholder values in the script with your actual connection details.
2. Execute the script to connect to your Azure SQL database and perform queries