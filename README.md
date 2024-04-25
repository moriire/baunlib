# BaunLib

BaunLib is a library component of Baun Eduvault, designed to provide access to a diverse range of educational materials focusing on STEAM (Science, Technology, Engineering, Arts, and Mathematics) and Robotics.

## Features

- **Comprehensive Collection:** BaunLib offers a rich repository of educational resources covering various topics in STEAM and Robotics, catering to learners of all levels.
- **User-Friendly Interface:** The frontend of BaunLib is built using Bootstrap 5, ensuring a responsive and intuitive user experience.
- **Robust Backend:** Powered by uvicorn server and MariaDB database, BaunLib's backend ensures efficient data management and retrieval.

## Installation

### Prerequisites

Before installing BaunLib, make sure you have the following prerequisites installed on your system:

- Python (with pip)
- MariaDB (or MySQL)

### Installation Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/roboticsbaun/baunlib.git
    ```

2. **Set Up the Backend:**

    - Navigate to the `backend` directory:

        ```bash
        cd baunlib/backend
        ```

    - Install Python dependencies:

        ```bash
        pip install -r requirements.txt
        ```

    - Set up the MariaDB database:

        - Create a new database and user:

            ```sql
            CREATE DATABASE baunlib_db;
            CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
            GRANT ALL PRIVILEGES ON baunlib_db.* TO 'user'@'localhost';
            FLUSH PRIVILEGES;
            ```

        - Update the database connection details in `config.py`.

    - Run the migration to set up the database schema:

        ```bash
        python manage.py migrate
        ```

    - Start the uvicorn server:

        ```bash
        uvicorn main:app --reload
        ```

3. **Set Up the Frontend:**

    - No installation required for the frontend as it's built with Bootstrap 5.

4. **Access BaunLib:**

    - BaunLib frontend should be accessible at `http://localhost:3000`.

## Usage

- Once BaunLib is installed and running, users can navigate through the frontend to browse, search, and access educational materials in various STEAM and Robotics subjects.

## License

This project is licensed under the [MIT License](LICENSE).
