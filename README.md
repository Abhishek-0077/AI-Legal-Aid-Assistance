# AI-Legal-Aid-Assistance

## Description

AI-Legal-Aid-Assistance is an AI-powered tool designed to provide legal aid and assistance to users. It leverages a FastAPI backend for handling requests and an HTML frontend for user interaction. The system uses data preprocessing on IPC (Indian Penal Code) sections and integrates with a Language Model (LLM) to offer intelligent responses to legal queries.

## Features

- **Legal Query Assistance**: Users can input legal questions and receive AI-generated responses based on IPC sections.
- **Data Preprocessing**: Includes scripts for processing legal data from CSV files.
- **FastAPI Backend**: Robust API for handling user requests and integrating with the LLM.
- **HTML Frontend**: Simple web interface for easy access.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- A web browser to access the HTML frontend

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Abhishek-0077/AI-Legal-Aid-Assistance.git
   cd AI-Legal-Aid-Assistance
   ```

2. Install the required dependencies:
   ```
   pip install -r requirement.txt
   ```

## Usage

1. **Run the Backend**:
   Start the FastAPI server by running the backend script:
   ```
   python backend.py
   ```
   The server will start on `http://localhost:8000` (or the port specified in the code).

2. **Access the Frontend**:
   Open the `nyaya_sahayak.html` file in your web browser. You can do this by double-clicking the file or opening it directly in the browser.

3. **Interact with the Application**:
   - Enter your legal query in the provided interface.
   - The application will process the query using the backend and display the AI-generated response.

## Screenshots

Here are some screenshots of the application in action:

![Image1](image1.png)
*Description of Image1: Overview of the main interface.*

![Image2](image2.png)
*Description of Image2: Example of a query and response.*

## Project Structure

- `backend.py`: The main FastAPI application handling API requests.
- `data_preprocessing.ipynb`: Jupyter notebook for data preprocessing.
- `data_preprocessing.py`: Python script for data preprocessing.
- `ipc_sections (1).csv`: Dataset containing IPC sections.
- `LLM.py`: Script for integrating with the Language Model.
- `nyaya_sahayak.html`: HTML frontend for user interaction.
- `requirement.txt`: List of Python dependencies.
- `README.md`: This file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.