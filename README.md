# Learning Management System - API

## Project Requirements

- Python 3+
- FastAPI
- Uvicorn
- SQLAlchemy
- psycopg2-binary
- pydantic
- python-multipart
- python-dotenv
- Docker (if you want to run the project in docker container)

## Database Diagram

![Diagram](/public/DbDiagram.png)

[View Online](https://dbdiagram.io/d/67304c62e9daa85acae8f2ef)

## How to run

### Run on Your Local Machine

1. Create a virtual environment

```
python3 -m venv env
source env/bin/activate
```

2. cd into app

```
cd app
```

3. install requuirements

```
pip install -r requirements.txt
```

5. run the project

```
uvicorn main:app --reload
```

### Run on Docker

1.  cd into app

```
cd app
```

2. run the project

```
docker-compose up --build
```

3. shutdown the project (when needed)

```
docker-compose down
```

## View the project

- [http://localhost:8000/](http://localhost:8000/)
- [http://localhost:8000/docs](http://localhost:8000/docs) for testing APIs

## PayLoad Format

- JSON

```
{
  "departments": [{ "name": "string" }],
  "teachers": [{
    "name": "string",
    "department_name": "string"
  }],
  "courses": [{ "title": "string" }],
  "students": [{ "name": "string" }],
  "enrolleds": [{
    "student_name": "string",
    "course_title": "string"
  }],
  "courseTaughts": [
    {
      "teacher_name": "string",
      "course_title": "string",
      "department_name": "string"
    }
  ]
}
```

**Note**: All the parent fields are optional, but if you want a parent field then all its child fields are required.

## CSV Format

CSV file should be in the following format:

- For Departments:
  DepartmentName (String)
- For Teachers:
  TeacherName, DepartmentName (String)
- For Courses:
  CourseTitle (String)
- For Students:
  StudentName (String)
- For Enrolleds:
  StudentName, CourseTitle (String)
- For CourseTaughts:
  TeacherName, CourseTitle, DepartmentName (String)
