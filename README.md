# Flask Project

## ✨ Description

Welcome to the Flask Project! This is a simple web application built using Flask that provides a secure interface for users to manage their accounts and submit complaints. The project includes user authentication, registration, and complaint submission functionalities.

## 🚀 Features

- **User Authentication**: Secure login and registration.
- **Complaint Submission**: Submit complaints via the web interface.
- **Session Management**: Persistent user sessions using Flask-Login.

## ⛓️ Installation

To get started with this project, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/gag3301v/flask_project.git
   cd flask_project
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```sh
   pip install Flask Flask-SQLAlchemy Flask-Login
   ```

4. **Initialize the Database**:
   ```sh
   python main.py --init-db
   ```

## 📦 Usage

Here’s how you can use the application:

1. **Run the Application**:
   ```sh
   python main.py
   ```

2. **Access the Web Interface**:
   Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. **Register an Account**:
   Visit the registration page, fill in the details, and create your account.

4. **Login**:
   Use your credentials to log in.

5. **Submit a Complaint**:
   Navigate to the complaint submission page and enter your complaint.

## 🔧 Configuration

- **Database URI**: Set the `DATABASE_URI` environment variable to configure the database connection.
  ```sh
  export DATABASE_URI=sqlite:///site.db
  ```

## 🧪 Tests

To run tests, use:

```sh
python -m unittest discover tests
```

## 📁 Project Structure

```
flask_project/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── forms.py
├── templates/
│   ├── base.html
│   ├── register.html
│   ├── login.html
│   └── complaint.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── scripts.js
├── tests/
│   ├── __init__.py
│   └── test_routes.py
├── main.py
└── requirements.txt
```

## 🙌 Contributing

Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) for more details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Owner**: gag3301v  
**Repository URL**: [https://github.com/gag3301v/flask_project](https://github.com/gag3301v/flask_project)

Feel free to star, fork, and contribute! 🌟