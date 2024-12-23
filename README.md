# Finance-Agent

Finance-Agent is a comprehensive application designed to streamline financial data management through an intuitive user interface and a robust backend system. The project is divided into two main components: the **Frontend**, which offers a responsive and interactive user experience, and the **Backend**, which handles data processing and API services.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Available Scripts](#available-scripts)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Responsive Design**: Ensures optimal viewing across various devices.
- **Interactive Dashboards**: Visual representation of financial data.
- **Modular Components**: Reusable components for efficient development.
- **FastAPI Framework**: Utilizes FastAPI for building high-performance APIs.
- **Asynchronous Processing**: Supports asynchronous operations for improved performance.
- **Financial Data Management**: Handles various financial data operations, including retrieval, processing, and storage.

## Technologies Used

**Frontend**:

- React: JavaScript library for building user interfaces.
- Tailwind CSS: Utility-first CSS framework for rapid UI development.
- Vite: Next-generation frontend tooling for faster builds.
- TypeScript (if applicable): Adds static typing to JavaScript.

**Backend**:

- Python: Programming language for backend development.
- FastAPI: Modern, fast (high-performance) web framework for building APIs with Python.
- Uvicorn: ASGI server implementation for serving FastAPI applications.

## Getting Started

### Prerequisites

Ensure you have the following installed on your system:

- [Node.js](https://nodejs.org/)
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ayushs1214/Finance-Agent.git
   cd Finance-Agent
   ```

2. **Setting Up the Frontend**:

   - Navigate to the frontend directory:

     ```bash
     cd frontend
     ```

   - Install dependencies:

     ```bash
     npm install
     ```

   - Start the development server:

     ```bash
     npm run dev
     ```

   - The frontend application should now be running at `http://localhost:3000`.

3. **Setting Up the Backend**:

   - Navigate to the backend directory:

     ```bash
     cd ../backend
     ```

   - Create a virtual environment and activate it:

     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```

   - Install dependencies:

     ```bash
     pip install -r requirements.txt
     ```

   - Start the FastAPI server:

     ```bash
     uvicorn main:app --reload
     ```

   - The backend application will be accessible at `http://127.0.0.1:8000`.

## Project Structure

```
Finance-Agent/
├── backend/
│   ├── app/
│   │   ├── main.py         # Entry point for the FastAPI application
│   │   ├── models/         # Database models
│   │   ├── routers/        # API route definitions
│   │   ├── services/       # Business logic and data processing
│   │   └── tests/          # Test cases for the backend
│   ├── requirements.txt    # Backend dependencies
│   └── README.md           # Backend-specific documentation
├── frontend/
│   ├── public/             # Static assets
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Page components
│   │   ├── App.tsx         # Main application component
│   │   ├── main.tsx        # Entry point
│   │   ├── index.css       # Global styles
│   ├── package.json        # Frontend dependencies and scripts
│   ├── tailwind.config.js  # Tailwind CSS configuration
│   ├── tsconfig.json       # TypeScript configuration
│   └── README.md           # Frontend-specific documentation
├── .gitignore              # Git ignore file
└── README.md               # Project overview and documentation
```

## Available Scripts

**Frontend**:

- `npm start`: Starts the development server.
- `npm run build`: Builds the app for production.
- `npm run preview`: Previews the production build locally.
- `npm run lint`: Lints the codebase for errors and style issues.

**Backend**:

- `uvicorn main:app --reload`: Starts the FastAPI development server with live reload.
- `pytest`: Runs the backend test suite.

## Contributing

Contributions are welcome! Please fork the repository and create a new branch for your feature or bug fix. Submit a pull request for review, ensuring that your code adheres to the project's coding standards and includes appropriate tests.

Created with Love by Ayush Singh for Kedar, Appu, Bafna

---
