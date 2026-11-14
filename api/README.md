# SAH QR Code Generator — Web Application

A web-based QR code generator built with **Python, FastAPI, and Jinja2**, powered by the [`sah-qr-generator`](https://pypi.org/project/sah-qr-generator/) Python package.

The application allows users to generate QR codes from text or URLs, customize foreground and background colors, preview the generated QR code, and download it as a PNG image.

🌐 **Live Demo:** https://sah-qr-generator.onrender.com/

---

## Features

- **QR Code Generation:** Generate QR codes from text or URLs.
- **Color Customization:** Choose foreground and background colors.
- **Instant Preview:** Display the generated QR code directly on the page.
- **PNG Download:** Download generated QR codes as PNG images.
- **Input Validation:** Handle empty inputs, unsupported colors, and data that exceeds QR code capacity.
- **No Registration Required:** Generate QR codes without creating an account.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Web framework |
| Jinja2 | HTML templating |
| Pillow | Image processing |
| QRCode | QR code generation dependency |
| HTML5 | Page structure |
| CSS3 | Styling and responsive layout |
| Pytest | Automated testing |

The application uses the `sah-qr-generator` package for its core QR generation functionality.

---

## Project Structure

```text
api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── pages.py
│   │
│   ├── service/
│   │   ├── __init__.py
│   │   └── qr_service.py
│   │
│   ├── exceptions/
│   │   └── __init__.py
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── images/
│
├── assets/
│   └── logo/
│       └── icon_bw.png
│
├── tests/
│   ├── test_qr_service.py
│   └── test_routes.py
│
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

### Architecture

The application follows a simple separation of responsibilities:

- **Routes:** Handle incoming HTTP requests and return HTML pages or generated images.
- **Service:** Contains the application-level QR generation logic, including color validation and interaction with the QR generation package.
- **Templates:** Contains the Jinja2 HTML templates.
- **Static:** Contains CSS and frontend assets.
- **Tests:** Contains automated tests for the service and application routes.

The core QR generation functionality is maintained separately in the `sah-qr-generator` Python package.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ahmed122000/QR-Code-Generator.git
```

Navigate to the API directory:

```bash
cd QR-Code-Generator/api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Linux / macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

For running the application:

```bash
pip install -r requirements.txt
```

For development and testing:

```bash
pip install -r requirements-dev.txt
```

---

## Running the Application

Start the development server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

Open the URL in your browser to access the QR code generator.

---

## Application Routes

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Displays the QR code generator page |
| POST | `/generate-qr` | Generates a QR code and displays its preview |
| POST | `/download-qr` | Generates and returns the QR code as a downloadable PNG |

### 1. Home Page

```http
GET /
```

Displays the main page containing the QR generation form.

### 2. Generate QR Code

```http
POST /generate-qr
```

Accepts form data:

| Parameter | Description |
|---|---|
| `data` | Text or URL to encode |
| `fg_color` | QR code foreground color |
| `bg_color` | QR code background color |

Returns the HTML page with the generated QR code preview or an error message.

### 3. Download QR Code

```http
POST /download-qr
```

Accepts the same form parameters and returns the generated QR code as a PNG image.

The response uses:

```http
Content-Type: image/png
Content-Disposition: attachment; filename="qr.png"
```

---

## Running Tests

The project uses Pytest for automated testing.

From the `api/` directory, run:

```bash
pytest
```

To get a more detailed test report:

```bash
pytest -v
```

---

## Deployment

The application is deployed using [Render](https://render.com/).

Deployment configuration:

| Setting | Value |
|---|---|
| Runtime | Python 3 |
| Root Directory | `api` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |

Render provides the `PORT` environment variable used by Uvicorn to bind the application to the correct port.

---

## Related Project

The core QR generation functionality is available as a standalone Python package:

**[SAH QR Generator — PyPI](https://pypi.org/project/sah-qr-generator/)**

---

## License

This project is licensed under the MIT License.