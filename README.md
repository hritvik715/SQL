# SQL NLP Query Assistant

## 📌 Project Overview
SQL NLP Query Assistant is a Python-based application that allows users to query a database using **natural language** instead of writing SQL manually. The project uses an AI model (Gemini) to convert user questions into SQL queries, executes them on a SQLite database, and displays the results in a simple and user-friendly way.

This project demonstrates the integration of **Natural Language Processing (NLP)** with **database querying**, making data access easier for non-technical users.

---

## 🚀 Problem Statement
Many users struggle to write SQL queries to fetch data from databases. This project solves that problem by allowing users to ask questions in plain English, which are then automatically converted into valid SQL queries and executed on the database.

---

## 💡 Solution
- User enters a natural language question  
- AI model converts the question into an SQL query  
- SQL query is executed on a SQLite database  
- Results are returned and displayed to the user  

Example:
- **Input:** “Provide the average marks of all students”
- **Generated SQL:** `SELECT AVG(marks) FROM STUDENT;`
- **Output:** `72.2`

---

## 🛠️ Technologies Used
- **Python**
- **SQLite**
- **Google Gemini API**
- **Natural Language Processing (NLP)**
- **Streamlit (for UI, if applicable)**

---

## 📂 Project Structure
├── app.py # Main application logic
├── sql.py # Database connection and SQL execution
├── student.db # SQLite database
├── test.py # Testing and experimentation
├── requirements.txt # Project dependencies
├── .env # API keys (not committed)




---

## ⚙️ How It Works
1. The user inputs a question in natural language  
2. The input is sent to the Gemini API  
3. Gemini generates a valid SQL query  
4. The query is executed on the SQLite database  
5. The result is displayed to the user  

---

## 🔐 Security Considerations
- Input validation is applied to avoid invalid queries
- SQL execution is controlled to prevent misuse
- API keys are stored securely using environment variables

---

## 📈 Future Improvements
- Support for multiple database tables
- Better result formatting
- Query history tracking
- Role-based access
- Migration to PostgreSQL for scalability

---

## 📌 Use Cases
- Learning SQL concepts
- Quick database querying
- AI-powered data exploration
- Educational demonstrations of NLP + SQL integration

---

## 👤 Author
**Hritvik Mohan**  
GitHub: https://github.com/hritvik715

---

## 📄 License
This project is for educational and demonstration purposes.
