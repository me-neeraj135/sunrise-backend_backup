# Flask REST API Project

This is a simple REST API built with Flask, featuring interactive API documentation with Swagger.

## Project Structure

flask_rest_api/
│
├── app/
│ ├── init.py # Initialize the Flask app and Swagger
│ ├── models.py # Define data models (if any)
│ ├── routes.py # Define API routes
│
├── venv/ # Virtual environment
├── app.py # Entry point of the application
├── requirements.txt # Project dependencies
├── README.md # Project overview and setup instructions



## Setup Instructions

### Prerequisites

- Python 3.7+
- Virtual environment (`venv`)

### Installation

Clone the repository:

   ```sh
   git clone https://github.com/javedansari81/sunrise-backend.git
   cd sunrise-backend

## Create and activate a virtual environment:

python -m venv venv
.\venv\Scripts\activate   # For Windows
source venv/bin/activate  # For macOS/Linux

## Install the dependencies

pip install -r requirements.txt

## Start the Flask application:
python app.py

Access the Swagger UI for interactive API documentation at http://127.0.0.1:5000/apidocs/
