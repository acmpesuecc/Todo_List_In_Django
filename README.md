# Todo List In Django

## Build a Priority todo list in Django

In this app, you get to contribute to and help building a simple web app in which you can add, delete todos to a database.
We also fetch and display the todos according to their assigned priority.

## The Database used in this app
#### Consists of a single Todo table

With attributes id(Primary Key), title, content, created_at(timestamp) and priority

| id  | title  | content        | created_at | priority |
| --- | ------ | -------------- | ---------- | -------- |
| 1   | Todo 1 | Todo 1 Content | Date time  | 1        |
| 2   | Todo 2 | Todo 2 Content | Date time  | 2        |
| 3   | Todo 3 | Todo 3 Content | Date time  | 3        |
| 4   | Todo 4 | Todo 4 Content | Date time  | 1        |

## Functionalities

* `GET` - fetches all todos present in the database and displays them according to their priority field.
* `ADD` - creates a new todo and inserts it in the database.
* `DELETE` - Removes a specific todo (given id) from the database.

## Steps to replicate this project on your computer

1. Create a virtual environment - `python3 -m venv /path/to/new/virtual/environment`
2. Activate it
   - In Terminal - `source <venv>/bin/activate`
   - In cmd.exe - `<venv>\Scripts\activate.bat`
3. In case of difficulties, read more about Virtual environments [here](https://docs.python.org/3/library/venv.html).
4. To Install sqlite3, please go through this [link](https://www.servermania.com/kb/articles/install-sqlite/).
5. Install all the required modules for the project via `pip` with the command.

        `pip3 install -r requirements.txt`

6. This installs Django and other required packages.
7. To start the project and run the server - `cd Priority_Todo_List` and then run 

        `python3 manage.py runserver`

9. Similarly, to create a super user for the DB

        `python3 manage.py createsuperuser`
10. Make migrations

        `python3 manage.py makemigrations`
18. Migrate changes to the Database
        
        `python3 manage.py migrate`
 *NOTE* - The Commands above may not work as there are issues which you can solve by sending PRs to this repository!
