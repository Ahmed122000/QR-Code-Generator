# QR Code Generator

[![PyPI version](https://badge.fury.io/py/qr-generator-cli.svg)](https://pypi.org/project/qr-generator-cli/)
[![Python](https://img.shields.io/pypi/pyversions/qr-generator-cli)](https://pypi.org/project/qr-generator-cli/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A Python-based QR code generator that allows you to create QR codes from URLs or plain text. Customize colors, add an optional center icon, and save your generated QR codes in different image formats.

Use it through a simple command-line interface (CLI) or integrate it directly into your Python projects.

## Features

- **URL and Text Support:** Generate QR codes from URLs or plain text.
- **Custom Colors:** Choose from supported foreground and background colors.
- **Center Icon:** Add an optional image to the center of your QR code.
- **Multiple Formats:** Save generated QR codes as PNG, JPG, or JPEG.
- **Custom Output:** Choose your output filename and directory.
- **Python API:** Use the QR generation functionality directly in your Python applications.
- **Automated Tests:** Includes unit tests using pytest.

## Requirements

- Python 3.8 or higher
- pip

## Installation

### Install from PyPI

```bash
pip install qr-generator-cli
```

### Install from GitHub

```bash
git clone https://github.com/Ahmed122000/QR-Code-Generator.git

cd QR-Code-Generator

pip install -e .
```

### Install development dependencies

If you want to contribute or run the tests, install the development dependencies:

```bash
pip install -e ".[dev]"
```

## Usage

### 1. Command-Line Interface (CLI)

After installation, you can use the `qr` command directly from your terminal.

**Generate a QR code from a URL:**

```bash
qr --url https://example.com
```

**Generate a QR code from plain text:**

```bash
qr --txt "Hello, World!"
```

**Customize QR code colors:**

```bash
qr --url https://example.com --color blue --bg-color white
```

**Add an icon to the center:**

```bash
qr --url https://example.com --icon assets/logo.png
```

**Customize the output filename and directory:**

```bash
qr --url https://example.com \
   --output my_qr \
   --path custom_output \
   --format png
```

**Display available commands and options:**

```bash
qr --help
```

Generated QR codes are saved in `assets/output/` by default.

### 2. Python API

You can also use the QR generator directly in your Python applications.

**Generate a QR code:**

```python
from src.qr_generator import QRGenerator

qr = QRGenerator.generate_qrcode(
    data="https://example.com",
    color="black",
    background_color="white"
)
```

The `generate_qrcode()` method returns a Pillow `Image` object. It does not save the image automatically.

**Save the generated QR code:**

```python
saved_path = QRGenerator.save_qrcode(
    image=qr,
    output="my_qr",
    output_path="assets/output",
    img_format="png"
)

print(f"QR code saved at: {saved_path}")
```

**Generate and save a QR code with a center icon:**

```python
from src.qr_generator import QRGenerator

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

## CLI Reference

| Option | Description | Default |
|---|---|---|
| `--url` | URL to encode in the QR code | None |
| `--txt` | Text to encode in the QR code | None |
| `--color` | QR code foreground color | black |
| `--bg-color` | QR code background color | white |
| `--icon` | Path to the optional center icon | None |
| `--output` | Output filename without extension | qrcode |
| `--path` | Output directory | assets/output |
| `--format` | Output image format: png, jpg, jpeg | png |
| `-h`, `--help` | Display help information | — |

**Supported colors:**

`black`, `white`, `red`, `blue`, `green`, `orange`, `purple`, `yellow`.

The `--url` and `--txt` options are mutually exclusive. You must provide exactly one of them.

## Python API Reference

### `generate_qrcode()`

Generates a QR code and returns a Pillow Image object.

| Parameter | Description | Default |
|---|---|---|
| `data` | URL or text to encode | Required |
| `color` | QR code foreground color | black |
| `background_color` | QR code background color | white |
| `box_size` | Size of each QR code box | 10 |
| `border` | QR code border width | 4 |
| `icon_path` | Optional path to a center icon | None |

### `save_qrcode()`

Saves a generated Pillow Image to the specified location.

| Parameter | Description | Default |
|---|---|---|
| `image` | Pillow Image object | Required |
| `output` | Output filename without extension | qrcode |
| `output_path` | Destination directory | assets/output |
| `img_format` | Image format: png, jpg, jpeg | png |

The method returns the path of the saved image.

## Project Structure

```text
QR-Code-Generator/
│
├── src/
│   ├── __init__.py
│   ├── main.py              # CLI interface
│   └── qr_generator.py      # Core QR generation logic
│
├── tests/
│   ├── test_main.py         # CLI tests
│   ├── test_qr_generator.py # QR generation tests
│   └── test_save_qr.py      # Image saving tests
│
├── assets/
│   └── output/              # Generated QR codes
│
├── pyproject.toml           # Package configuration
├── README.md
├── LICENSE
└── .gitignore
```

## Testing

The project uses **pytest** for automated testing and **pytest-cov** for measuring test coverage.

Install the development dependencies:

```bash
pip install -e ".[dev]"
```

Run all tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=src --cov-report=term-missing
```

The project currently has 25 passing test cases and approximately 99% overall code coverage.

## Error Handling

The project handles common errors, including:

- Empty or invalid input.
- Invalid QR code configuration.
- Missing or invalid icon files.
- Unsupported image formats.
- File permission errors.
- QR code data overflow.

The core generation logic raises meaningful exceptions, while the CLI handles them and displays appropriate error messages.

## Technologies Used

- **Python:** Main programming language.
- **qrcode:** QR code generation.
- **Pillow:** Image processing and manipulation.
- **argparse:** Command-line argument parsing.
- **pytest:** Automated testing.
- **pytest-cov:** Test coverage reporting.
- **setuptools:** Python package building and distribution.

## Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes.
4. Run the tests:

   ```bash
   pytest
   ```

5. Commit your changes:

   ```bash
   git commit -m "Add your feature"
   ```

6. Push your branch and open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Ahmed Hesham**

- GitHub: [Ahmed122000](https://github.com/Ahmed122000)
- LinkedIn: [Ahmed Hesham](https://linkedin.com/in/eng-ahmed-hesham24/)

## Acknowledgments

- [qrcode](https://github.com/lincolnloop/python-qrcode) for QR code generation.
- [Pillow](https://python-pillow.org/) for image processing.
