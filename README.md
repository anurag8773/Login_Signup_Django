# Login_Signup_Django_MySQL

This project implements a secure login and signup system for patients and doctors within a hospital environment using Django as the web framework and MySQL as the database management system.

## Features

- Separate authentication mechanisms for patients and doctors.
- Robust user authentication with password hashing for security.
- User-friendly interfaces for registration and login processes.
- Customized dashboards for patients and doctors upon successful login.
- Doctor's access to patient information and appointment details.
- Patient access to personal medical records and the ability to schedule appointments.

## Requirements

- Python 3.x
- Django 3.x
- MySQL database
- Additional dependencies can be found in the `requirements.txt` file.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/hospital-login-signup-django.git
    ```

2. Navigate to the project directory:

    ```bash
    cd hospital-login-signup-django
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MySQL database:
   
   - Ensure MySQL is installed and running.
   - Update the database configurations in `settings.py`:

        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'your_database_name',
                'USER': 'your_database_user',
                'PASSWORD': 'your_database_password',
                'HOST': 'localhost',
                'PORT': '',
            }
        }
        ```

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application by visiting [http://localhost:8000](http://localhost:8000) in your web browser.

## Usage

1. Access the registration page to create a new account as either a patient or a doctor.
2. Log in using your registered credentials.
3. Explore the patient or doctor dashboard based on your account type.

## Contributing

Contributions are welcome! To contribute:
- Fork the repository.
- Create a new branch (`git checkout -b feature/new-feature`).
- Make your changes.
- Commit your changes (`git commit -am 'Add new feature'`).
- Push to the branch (`git push origin feature/new-feature`).
- Create a new Pull Request.


This README includes details specific to using Django with a MySQL database. Adjust the database configuration section based on your MySQL setup.
