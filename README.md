# QR Code Generator

A Python-based QR code generator with customizable styling and watermark/logo support. Generate professional QR codes from URLs or text with ease.

[![PyPI version](https://img.shields.io/pypi/v/qr-generator-cli.svg)](https://pypi.org/project/qr-generator-cli/)
[![Python versions](https://img.shields.io/pypi/pyversions/qr-generator-cli.svg)](https://pypi.org/project/qr-generator-cli/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

## Features

- Generate QR codes from URLs or plain text
- Customizable size, foreground/background colors, and error correction level
- Add watermark/logo with automatic centering and scaling
- Save to PNG/JPG/JPEG
- Command-line interface (CLI) and Python API
- Packaged and published on PyPI (see installation below)
- Project metadata and build configuration provided via `pyproject.toml`

## Installation

Install from PyPI:

```bash
pip install qr-generator-cli
```

Or install the latest from the repository:

```bash
pip install git+https://github.com/Ahmed122000/QR-Code-Generator.git
```

Development install (uses `pyproject.toml` / PEP 517):

```bash
# Build and install in editable/development mode (if you use Poetry, see Poetry docs)
pip install -e .
```

Requirements: Python >= 3.8. Dependencies are declared in `pyproject.toml` and include `qrcode[pil]` and `Pillow`.

## Quick Usage

CLI (recommended):

```bash
# Basic: generate and save qrcode.png
qr "https://example.com" --output qrcode.png

# With styling
qr "https://example.com" --size 800 --fg "#1d3557" --bg "#f1faee" --ec H

# Add watermark/logo
qr "https://example.com" --output qrcode.png --watermark assets/logo.png --watermark-scale 0.25
```

(The CLI entry point is `qr` as declared in `pyproject.toml`.)

Python API (example — adjust import path to your package layout if needed):

```python
from src.main import main as qr_main  # or import the QRGenerator class from your package

# Example: if you expose a programmatic API, call it like:
# from qr_generator import QRGenerator
# gen = QRGenerator(...)
# gen.make_qr("https://example.com", output_path="qrcode.png")
```

## Configuration (pyproject.toml)

This repository includes `pyproject.toml` for packaging metadata and build configuration (setuptools backend). Use standard tools to build and publish:

```bash
# Build
python -m build

# Upload (after building)
twine upload dist/*
```

If you use Poetry, `pyproject.toml` can also contain Poetry configuration.

## Examples

- `examples/basic.py` — simple generation and save
- `examples/with_logo.py` — generate QR with a centered watermark/logo
- `examples/batch_generate.py` — generate multiple QR codes from a CSV

(Adjust example paths to match repository layout.)

## Changelog (high level)

- v1.0.0 — Packaged and published to PyPI as `qr-generator-cli`; added `pyproject.toml` and CLI entry point `qr`.

If you maintain a `CHANGELOG.md`, add detailed release notes there.

## Project Structure (example)

```
QR-Code-Generator/
├── assets/
│   ├── output/
│   └── logo.png
├── src/
│   └── main.py        # CLI entry point (pyproject defines `qr = src.main:main`)
├── pyproject.toml
├── README.md
├── LICENSE
└── examples/
```

## How It Works

- CLI argument parsing uses `argparse` with mutually exclusive input options (URL or text).
- QR generation uses the `qrcode` library with Pillow (PIL) for image processing.
- Watermark/logo support scales and centers an icon on the QR image and preserves transparency.
- Output formats supported: `png`, `jpg`, `jpeg`.

## Common Commands

- Build package: `python -m build`
- Publish to PyPI: `twine upload dist/*`
- Run CLI locally: `qr "https://example.com" --output q.png`

## Troubleshooting

- ModuleNotFoundError: No module named 'qrcode' — install dependencies: `pip install qrcode[pil] Pillow`
- Permission denied creating output directory — check write permissions
- Icon not displayed — ensure the icon path exists and supports transparency (PNG recommended)

## Contributing

Contributions welcome! Suggested workflow:

1. Fork the repo and create a feature branch.
2. Run tests and linting (if present).
3. Open a pull request describing your changes.

When releasing a new version to PyPI, update `pyproject.toml` version and follow standard build/release steps.

## License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

## Author

**Ahmed122000** — https://github.com/Ahmed122000
