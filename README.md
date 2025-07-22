# Matrix-Sols-Assignment

# 🔗 URL Shortener
A powerful Flask-based web application that allows users to shorten long URLs, generate QR codes for easy sharing, and track the number of clicks on each shortened link through a dedicated analytics dashboard.

---
## 📌 About the Project

This project provides a robust solution for creating concise short URLs from lengthy ones. Beyond basic shortening, it enhances usability by generating scannable QR codes for each shortened link and offers an analytics dashboard to monitor click-through rates. Built with Flask and SQLite, it offers persistent storage for all created URLs and their visit statistics.

---
## 🚀 Features

-   **URL Shortening** – Convert long, unwieldy URLs into short, manageable links.
-   **Custom Short Codes** – Option to specify your own memorable short code instead of a randomly generated one.
-   **QR Code Generation** – Instantly generate a QR code for each shortened URL, perfect for print or digital sharing.
-   **URL Redirection** – Shortened links redirect seamlessly to their original destination.
-   **Visit Analytics** – Track the number of times each short URL has been visited.
-   **Analytics Dashboard** – A dedicated page to view all shortened URLs and their respective visit counts, with search functionality.
-   **Persistent Storage** – All URL mappings and visit data are stored in an SQLite database.
-   **CORS Enabled** – Configured for Cross-Origin Resource Sharing.

---

## 🛠️ Technology Stack

-   **Backend**: Python 3.x, Flask
-   **Database**: SQLite3 (managed with Flask-SQLAlchemy)
-   **URL Shortening/QR Code**: `qrcode`, `Pillow`
-   **Web Framework Extensions**: `Flask-SQLAlchemy`, `Flask-Cors`
-   **Frontend**: HTML, CSS (`style.css`)

---
## ⚙️ Getting Started

Follow these steps to set up and run the project locally.

### 📌 Prerequisites

-   Python 3.8+
-   `pip` (Python package installer)
-   Git (optional, for cloning the repository)

### 📥 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/URL_Shortener_Project.git](https://github.com/your-username/URL_Shortener_Project.git)
    cd URL_Shortener_Project
    ```
    (Replace `your-username` with your actual GitHub username if you're forking).

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 🛢️ Database Initialization

The SQLite database (`urls.db`) and its necessary tables will be automatically created the first time `app.py` is run, thanks to `db.create_all()` within the application context.

---

## 🧪 Usage

### Running the Application

1.  From the project's root directory, ensure your virtual environment is active.
2.  Run the Flask application:
    ```bash
    python app.py
    ```
3.  Open your web browser and navigate to:
    ```
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    ```

### Shortening a URL

1.  On the homepage, enter a long URL into the provided input field.
2.  Click the "Shorten" button.
3.  A short URL and a QR code will be displayed.

### Using Custom Short Codes

1.  On the homepage, enter a long URL.
2.  In the "Custom short code (optional)" field, type your desired short code (e.g., `my-link`).
3.  Click "Shorten". If the custom code is available, your URL will be shortened with that code. If it's taken, you'll receive an error.

### Viewing Analytics

1.  From the homepage, click on the "🔍 View Analytics" link.
2.  This will take you to the analytics dashboard, where you can see a list of all shortened URLs, their original links, and their visit counts. You can also use the search bar to filter entries.

---
Contributions are welcome! If you have any suggestions, bug reports, or want to contribute code, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

## Deployment:  https://matrix-sols-assignment.onrender.com

