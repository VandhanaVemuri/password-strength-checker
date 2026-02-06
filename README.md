# 🔐 Password Strength Checker

A **Python Flask web application** that checks the strength of a password based on
length, character variety, entropy, and common weak patterns.  
The application provides clear feedback and suggestions through a clean, modern UI.

---

## 🚀 Features

- Password strength detection (**Weak / Medium / Strong**)
- Entropy calculation
- Suggestions for creating stronger passwords
- Clean and responsive user interface
- Flask backend with HTML & CSS frontend

---

## 🛠 Tech Stack

- **Python**
- **Flask**
- **HTML**
- **CSS**

---

## 📂 Project Structure

password-strength-checker/
├── app.py
├── password_checker.py
├── templates/
│ └── index.html
├── static/
│ └── style.css
└── README.md


---

## ▶️ How to Run Locally

### 1️⃣ Clone or Download the Repository
- Click **Code → Download ZIP**, or
- Clone using Git:
```bash
git clone https://github.com/your-username/password-strength-checker.git
## 2️⃣ Navigate to the Project Folder
cd password-strength-checker

## 3️⃣ Install Dependencies
pip install flask

## 4️⃣ Run the Application
python app.py


You should see:

Running on http://127.0.0.1:5000/

## 5️⃣ Open in Browser

Open your browser and go to:

http://127.0.0.1:5000/

⚠️ Important Note

❌ Do NOT open index.html directly in the browser
This is a Flask web application, not a static website.

✔ Always run the app using:

python app.py


✔ Then open:

http://127.0.0.1:5000/

📌 Future Improvements

Live password strength meter (JavaScript)

Password breach detection (Have I Been Pwned API)

User authentication

Deploy the app online

🧠 What I Learned

Building a Flask backend

Using templates and static files in Flask

Connecting frontend and backend

Debugging real-world path and deployment issues

Writing clean project documentation
