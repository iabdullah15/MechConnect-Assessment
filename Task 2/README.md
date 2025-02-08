# Spare Parts API Documentation

## Overview
This Django REST API allows users to manage spare parts inventory, including creating, retrieving, updating, and deleting spare parts records. The API also supports filtering spare parts based on car model and price range (bonus task).

## Environment Setup

You can set up the Python environment using either `venv` or `pipenv`. Follow one of the methods below.

### Using `venv`

1. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   run:

   ```bash
   pip install -r requirements.txt
   ```

### Using `pipenv`

1. **Install pipenv (if not already installed):**
   ```bash
   pip install pipenv
   ```
2. **Create and Activate a New Pipenv Environment**
   ```bash
   pipenv shell
   ```
3. **Install Dependencies from requirements.txt**
   ```bash
   pipenv install --ignore-pipfile -r requirements.txt
   ```

## Authentication
The Django admin panel is accessible at `/admin` with the following credentials:

- **Username:** `abdu`
- **Password:** `123`

## API Endpoints

### **Spare Parts List and Create**
**Endpoint:** `/spare-parts/`

**Methods:**
- `GET` - Retrieves all spare parts, with optional filtering.
- `POST` - Creates a new spare part.

**Query Parameters:**
- `model` - Filter by car model (case-insensitive exact match).
- `min_price` - Filter parts greater than or equal to the specified price.
- `max_price` - Filter parts less than or equal to the specified price.

**Example Request:**
```bash
GET /spare-parts/?model=Toyota&min_price=100&max_price=500
```

**Example Request Body for POST:**
```json
{
  "part_name": "Brake Pad",
  "category": "Brakes",
  "part_number": "BP1234",
  "manufacturer": "Bosch",
  "description": "High-performance brake pad",
  "price": 150.00,
  "quantity": 10,
  "min_stock": 2,
  "car_model": {
    "manufacturer": "Toyota",
    "model": "Camry",
    "year": 2020
  },
  "supplier": "XYZ Motors"
}
```

### **Retrieve, Update, and Delete Spare Part**
**Endpoint:** `/spare-parts/<int:pk>`

**Methods:**
- `GET` - Retrieve a specific spare part by ID.
- `PUT` - Update a spare part.
- `DELETE` - Delete a spare part.

**Example Request:**
```bash
GET /spare-parts/1
```

**Example Request Body for PUT:**
```json
{
  "part_name": "Air Filter",
  "category": "Filters",
  "part_number": "AF5678",
  "manufacturer": "Toyota",
  "description": "High-efficiency air filter",
  "price": 75.00,
  "quantity": 20,
  "min_stock": 5,
  "car_model": {
    "manufacturer": "Toyota",
    "model": "Corolla",
    "year": 2019
  },
  "supplier": "John Doe"
}
```

### **Models**

#### **CarModel**
| Field | Type | Description |
|---|---|---|
| `manufacturer` | CharField | Manufacturer of the car. |
| `model` | CharField | Model name of the car. |
| `year` | PositiveIntegerField | Year of manufacture. |

#### **SparePart**
| Field | Type | Description |
|---|---|---|
| `part_name` | CharField | Name of the spare part. |
| `category` | CharField | Category of the spare part. |
| `part_number` | CharField | Unique identifier for the part. |
| `manufacturer` | CharField | Manufacturer of the part. |
| `description` | TextField | Additional details about the part. |
| `price` | DecimalField | Price of the part. |
| `quantity` | PositiveIntegerField | Available stock quantity. |
| `min_stock` | PositiveIntegerField | Minimum required stock before restocking. |
| `car_model` | ForeignKey | Associated car model. |
| `supplier` | CharField | Supplier of the part. |
| `added_on` | DateTimeField | Timestamp when the part was added. |
| `updated_on` | DateTimeField | Timestamp when the part was last updated. |
| `is_available` | BooleanField | Indicates if the part is in stock. |

## Available Car Models
The following car models are currently available for creating new spare parts:

- Ford Explorer 2016
- Honda Accord 2017
- Honda Civic 2023
- Toyota Camry 2015
- Toyota Corolla 2015

## Sample Requests

### **Create a New Car Model**
Please use the django admin panel to create/delete/update car models

### **Create a New Spare Part**
**Endpoint:** `/spare-parts/`

**Method:** `POST`

**Example Request Body:**
```json
{
  "part_name": "Engine Oil Filter",
  "category": "Filters",
  "part_number": "EOF789",
  "manufacturer": "Nissan",
  "description": "High-quality oil filter",
  "price": 50.00,
  "quantity": 15,
  "min_stock": 3,
  "car_model": {
    "manufacturer": "Ford",
    "model": "Explorer",
    "year": 2016
  },
  "supplier": "ABC Suppliers"
}
```

### **Important Note**
If you try to create a spare part for a car model that does not exist in the database, the API will return an error. Ensure the car model exists before attempting to create a spare part.

## Running the Django Server
Once your virtual environment is set up and dependencies are installed, start the Django development server:

```bash
python manage.py runserver
```

The API will be accessible at:
- `http://127.0.0.1:8000/spare-parts/`

