# 🌤️ Cloud-Native Weather Dashboard

## 📋 Project Overview

A professional-grade weather tracking application that bridges real-time data with persistent cloud storage. This personal project demonstrates full-stack Python capabilities, focusing on cloud deployment, secure API handling, and relational database management.

* 🔍 **Real-Time Data**: Fetches live weather metrics using the OpenWeatherMap API.
* ☁️ **Cloud Persistence**: Integrated with **Supabase (PostgreSQL)** via SQLAlchemy for long-term data storage.
* 🚀 **Production Ready**: Fully deployed on **Streamlit Cloud** with secure secrets management.
* 📊 **CRUD Logic**: Implements Create and Read operations to track weather history across global sessions.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (Python-based interactive UI)
* **Database:** [Supabase](https://supabase.com/) (PostgreSQL)
* **ORM:** [SQLAlchemy](https://www.sqlalchemy.org/)
* **API:** OpenWeatherMap API
* **Deployment:** Streamlit Cloud

---

## 📥 Local Installation

To run this project on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/weather-project.git](https://github.com/yourusername/weather-project.git)
    cd weather-project
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Setup:**
    Create a `.env` file in the root directory:
    ```ini
    API_KEY = "your_openweathermap_key"
    DATABASE_URL = "postgresql://user:password@host:port/postgres"
    ```

---

## 🚀 Deployment & Secrets

This app is optimized for **Streamlit Cloud**. To maintain security, API keys and Database credentials are managed via **Streamlit Secrets** rather than hardcoded variables.

### Configuration in Streamlit Cloud Dashboard:
In your app settings, add the following to the **Secrets** box:
```toml
API_KEY = "your_openweathermap_api_key"
DATABASE_URL = "postgresql://postgres.[ID]:[PASSWORD]@[aws-1-eu-north-1.pooler.supabase.com:6543/postgres](https://aws-1-eu-north-1.pooler.supabase.com:6543/postgres)"