# Image Builder

## Getting Started

### Clone the Repository
First, clone the repository to your local machine using the following command:

```bash
$ git clone https://github.com/raheemiqram/pixel_to_image.git
```

### Install Dependencies
Ensure that Python 3 and pip3 are installed on your system. Navigate to the project's root directory and install the required dependencies using pip:

```bash
$ pip install -r ./requirements/local.txt
```

Consider using a virtual environment for isolation.

### Running the Project

#### Using Makefile
If you have Make installed, you can simply run the project using the provided Makefile. Execute the following command:

```bash
$ make run
```

#### Without Makefile
If you don't have Make installed, you can still run the project by executing the following commands:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py test_data
$ python manage.py runserver
```

### Accessing the Application

Once the server is running, you can access the application via your web browser:

```bash
http://127.0.0.1:8000/
```

Login credentials:

- Username: admin@admin.com
- Password: admin@admin.com

### Demo Link

You can also access a demo version of the application online:

```bash
https://raheemiqram.pythonanywhere.com/
```

Login credentials are the same as above.

## Running Tests

To execute the test cases, run the following command:

```bash
$ make test
```

## Screenshots
![Screenshot Description](readme_data/1.png)
![Screenshot Description](readme_data/2.png)
![Screenshot Description](readme_data/3.png)
![Screenshot Description](readme_data/4.png)