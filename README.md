# QR Code Generator

[![PyPI version](https://img.shields.io/pypi/v/qr-generator-cli.svg)](https://pypi.org/project/qr-generator-cli/)
[![Python version](https://img.shields.io/badge/python-3.8-blue.svg)](https://pypi.org/project/qr-generator-cli/1.0.0/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/Ahmed122000/QR-Code-Generator/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Ahmed122000/QR-Code-Generator.svg)](https://github.com/Ahmed122000/QR-Code-Generator/issues)

A powerful, easy-to-use Python package for generating professional QR codes with customizable styling, watermark/logo support, and multiple output formats.

## Overview

QR Code Generator enables you to quickly create QR codes from URLs or plain text with full control over appearance and branding. Perfect for marketing materials, product packaging, event management, and more.

**Key Highlights:**
- 🎨 Fully customizable colors and styling
- 🏷️ Built-in watermark/logo support with automatic scaling
- 📦 Easy installation from PyPI
- 🖥️ Both CLI and Python API
- 💾 Multiple output formats (PNG, JPG, JPEG)
- 🔧 Simple, intuitive interface

## Features

- ✅ Generate QR codes from URLs or plain text
- ✅ Customize size, foreground/background colors, and error correction level
- ✅ Add watermark/logo with automatic centering and scaling
- ✅ Save to PNG/JPG/JPEG formats
- ✅ Command-line interface (CLI) for quick generation
- ✅ Python API for programmatic use
- ✅ Packaged and published on [PyPI](https://pypi.org/project/qr-generator-cli/)
- ✅ Project metadata and build configuration via `pyproject.toml`
- ✅ Supports error correction levels (L, M, Q, H)
- ✅ Automatic output directory creation

## Requirements

- Python >= 3.8
- Dependencies: `qrcode[pil]`, `Pillow`

## Installation

### From PyPI (Recommended)

```bash
pip install qr-generator-cli
```

### From GitHub

Install the latest development version from the repository:

```bash
pip install git+https://github.com/Ahmed122000/QR-Code-Generator.git
```

### Development Install

Clone the repository and install in editable mode:

```bash
git clone https://github.com/Ahmed122000/QR-Code-Generator.git
cd QR-Code-Generator
pip install -e .
```

## Quick Start

### Using the CLI

The simplest way to generate QR codes:

```bash
# Basic: generate and save to qrcode.png
qr "https://example.com" --output qrcode.png

# With custom styling
qr "https://example.com" --size 800 --fg "#1d3557" --bg "#f1faee" --ec H

# Add a watermark/logo
qr "https://example.com" --output qrcode.png --watermark assets/logo.png --watermark-scale 0.25

# Plain text input
qr "Hello, World!" --output text-qr.png

# High error correction
qr "https://example.com" --size 600 --ec H --output secure-qr.png
```

### Using the Python API

For programmatic QR code generation:

```python
from qr_generator import QRGenerator

# Create a QR code generator instance
gen = QRGenerator()

# Generate and save a QR code
gen.make_qr(
    data="https://example.com",
    output_path="qrcode.png"
)

# With custom styling
gen.make_qr(
    data="https://example.com",
    output_path="styled_qr.png",
    size=800,
    fg_color="#1d3557",
    bg_color="#f1faee",
    error_correction="H"
)

# With watermark/logo
gen.make_qr(
    data="https://example.com",
    output_path="branded_qr.png",
    watermark_path="assets/logo.png",
    watermark_scale=0.25
)
```

## CLI Options

```
Usage: qr [OPTIONS] DATA

Arguments:
  DATA                    The URL or text to encode in the QR code

Options:
  --output, -o            Output file path (default: qrcode.png)
  --size                  QR code size in pixels (default: 400)
  --fg, --foreground      Foreground color as hex code (default: #000000)
  --bg, --background      Background color as hex code (default: #FFFFFF)
  --ec, --error-correction Error correction level: L, M, Q, H (default: M)
  --watermark             Path to watermark/logo image file
  --watermark-scale       Watermark scale relative to QR code (default: 0.2)
  --help                  Show help message
```

## Configuration Reference

### Error Correction Levels

| Level | Recovery | Use Case |
|-------|----------|----------|
| **L** | ~7% | Low-traffic environments |
| **M** | ~15% | Standard use (recommended) |
| **Q** | ~25% | Partially obscured codes |
| **H** | ~30% | Highly damaged/outdoor use |

### Color Formats

Colors should be specified as hexadecimal values:
- `#000000` (black)
- `#FFFFFF` (white)
- `#FF5733` (custom colors)

## Examples

### Example 1: Simple QR Code

```python
from qr_generator import QRGenerator

gen = QRGenerator()
gen.make_qr("https://github.com/Ahmed122000", output_path="github_qr.png")
```

### Example 2: Branded QR Code

```python
from qr_generator import QRGenerator

gen = QRGenerator()
gen.make_qr(
    data="https://yourcompany.com",
    output_path="company_qr.png",
    size=600,
    fg_color="#2C3E50",
    bg_color="#ECF0F1",
    watermark_path="company_logo.png",
    watermark_scale=0.3,
    error_correction="H"
)
```

### Example 3: Batch Generation

```python
from qr_generator import QRGenerator
import csv

gen = QRGenerator()

# Read URLs from CSV and generate QR codes
with open("urls.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        gen.make_qr(
            data=row["url"],
            output_path=f"output/{row['name']}_qr.png",
            size=500,
            fg_color="#1d3557",
            bg_color="#f1faee"
        )
```

## How It Works

### Architecture

1. **CLI Interface** — Command-line argument parsing via `argparse` with flexible input options
2. **QR Generation** — Leverages the `qrcode` library for reliable QR encoding
3. **Image Processing** — Uses Pillow (PIL) for image manipulation
4. **Watermarking** — Custom logo/watermark scaling and centering with transparency preservation
5. **Output** — Supports PNG, JPG, and JPEG formats with high quality

### Process Flow

```
User Input (URL/Text)
    ↓
Validation & Normalization
    ↓
QR Code Generation (qrcode library)
    ↓
Watermark Processing (if provided)
    ↓
Image Conversion (if needed)
    ↓
File Output
```

## Project Structure

```
QR-Code-Generator/
├── src/
│   ├── main.py              # CLI entry point
│   ├── qr_generator.py      # Core QR generation logic
│   └── utils.py             # Utility functions
├── examples/
│   ├── basic.py             # Simple QR generation
│   ├── with_logo.py         # Watermark/logo example
│   └── batch_generate.py    # Batch processing example
├── assets/
│   ├── output/              # Sample output directory
│   └── logo.png             # Sample logo for examples
├── tests/                   # Unit tests
├── pyproject.toml           # Package configuration
├── README.md                # This file
├── LICENSE                  # MIT License
└── .gitignore               # Git ignore rules
```

## Troubleshooting

### Common Issues

**ImportError: No module named 'qrcode'**
```bash
pip install qrcode[pil] Pillow
```

**PermissionError: Permission denied creating output directory**
- Ensure you have write permissions in the target directory
- Try creating the output directory manually: `mkdir -p output`

**Watermark not displaying**
- Verify the watermark file path exists and is readable
- Use PNG format with transparency for best results
- Check watermark-scale is between 0.1 and 0.5

**Invalid color format**
- Ensure colors are specified as hex values: `#RRGGBB`
- Example: `#FF5733` (not `rgb(255, 87, 51)`)

**QR code not scannable**
- Try increasing error correction level: `--ec H`
- Increase QR code size: `--size 600` or higher
- Ensure sufficient contrast between foreground and background colors

## Version History

### v1.0.0
- ✨ Initial release
- 📦 Published to PyPI as `qr-generator-cli`
- 🎨 Full customization support
- 🏷️ Watermark/logo feature
- 🖥️ CLI and Python API

For detailed release notes, see [CHANGELOG.md](./CHANGELOG.md) (if available).

## Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository** on GitHub
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes** and commit: `git commit -m "Add your feature"`
4. **Write/update tests** to cover your changes
5. **Push to your fork**: `git push origin feature/your-feature-name`
6. **Open a Pull Request** with a clear description of your changes

### Development Workflow

```bash
# Install in development mode
pip install -e ".[dev]"

# Run tests
python -m pytest

# Run linting
pylint src/

# Format code
black src/
```

### Reporting Issues

Found a bug? Please [open an issue](https://github.com/Ahmed122000/QR-Code-Generator/issues) with:
- Clear description of the problem
- Steps to reproduce
- Expected vs. actual behavior
- Python version and OS information

## Performance Considerations

- **QR Code Size**: Larger QR codes (800x800px) take slightly longer to generate but are easier to scan
- **Watermark Processing**: Watermarked codes take ~10-20% longer due to image compositing
- **Batch Operations**: For generating 100+ codes, consider using threading or async patterns

## Security Notes

- **Input Validation**: URLs and text are validated before QR encoding
- **File Permissions**: Output files are created with standard user permissions
- **No External Calls**: All processing is local; no data is sent to external services

## Limitations

- Maximum data capacity: ~2953 bytes (depends on error correction level)
- Watermarks should be <= 30% of QR code size for optimal scanability
- Recommended minimum QR code size: 200x200 pixels

## License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

You are free to use, modify, and distribute this software, provided you include the original copyright notice and license.

## Acknowledgments

- Built with [qrcode](https://github.com/lincolnloop/python-qrcode)
- Image processing powered by [Pillow](https://github.com/python-pillow/Pillow)
- Inspired by the need for simple, professional QR code generation

## Support

- 📖 **Documentation**: See examples and features above
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/Ahmed122000/QR-Code-Generator/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Ahmed122000/QR-Code-Generator/discussions)

## Author

**Ahmed122000**  
GitHub: [@Ahmed122000](https://github.com/Ahmed122000)

---

**Made with ❤️ for the open-source community**

If you find this project useful, please consider giving it a ⭐ on [GitHub](https://github.com/Ahmed122000/QR-Code-Generator)!
