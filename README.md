# QR Code Generator

A Python QR code generator with customizable colors, optional center icons, and support for PNG, JPG, and JPEG output formats.

[![PyPI version](https://img.shields.io/pypi/v/qr-generator-cli.svg)](https://pypi.org/project/qr-generator-cli/)
[![Python version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Overview

QR Code Generator is a Python project that allows you to generate QR codes from URLs or plain text.

It provides two ways to use the project:

- **Command-Line Interface (CLI):** Generate QR codes directly from your terminal.
- **Python API:** Use the QR generator in your own Python applications.

The project separates QR code generation from file saving, making the core functionality reusable across different interfaces.

## Features

- Generate QR codes from URLs or plain text.
- Customize foreground and background colors.
- Add an optional center icon to your QR code.
- Automatically resize and center the icon.
- Save generated QR codes as PNG, JPG, or JPEG.
- Automatically create output directories when needed.
- Use the generator through the CLI or Python code.
- Validate input and handle common generation and file errors.

## Requirements

- Python 3.8 or newer.
- [qrcode](https://pypi.org/project/qrcode/)
- [Pillow](https://pypi.org/project/Pillow/)

## Installation

### From PyPI

Install the package using pip:

```bash
pip install qr-generator-cli
```

### From GitHub

Install the latest version from the repository:

```bash
git clone https://github.com/Ahmed122000/QR-Code-Generator.git

cd QR-Code-Generator

pip install -e .
```

### Development Installation

If you want to contribute or run the tests, clone the repository and install the development dependencies:

```bash
git clone https://github.com/Ahmed122000/QR-Code-Generator.git

cd QR-Code-Generator

pip install -e ".[dev]"
```

## Quick Start

### Using the CLI

You can generate QR codes directly from your terminal.

Run the CLI from the project root:

```bash
python -m src.main --url https://example.com
```

Generate a QR code from plain text:

```bash
python -m src.main --txt "Hello, World!"
```

Customize the QR code colors:

```bash
python -m src.main --url https://example.com --color blue --bg-color white
```

Add an icon to the center:

```bash
python -m src.main --url https://example.com --icon assets/logo.png
```

Choose the output filename, directory, and format:

```bash
python -m src.main \
    --url https://example.com \
    --output my_qrcode \
    --path assets/output \
    --format png
```

### Using the Python API

The project also provides a Python API for generating and saving QR codes programmatically.

#### 1. Generate a QR code

Use `generate_qrcode()` to create a QR code.

```python
from src.qr_generator import QRGenerator

image = QRGenerator.generate_qrcode(
    data="https://example.com",
    color="blue",
    background_color="white"
)
```

The method returns a Pillow `Image` object. It does not save the image automatically.

#### 2. Save the generated QR code

Use `save_qrcode()` to save the generated image:

```python
saved_path = QRGenerator.save_qrcode(
    image,
    output="my_qrcode",
    output_path="assets/output",
    img_format="png"
)

print(f"Saved to: {saved_path}")
```

#### 3. Generate and save with a center icon

You can also provide an icon when generating the QR code:

```python
from src.qr_generator import QRGenerator

image = QRGenerator.generate_qrcode(
    data="https://github.com/Ahmed122000",
    color="black",
    background_color="white",
    icon_path="assets/logo.png"
)

QRGenerator.save_qrcode(
    image,
    output="github_qrcode",
    output_path="assets/output",
    img_format="png"
)
```

## CLI Reference

The CLI uses `argparse` to handle command-line arguments.

| Argument | Description | Default |
|---|---|---|
| `--url` | URL to encode in the QR code | None |
| `--txt` | Text to encode in the QR code | None |
| `--color` | QR code foreground color | `black` |
| `--bg-color` | QR code background color | `white` |
| `--icon` | Path to an optional center icon | None |
| `--output` | Output filename without extension | `qrcode` |
| `--path` | Output directory | `assets/output` |
| `--format` | Output image format: `png`, `jpg`, or `jpeg` | `png` |

**Important:**

- Provide either `--url` or `--txt`, not both.
- URLs must use HTTP or HTTPS.
- The available CLI colors are `black`, `white`, `red`, `blue`, `green`, `orange`, `purple`, and `yellow`.
- The output filename is provided without its extension. The extension is determined by `--format`.

To see all available arguments:

```bash
python -m src.main --help
```

## Python API Reference

### `generate_qrcode()`

Generates a QR code and returns a Pillow Image object.

```python
QRGenerator.generate_qrcode(
    data,
    color="black",
    background_color="white",
    box_size=10,
    border=4,
    icon_path=None
)
```

| Parameter | Description |
|---|---|
| `data` | Text or URL to encode |
| `color` | QR code foreground color |
| `background_color` | QR code background color |
| `box_size` | Size of each QR code box |
| `border` | Width of the QR code border |
| `icon_path` | Optional path to a center icon |

### `save_qrcode()`

Saves a generated Pillow Image object and returns the saved file path.

```python
QRGenerator.save_qrcode(
    image,
    output="qrcode",
    output_path="assets/output",
    img_format="png"
)
```

| Parameter | Description |
|---|---|
| `image` | Pillow Image object to save |
| `output` | Output filename without extension |
| `output_path` | Directory where the image will be saved |
| `img_format` | Image format: `png`, `jpg`, or `jpeg` |

## Project Structure

```text
QR-Code-Generator/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── qr_generator.py
│
├── tests/
│   ├── test_main.py
│   ├── test_qr_generator.py
│   └── test_save_qr.py
│
├── assets/
│   └── output/
│
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

## Running Tests

The project uses `pytest` for automated testing.

Install the development dependencies:

```bash
pip install -e ".[dev]"
```

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=src --cov-report=term-missing
```

The tests cover QR code generation, image saving, input validation, icon handling, and CLI error handling.

## Error Handling

The project handles common errors, including:

- Empty or invalid input.
- Invalid QR code configuration.
- Missing icon files.
- Unsupported or invalid image files.
- Input data that exceeds QR code capacity.
- Unsupported output formats.
- File permission and saving errors.

The core generator raises exceptions when an operation fails. The CLI catches these exceptions and displays useful error messages.

## Troubleshooting

### Missing dependencies

If you encounter an import error for `qrcode` or `Pillow`, install the dependencies:

```bash
pip install "qrcode[pil]" Pillow
```

### Icon not displaying

- Check that the icon file exists.
- Make sure the file is a supported image.
- Use a valid image path.

### Permission error when saving

Make sure you have permission to write to the selected output directory.

### QR code cannot be scanned

- Ensure sufficient contrast between foreground and background colors.
- Avoid placing an icon that covers too much of the QR code.
- Test the generated QR code with a scanner.

## Contributing

Contributions are welcome!

To contribute:

1. Fork the repository.
2. Create a new feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes.
4. Add or update tests.
5. Run the test suite:

   ```bash
   pytest
   ```

6. Commit and push your changes.
7. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [python-qrcode](https://github.com/lincolnloop/python-qrcode) for QR code generation.
- [Pillow](https://github.com/python-pillow/Pillow) for image processing.

## Author

**Ahmed Hesham**

- GitHub: [@Ahmed122000](https://github.com/Ahmed122000)
- Portfolio: [ahmed122000.github.io/Portfolio](https://ahmed122000.github.io/Portfolio/)

---

If you find this project useful, consider giving it a ⭐ on [GitHub](https://github.com/Ahmed122000/QR-Code-Generator).
