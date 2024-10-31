 

# My FastAPI Todo Project

## Introduction
This project is a task management system developed using **FastAPI** as the API framework and **SQLAlchemy** for database management. It’s designed to be flexible and user-friendly, with a professional structure and modern technologies to ensure high performance and easy maintenance.

## Features
- **Add Tasks**: Add new tasks with multiple properties.
- **Update Tasks**: Support for updating task information through a dedicated API.
- **Delete Tasks**: Remove unwanted tasks from the database.
- **View Tasks**: Retrieve a list of available tasks with detailed information.

## Requirements
To run the project, the following requirements are needed:
- Python 3.7 or higher
- Python libraries:
  - FastAPI
  - SQLAlchemy
  - Pydantic

Install the required packages using `requirements.txt` (if available):

```bash
pip install -r requirements.txt
```

## Usage
1. First, initialize the database by running the following command:

    ```bash
    # Database initialization command
    python init_db.py
    ```

2. Start the server with this command:

    ```bash
    uvicorn main:app --reload
    ```

3. Access the interactive API documentation at:
    ```
    http://127.0.0.1:8000/docs
    ```

## Project Structure
- `main.py`: The main application entry point.
- `db/database.py`: Database connection settings.
- `app/models/`: Contains database models.
- `app/schemas/`: Contains the schemas used in the API.

## Contribution
Contributions are welcome! Please open a pull request with your proposed changes. Ensure that all modifications adhere to the project's guidelines.

## License
This project is licensed under the MIT License.


