
### README for FastAPI Application

#### Description
This FastAPI application provides a simple yet efficient way to manage and retrieve account and invoice details. It's built using Python and FastAPI, and can be containerized using Docker for easy deployment.

#### Features
- **Account Management**: Fetch account details, including account numbers and names.
- **Invoice Handling**: Interface to deal with invoice-related data (further details would require analysis of the code).

#### Installation
1. **Clone the Repository**:
   ```bash
   git clone [repository-url]
   cd fast_api_app
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

#### Running the Application
1. **Normal Execution**:
   ```bash
   python modified_fastapi_app.py
   ```
   The application will be available at `http://localhost:8000`.

2. **Using Docker**:
   - Build the Docker image:
     ```bash
     docker build -t fast_api_app .
     ```
   - Run the container:
     ```bash
     docker run -d -p 8000:8000 fast_api_app
     ```
   The application will be available at `http://localhost:8000`.

#### API Endpoints
1. **List Accounts**:
   - `GET /account/list`: Fetches a list of account numbers and names.
2. **Account Details**:
   - `GET /account/details/{account_num}`: Retrieves full account details for a given account number.

#### Data Files
- `account_details.csv`
- `invoice_details.csv`

These files are used within the application to store and manage account and invoice information.
