# Finance-Agent Backend

The Finance-Agent backend is a robust system designed to manage financial data and operations efficiently. It is built using Python and leverages the FastAPI framework to provide high-performance asynchronous capabilities.

## Features

- **FastAPI Framework**: Utilizes FastAPI for building APIs with automatic interactive documentation.

- **Asynchronous Processing**: Supports asynchronous operations for improved performance.

- **Financial Data Management**: Handles various financial data operations, including retrieval, processing, and storage.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ayushs1214/Finance-Agent.git
   ```

2. **Navigate to the Backend Directory**:

   ```bash
   cd Finance-Agent/backend
   ```

3. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Ensure that all necessary environment variables are set before running the application. Refer to the `.env.example` file for the required variables and create a `.env` file with appropriate values.

## Running the Application

After setting up the environment and installing dependencies, start the FastAPI server:

```bash
uvicorn main:app --reload
```

The application will be accessible at `http://127.0.0.1:8000`.

## Testing

To run tests, use the following command:

```bash
pytest
```

Ensure that all tests pass to verify the integrity of the application.

## Contributing

Contributions are welcome! Please fork the repository and create a new branch for your feature or bug fix. Submit a pull request for review.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

For more information, visit the [Finance-Agent GitHub repository](https://github.com/ayushs1214/Finance-Agent). 