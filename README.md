# SAH QR Code Generator

[![PyPI version](https://badge.fury.io/py/sah-qr-generator.svg)](https://pypi.org/project/sah-qr-generator/)
[![Python versions](https://img.shields.io/pypi/pyversions/sah-qr-generator)](https://pypi.org/project/sah-qr-generator/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A Python-based QR code generation project that provides both a reusable Python library and a web application.

Generate QR codes from URLs or plain text, customize their appearance, add an optional center icon, and export them as image files.

**🌐 Live Demo:** [SAH QR Code Generator](https://sah-qr-generator.onrender.com/)

**📦 PyPI Package:** [sah-qr-generator](https://pypi.org/project/sah-qr-generator/)

---

## Project Overview

This repository contains two main components:

### 1. QR Generator Library

A reusable Python package that provides the core QR code generation functionality.

- Available on PyPI.
- Provides a command-line interface (CLI).
- Can be integrated into other Python applications.
- Supports custom colors and optional center icons.
- Supports PNG, JPG, and JPEG output formats.

### 2. Web Application

A web-based QR code generator built with FastAPI and Jinja2.

- Generate QR codes directly from your browser.
- Customize foreground and background colors.
- Preview generated QR codes instantly.
- Download QR codes as PNG images.
- No registration or database required.

The web application uses the published `sah-qr-generator` package rather than duplicating its core generation logic.

---

## Architecture

The project separates the QR generation functionality from the web application.

```text
User
 │
 ├── Command Line Interface
 │       │
 │       ▼
 │   QR Generator Library
 │
 └── Web Browser
         │
         ▼
     FastAPI Application
         │
         ▼
     Application Service
         │
         ▼
     QR Generator Library
         │
         ▼
     Generated QR Code
```

The library handles QR code generation, while the web application handles HTTP requests, input validation, HTML rendering, and image downloads.

---

## Repository Structure

```text
QR-Code-Generator/
│
├── qr-generator/
│   ├── src/
│   │   └── qr_generator/
│   │       ├── __init__.py
│   │       ├── generator.py
│   │       └── cli.py
│   │
│   ├── tests/
│   ├── assets/
│   ├── pyproject.toml
│   ├── README.md
│   └── LICENSE
│
├── api/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── service/
│   │   ├── exceptions/
│   │   ├── templates/
│   │   └── static/
│   │
│   ├── assets/
│   ├── tests/
│   ├── requirements.txt
│   ├── requirements-dev.txt
│   └── README.md
│
├── LICENSE
└── README.md
```

---

# Part 1: QR Generator Library

## Installation

Install the package from PyPI:

```bash
pip install sah-qr-generator
```

**Requirements:**
- Python 3.8+
- pip

## Usage

### 1. Command-Line Interface

After installation, the `qr` command becomes available.

Generate a QR code from a URL:

```bash
qr --url https://example.com
```

Generate a QR code from plain text:

```bash
qr --txt "Hello, World!"
```

Customize QR code colors:

```bash
qr --url https://example.com --color blue --bg-color white
```

Add an icon to the center:

```bash
qr --url https://example.com --icon assets/logo.png
```

Customize the output filename and directory:

```bash
qr --url https://example.com \
   --output my_qr \
   --path custom_output \
   --format png
```

Display available options:

```bash
qr --help
```

### 2. Python API

You can also integrate the library directly into your Python applications.

Generate a QR code:

```python
from qr_generator import QRGenerator

qr = QRGenerator.generate_qrcode(
    data="https://example.com",
    color="black",
    background_color="white"
)
```

The `generate_qrcode()` method returns a Pillow `Image` object. It does not save the image automatically.

Save the generated QR code:

```python
saved_path = QRGenerator.save_qrcode(
    image=qr,
    output="my_qr",
    output_path="assets/output",
    img_format="png"
)

print(f"QR code saved at: {saved_path}")
```

Generate a QR code with a center icon:

```python
from qr_generator import QRGenerator

qr = QRGenerator.generate_qrcode(
    data="https://example.com",
    color="blue",
    background_color="white",
    icon_path="assets/logo.png"
)

saved_path = QRGenerator.save_qrcode(
    image=qr,
    output="branded_qr",
    output_path="assets/output",
    img_format="png"
)
```

### Supported Customization

| Parameter | Description | Default |
|---|---|---|
| `data` | URL or text to encode | Required |
| `color` | QR code foreground color | black |
| `background_color` | QR code background color | white |
| `box_size` | Size of each QR code module | 10 |
| `border` | QR code border width | 4 |
| `icon_path` | Optional center icon path | None |

### CLI Options

| Option | Description | Default |
|---|---|---|
| `--url` | URL to encode | None |
| `--txt` | Text to encode | None |
| `--color` | Foreground color | black |
| `--bg-color` | Background color | white |
| `--icon` | Optional center icon | None |
| `--output` | Output filename | qrcode |
| `--path` | Output directory | assets/output |
| `--format` | Output format: png, jpg, jpeg | png |

The `--url` and `--txt` options are mutually exclusive. Provide exactly one of them.

### Testing the Library

Navigate to the library directory:

```bash
cd qr-generator
```

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run the tests:

```bash
python -m pytest
```

Run tests with coverage:

```bash
python -m pytest --cov=qr_generator --cov-report=term-missing
```

---

# Part 2: Web Application

## Features

- **QR Code Generation:** Generate QR codes from URLs or plain text.
- **Color Customization:** Customize QR code foreground and background colors.
- **Instant Preview:** Display generated QR codes directly on the page.
- **PNG Download:** Download generated QR codes as PNG images.
- **Input Validation:** Handle empty inputs, unsupported colors, and data that exceeds QR code capacity.
- **No Registration Required:** Generate QR codes without creating an account.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| FastAPI | Web framework |
| Uvicorn | ASGI server |
| Jinja2 | HTML templating |
| sah-qr-generator | Core QR generation library |
| Pillow | Image processing |
| HTML5 | Page structure |
| CSS3 | Styling and responsive layout |
| Pytest | Automated testing |
| HTTPX | HTTP testing client |

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Ahmed122000/QR-Code-Generator.git
```

Navigate to the API directory:

```bash
cd QR-Code-Generator/api
```

### 2. Create a Virtual Environment

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

### 3. Install Dependencies

For running the application:

```bash
pip install -r requirements.txt
```

For development and testing:

```bash
pip install -r requirements-dev.txt
```

### 4. Run the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

Open your browser:

```text
http://127.0.0.1:8000
```

The interactive API documentation is also available at:

```text
http://127.0.0.1:8000/docs
```

---

## Application Routes

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Displays the QR generator page |
| `POST` | `/generate-qr` | Generates a QR code and displays its preview |
| `POST` | `/download-qr` | Generates and downloads a QR code as PNG |

### Generate QR Code

```http
POST /generate-qr
```

Accepts the following form parameters:

| Parameter | Description |
|---|---|
| `data` | Text or URL to encode |
| `fg_color` | QR code foreground color |
| `bg_color` | QR code background color |

Returns the HTML page with the generated QR code preview or an error message.

### Download QR Code

```http
POST /download-qr
```

Accepts the same form parameters and returns the generated QR code as a downloadable PNG image.

---

## Testing the Web Application

Navigate to the API directory:

```bash
cd api
```

Run the automated tests:

```bash
pytest
```

For a more detailed test report:

```bash
pytest -v
```

---

## Deployment

The web application is deployed on [Render](https://render.com/).

**Live URL:** https://sah-qr-generator.onrender.com/

Deployment configuration:

| Setting | Value |
|---|---|
| Runtime | Python 3 |
| Root Directory | `api` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn app.main:app --host 0.0.0.0 --port $PORT` |

Render provides the `PORT` environment variable, which Uvicorn uses to bind the application to the correct port.

---

## Future Improvements

Potential enhancements for the project include:

- Expand the available QR code customization options.
- Improve automated test coverage.
- Add continuous integration with GitHub Actions.
- Introduce additional QR code formats and features.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Ahmed Hesham**

- GitHub: [Ahmed122000](https://github.com/Ahmed122000)
- LinkedIn: [Ahmed Hesham](https://linkedin.com/in/eng-ahmed-hesham24/)

## Acknowledgments

- [python-qrcode](https://github.com/lincolnloop/python-qrcode) for QR code generation.
- [Pillow](https://python-pillow.org/) for image processing.
- [FastAPI](https://fastapi.tiangolo.com/) for the web framework.
