# QR Code Generator

A Python-based QR code generator with customizable styling and watermark support. Generate professional QR codes from URLs or text with ease.

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Language](https://img.shields.io/badge/Language-Python-blue.svg)

## Features

✨ **Core Capabilities:**
- Generate QR codes from URLs or plain text
- Customizable QR code colors
- Built-in watermark support (centered on QR code)
- High error correction rate (Level H)
- Automatic output saving in PNG format
- Input validation for URLs

## Requirements

- Python 3.x
- `qrcode` library
- `pillow` (PIL) library

## Installation

### Install Dependencies

```bash
pip install qrcode[pil] pillow
```

## Usage

### Basic Commands

Generate a QR code from a URL:
```bash
python main.py --url "https://example.com"
```

Generate a QR code from text:
```bash
python main.py --txt "Hello, World!"
```

Generate a QR code with custom color:
```bash
python main.py --url "https://example.com" --color "red"
```

Generate with custom output filename:
```bash
python main.py --txt "Your text here" --output "my_qrcode"
```

### Arguments

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `--url` | string | Optional | - | URL to encode in QR code (URL validation performed) |
| `--txt` | string | Optional | - | Text to encode in QR code |
| `--color` | string | Optional | `black` | QR code color (e.g., `red`, `blue`, `#FF5733`) |
| `--output` | string | Optional | `qrcode` | Output filename (without .png extension) |

**Note:** You must provide either `--url` or `--txt`, but not both.

## Examples

### Generate QR code from GitHub URL
```bash
python main.py --url "https://github.com/Ahmed122000/QR-Code-Generator"
```

**Output:** `qrcode.png`

### Generate red QR code from text
```bash
python main.py --txt "Contact: Ahmed@example.com" --color "red" --output "contact_qr"
```

**Output:** `contact_qr.png`

### Generate with custom color code
```bash
python main.py --url "https://example.com" --color "#009688"
```

## Project Structure

```
QR-Code-Generator/
├── main.py              # CLI entry point with argument parsing
├── qr_generator.py      # Core QR code generation logic
├── icon.png             # Watermark image
├── LICENSE              # MIT License
└── README.md            # This file
```

## How It Works

### `main.py`
- Handles command-line argument parsing using `argparse`
- Validates URL format using `urllib.parse.urlparse`
- Ensures either `--url` or `--txt` is provided (not both)
- Calls `QRGenerator` to generate the QR code

### `qr_generator.py`
- Contains the `QRGenerator` class
- Generates QR codes using the `qrcode` library
- Uses PIL (Pillow) to:
  - Convert QR code to RGBA format
  - Apply watermark/icon at the center
  - Scale watermark to 1/4 of QR code size
  - Composite watermark onto QR code with transparency
  - Save final image as PNG

## Configuration

You can customize the QR code generation by modifying parameters in `qr_generator.py`:

```python
generate_qrcode(
    data,                           # QR code data
    file_path="./",                 # Save location
    output="qrcode",                # Filename
    version=1,                      # QR code version (1-40)
    box_size=10,                    # Pixel size per box
    border=2,                       # Border size in boxes
    color="black"                   # QR code color
)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Technologies Used

- **qrcode** - QR code generation
- **Pillow (PIL)** - Image processing and watermarking
- **argparse** - Command-line interface

## Topics

`argparse` | `python` | `qrcode` | `qrcode-generator`

---

**Author:** [Ahmed122000](https://github.com/Ahmed122000)
