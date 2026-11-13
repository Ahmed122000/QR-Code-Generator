# QR Code Generator

[![PyPI version](https://badge.fury.io/py/sah-qr-generator.svg)](https://pypi.org/project/sah-qr-generator/)
[![Python versions](https://img.shields.io/pypi/pyversions/sah-qr-generator)](https://pypi.org/project/sah-qr-generator/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A customizable Python QR code generator that creates QR codes from URLs or plain text.

Customize foreground and background colors, add an optional center icon, and save generated QR codes in PNG, JPG, or JPEG formats.

Use it through a command-line interface (CLI) or integrate it directly into your Python applications.

## Features

- **URL and Text Support:** Generate QR codes from URLs or plain text.
- **Custom Colors:** Customize QR code foreground and background colors.
- **Center Icon:** Add an optional image to the center of your QR code.
- **Multiple Formats:** Save QR codes as PNG, JPG, or JPEG.
- **Custom Output:** Specify the output filename and destination directory.
- **Python API:** Integrate QR generation into your own applications.
- **Automated Tests:** Includes unit tests using pytest.

## Requirements

- Python 3.8 or higher
- pip

## Installation

### Install from PyPI

```bash
pip install sah-qr-generator
```

### Install from GitHub

Clone the repository:

```bash
git clone https://github.com/Ahmed122000/QR-Code-Generator.git
```

Navigate to the library directory:

```bash
cd QR-Code-Generator/qr-generator
```

Install the package:

```bash
pip install .
```

### Install development dependencies

If you want to contribute or run the tests, install the package in editable mode with its development dependencies:

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
from qr_generator import QRGenerator

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

The `--url` and `--txt` options are mutually exclusive. Provide exactly one of them.

## Python API Reference

### `generate_qrcode()`

Generates a QR code and returns a Pillow Image object.

| Parameter | Description | Default |
|---|---|---|
| `data` | URL or text to encode | Required |
| `color` | QR code foreground color | black |
| `background_color` | QR code background color | white |
| `box_size` | Size of each QR code module in pixels | 10 |
| `border` | QR code border width in modules | 4 |
| `icon_path` | Optional path to a center icon | None |

### `save_qrcode()`

Saves a generated Pillow Image to the specified location.

| Parameter | Description | Default |
|---|---|---|
| `image` | Pillow Image object | Required |
| `output` | Output filename without extension | qrcode |
| `output_path` | Destination directory | assets/output |
| `img_format` | Image format: png, jpg, jpeg | png |

The method returns a `Path` object representing the saved image.

## Project Structure

```text
QR-Code-Generator/
│
├── qr-generator/
│   │
│   ├── src/
│   │   └── qr_generator/
│   │       ├── __init__.py
│   │       ├── generator.py
│   │       └── cli.py
│   │
│   ├── tests/
│   │   ├── test_cli.py
│   │   ├── test_generator.py
│   │   └── test_save_qr.py
│   │
│   ├── assets/
│   │   └── output/
│   │
│   ├── pyproject.toml
│   ├── README.md
│   ├── LICENSE
│   └── .gitignore
│
└── README.md
```

## Testing

The project uses:

- **pytest:** Automated testing.
- **pytest-cov:** Test coverage measurement.

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run all tests:

```bash
python -m pytest
```

Run tests with coverage:

```bash
python -m pytest --cov=qr_generator --cov-report=term-missing
```

## Error Handling

The library handles common errors, including:

- Empty or invalid input.
- Invalid QR code configuration.
- Missing or invalid icon files.
- Unsupported image formats.
- File permission errors.
- QR code data overflow.

The core library raises meaningful exceptions, allowing applications to handle errors according to their own requirements. The CLI catches relevant exceptions and displays appropriate error messages.

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
   python -m pytest
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

- [python-qrcode](https://github.com/lincolnloop/python-qrcode) for QR code generation.
- [Pillow](https://python-pillow.org/) for image processing.