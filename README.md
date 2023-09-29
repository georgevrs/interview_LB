
# Interview_LB API

## Overview

This is a FastAPI based application to parse company information from text files and expose it via an HTTP API. The parsed information includes official name, GEMH number, website, and date of registration of companies.

## File Structure

- `create_tables.py`: Script to create the necessary tables in the database.
- `main.py`: The main file containing the FastAPI application.
- `models.py`: Contains the SQLAlchemy models for the project.
- `parser.py`: Parses the information from text files and populates the database.

## How to Run


1. **Set Up Virtual Environment (Optional but recommended)**
   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install Dependencies**
   ```shell
   pip install -r requirements.txt
   ```

3. **Create Database Tables**
   ```shell
   python create_tables.py
   ```

4. **Run the Parser**
   ```shell
   python parser.py
   ```

5. **Start the FastAPI application**
   ```shell
   uvicorn main:app --reload --port 8001
   ```

## API Endpoints

- `GET /company/{gemh_number}`: Retrieve company information based on the provided GEMH number.

## Database Configuration

This project is configured to use MySQL. Modify the `DATABASE_URL` in `models.py` to point to the correct database instance.

## License

[MIT](LICENSE)
