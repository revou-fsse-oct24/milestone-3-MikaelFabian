# RevoBank API

## Overview
RevoBank is a comprehensive banking API built with Python, Flask, and PostgreSQL.

## Features
- User Registration and Authentication
- JWT-based Authorization
- Secure Password Hashing
- Profile Management

## Setup and Installation
1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Set up environment variables
5. Initialize database: 
   - `flask db upgrade`
6. Run the application: 
   - `python run.py`

## API Endpoints
- POST /api/v1/users: Register a new user
- GET /api/v1/users/me: Get current user profile
- PUT /api/v1/users/me: Update user profile

## Technologies
- Flask
- SQLAlchemy
- PostgreSQL
- JWT Authentication