# Cat Fact Project - Omair Ansari

## Description
The Cat Fact Project is a Django application that provides endpoints to fetch and display cat facts. It includes functionality to fetch cat facts from an external API asynchronously and retrieve the last fetched fact.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/oansari22/Leap-App-Cat-Fact.git
   ```

2. Navigate to the project directory:
   ```
   cd Leap-App-Cat-Fact
   ```

3. Create and activate a virtual environment (optional but recommended):
   - On Windows:
     ```
     python -m venv myenv
     myenv\Scripts\activate
     ```

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run migrations:
   ```
   python manage.py migrate
   ```

2. Start the development server:
   ```
   python manage.py runserver
   ```
3. **Start the Dramatiq worker**:
   ```
   python manage.py rundramatiq
   ```

4. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Endpoints
Click on the url to check the endpoints hosted on [pythonanywhere.com](https://www.pythonanywhere.com/)
- `/health_check`: Returns status code 200 when the application is running.  [URL](https://oansari22.pythonanywhere.com/health_check/)
- `/fetch_fact`: Queues an async task to fetch data from an external cat fact API. [URL](https://oansari22.pythonanywhere.com/fetch_fact/)
- `/get_fact`: Returns the first cat fact fetched from the `/fetch_fact` endpoint. If no task has been queued yet, it returns an appropriate error message. [URL](https://oansari22.pythonanywhere.com/get_fact/)
