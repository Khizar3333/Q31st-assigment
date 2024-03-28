# Fastapi Todos app

This is a simple **Todo App** built using FastAPI that allows you to manage a list of students.

## Features

* Retrieve a list of all students.
* Get details of a single student by roll number.
* Add a new student.
* Update student information.
* Delete a student.

### Installation

Clone this repository:

git clone https://github.com/yourusername/fastapi-todo-app.git


### Setup

we use poetry as package manager,to install poetry on windown you need to run below command


```bash
pipx install poetry
```

**you also need to install pipx, for this run these commands**

pip install --user pipx

pipx ensurepath

**you can also install it using scoop**

scoop install pipx

**Now install fastapi and uvicorn**
pip install fastapi

pip install "uvicorn[standard]"


## Usage

add these lines in pyproject.toml file

[tool.poetry.scripts]
dev= "todos.main:start"

Run the FastAPI server

poetry run dev


1. Access the API at http://127.0.0.1:8000.

## Endpoints

### 1. Get All Students

* **URL:** `/students`
* **Method:** `GET`
* **Response**

[
    {
        "name": "khizar",
        "rollno": 30,
        "age": 21,
        "section": "A"
    }
]


## . Get Single Student by Roll Number

* **URL:** `/singlestudent?rollno={roll_number}`
* **Method:** `GET`
* **Parameters:**
  * `rollno` (integer): Roll number of the student.
* **Response**

{
    "name": "khizar",
    "rollno": 30,
    "age": 21,
    "section": "A"
}


## Add a New Student

* **URL:** `/students`
* **Method:** `POST`
* **Request Body:**

{
    "name": "John Doe",
    "rollno": 31,
    "age": 22,
    "section": "B"
}



## Update Student Information

* **URL:** `/students/{student_id}`
* **Method:** `PUT`
* **Path Parameters:**
  * `student_id` (integer): Roll number of the student to update.
* **Request Body (Example)**

{
    "name": "Updated Name",
    "rollno": 30,
    "age": 23,
    "section": "C"
}



## 5. Delete a Student

* **URL:** `/students/{student_id}`
* **Method:** `DELETE`
* **Path Parameters:**
* `student_id` (integer): Roll number of the student to delete.
* **Response (Success)**

{
    "message": "Student with roll number 30 deleted successfully."
}
