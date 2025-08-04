## SmartForm – Intelligent Recruitment Form
A full-featured intelligent web form, designed for efficient recruitment data collection. Includes dynamic multi-tab sections, advanced field validation, file uploads, and automatic document generation.

## 🛠️ Technologies Used
- Python 3
- Django
- Bootstrap 5
- crispy-forms
- django-recaptcha
- htmx
- SQLite (local mode)
- PostgreSQL (production mode)
- Playwright (E2E testing)
- Postman + Newman (API testing)

## 🚀 Features
- Multi-tab form structure collecting:
  - Personal info
  - Identity
  - Contact
  - Family
  - Education
  - Experience
  - Financial data
  - Legal Situation

- Dynamic field validation

- Basic built-in security features

## ⚙️ Local Setup
Clone the repository:

``` bash
git clone https://github.com/Pizofh/SmartForm.git
cd SmartForm
```

Create and activate a virtual environment:

```bash
python -m venv venv
```
- Windows
```bash
.\venv\Scripts\activate
```
- Unix/macOS
```bash
source venv/bin/activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```

Apply database migrations:
```bash
python manage.py migrate
```

Run the development server:
```bash
python manage.py runserver
```

Then open in your browser:

http://127.0.0.1:8000/

## 📂 Automated Testing
This project includes full automated testing coverage.

## ▶️ End-to-End Tests (Playwright)
- e2e-tests/HappyPath.spec.ts: full successful user flow

- e2e-tests/SadPath.spec.ts: validation for required fields

- e2e-tests/SadPathValidators.spec.ts: edge cases for custom validators across tabs

Run Playwright tests:
```bash
npx playwright install
npx playwright test
```
Generate trace report:
```bash
npx playwright test --trace on
```
View trace report: 
```bash
npx playwright show-trace
```
## 📡 API Tests (Postman + Newman)


Run Postman collection via Newman:
``` bash
npx newman run e2e-tests/SmartFormAPITests.postman_collection.json

```

## 👤 Author
**Brian Steve Garnica Sandoval**
[LinkedIn Profile](https://www.linkedin.com/in/steve-garnica)
DevOps Engineer

_This project is part of a real-world DevOps portfolio. Designed, tested, and deployed to reflect full-cycle engineering practices._

