# QR Code Generator

A Python-based QR code generator with customizable styling, watermark support, and multiple output formats. Generate professional QR codes from URLs or text with ease.

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Language](https://img.shields.io/badge/Language-Python-blue.svg)

## Features

✨ **Core Capabilities:**
- Generate QR codes from URLs or plain text
- **Customizable QR code colors** (red, blue, green, orange, purple, yellow, black)
- **Optional watermark/icon support** at the center of QR code
- **Multiple output formats** (PNG, JPG, JPEG)
- High error correction rate (Level H)
- **Automatic directory creation** for output paths
- Input validation for URLs
- **Better error handling** with detailed error messages
- **Mutually exclusive arguments** enforcing either URL or text input

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`:
  - `qrcode==7.3.1`
  - `Pillow==8.4.0`

## Installation

### Quick Setup

1. Clone the repository:
```bash
git clone https://github.com/Ahmed122000/QR-Code-Generator.git
cd QR-Code-Generator
```

2. Install dependencies using requirements.txt:
```bash
pip install -r requirements.txt
```

**Alternative:** Install dependencies manually:
```bash
pip install qrcode[pil]==7.3.1 Pillow==8.4.0
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
python main.py --url "https://example.com" --color red
```

Generate with custom output filename and directory:
```bash
python main.py --txt "Your text here" --output "my_qrcode" --path "./qrcodes"
```

Generate with custom format (JPG instead of PNG):
```bash
python main.py --url "https://example.com" --format jpg
```

Generate with watermark/icon:
```bash
python main.py --url "https://example.com" --icon icon.png
```

### Arguments

| Argument | Type | Default | Required | Description |
|----------|------|---------|----------|-------------|
| `--url` | string | - | * | URL to encode in QR code (URL validation performed) |
| `--txt` | string | - | * | Text to encode in QR code |
| `--color` | string | `black` | No | QR code color: `red`, `blue`, `green`, `orange`, `purple`, `yellow`, `black` |
| `--output` | string | `qrcode` | No | Output filename (without extension) |
| `--icon` | string | - | No | Path to icon/watermark image file |
| `--path` | string | `./assets/output` | No | Output directory path |
| `--format` | string | `png` | No | Output image format: `png`, `jpg`, `jpeg` |

**\* Either `--url` or `--txt` is required, but not both.**

## Examples

### Generate QR code from GitHub URL
```bash
python main.py --url "https://github.com/Ahmed122000/QR-Code-Generator"
```

**Output:** `qrcode.png` (in current directory)

### Generate red QR code from text with custom output
```bash
python main.py --txt "Contact: Ahmed@example.com" --color red --output "contact_qr"
```

**Output:** `contact_qr.png`

### Generate QR code with watermark/logo
```bash
python main.py --url "https://example.com" --icon logo.png --output "branded_qr"
```

**Output:** `branded_qr.png` (with centered logo)

### Generate JPG format in custom directory
```bash
python main.py --txt "My Data" --format jpg --path "./output/qrcodes" --output "my_code"
```

**Output:** `./output/qrcodes/my_code.jpg` (creates directory if it doesn't exist)

### Generate blue QR code with all custom options
```bash
python main.py --url "https://example.com" --color blue --icon watermark.png --path "./qr_codes" --output "website_qr" --format png
```

**Output:** `./qr_codes/website_qr.png`

## Project Structure

```
QR-Code-Generator/
├── assets
    ├── output
    └── logo 
├── main.py              # CLI entry point with argument parsing and validation
├── qr_generator.py      # Core QR code generation logic
├── requirements.txt     # Python package dependencies
├── icon.png             # Default watermark image (optional)
├── LICENSE              # MIT License
└── README.md            # This file
```

## How It Works

### `main.py`
- **Argument Parsing:** Uses `argparse` with mutually exclusive group for `--url` and `--txt`
- **URL Validation:** Validates URL format using `urllib.parse.urlparse`
- **Input Validation:** Ensures input data is not empty and properly formatted
- **Directory Creation:** Automatically creates output directory if it doesn't exist
- **Error Handling:** Provides detailed error messages and graceful exit codes
- **Calls `QRGenerator`:** Passes arguments to the core QR generation logic

### `qr_generator.py`
- **QRGenerator Class:** Static method `generate_qrcode()` handles all QR generation
- **QR Code Creation:** Uses `qrcode` library with auto-fitting version
- **Image Processing:** Uses PIL (Pillow) for image manipulation
- **Icon/Watermark Support:** 
  - Optionally loads and converts icon to RGBA
  - Scales watermark to 1/4 of QR code size
  - Centers watermark on QR code
  - Composites with transparency support
- **Multiple Formats:** Saves in PNG, JPG, or JPEG format
- **Error Handling:** Catches and reports specific errors (DataOverflowError, PermissionError, etc.)
- **Type Hints:** Uses Python type hints for better code clarity

### `requirements.txt`
Contains all dependencies needed to run the project:
- `qrcode==7.3.1` - QR code generation library
- `Pillow==8.4.0` - Image processing library
- Pin versions ensure compatibility and reproducible builds

## Configuration

### QR Code Parameters (Advanced)

You can modify advanced parameters by editing `qr_generator.py`:

```python
QRGenerator.generate_qrcode(
    data,                           # QR code data (required)
    output="qrcode",                # Output filename
    output_path="./assets/output",  # Output directory
    box_size=10,                    # Pixel size per box (default: 10)
    border=2,                       # Border width in boxes (default: 2)
    color="black",                  # QR code color
    icon_path=None,                 # Icon file path (optional)
    format='png'                    # Output format
)
```

### Color Options
- `red` - Red colored QR code
- `blue` - Blue colored QR code
- `green` - Green colored QR code
- `orange` - Orange colored QR code
- `purple` - Purple colored QR code
- `yellow` - Yellow colored QR code
- `black` - Black colored QR code (default)

### Output Formats
- `png` - PNG format (lossless, recommended)
- `jpg` - JPEG format (lossy compression)
- `jpeg` - JPEG format (alias for jpg)

## Error Handling

The application provides helpful error messages for common issues:

| Error | Cause | Solution |
|-------|-------|----------|
| `Input data cannot be empty!` | Empty input provided | Provide non-empty `--url` or `--txt` |
| `Invalid URL format!` | Malformed URL | Use proper URL: `https://example.com` |
| `Cannot create directory` | Permission denied | Check directory permissions |
| `Icon file not found` | Icon path doesn't exist | Verify icon path is correct |
| `Data too large for this QR version` | Text/URL too long | Reduce input size |

## Troubleshooting

### ModuleNotFoundError: No module named 'qrcode'
Make sure to install dependencies:
```bash
pip install -r requirements.txt
```

### Permission Denied when creating output directory
Check write permissions on the target directory path.

### Icon not displayed in QR code
Ensure the icon file path is correct and the file exists. The icon should support transparency (PNG recommended).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Technologies Used

- **qrcode** - QR code generation (v7.3.1)
- **Pillow (PIL)** - Image processing and watermarking (v8.4.0)
- **argparse** - Command-line interface
- **typing** - Type hints for better code quality

## Topics

`argparse` | `python` | `qrcode` | `qrcode-generator` | `cli` | `image-processing`

---

**Author:** [Ahmed122000](https://github.com/Ahmed122000)
