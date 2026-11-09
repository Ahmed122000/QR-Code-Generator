
import pytest
from unittest.mock import Mock

from PIL import UnidentifiedImageError
from qrcode.exceptions import DataOverflowError

from src import main


def setup_mocks(monkeypatch, generate_mock, save_mock):
    """Replace the real QRGenerator methods with mocks."""
    monkeypatch.setattr(
        main.QRGenerator,
        "generate_qrcode",
        generate_mock,
    )
    monkeypatch.setattr(
        main.QRGenerator,
        "save_qrcode",
        save_mock,
    )


# ---------------------------
# Successful execution
# ---------------------------

def test_main_success(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--txt", "Hello, pytest!"],
    )

    fake_image = object()
    saved_path = tmp_path / "qrcode.png"

    generate_mock = Mock(return_value=fake_image)
    save_mock = Mock(return_value=saved_path)

    setup_mocks(monkeypatch, generate_mock, save_mock)

    result = main.main()

    assert result == 0

    generate_mock.assert_called_once_with(
        "Hello, pytest!",
        color="black",
        background_color="white",
        icon_path=None,
    )

    save_mock.assert_called_once_with(
        fake_image,
        output="qrcode",
        output_path="assets/output",
        img_format="png",
    )


def test_main_with_custom_arguments(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "sys.argv",
        [
            "main.py",
            "--url", "https://example.com",
            "--color", "blue",
            "--bg-color", "yellow",
            "--output", "custom_qr",
            "--path", str(tmp_path),
            "--format", "jpg",
        ],
    )

    fake_image = object()
    saved_path = tmp_path / "custom_qr.jpg"

    generate_mock = Mock(return_value=fake_image)
    save_mock = Mock(return_value=saved_path)

    setup_mocks(monkeypatch, generate_mock, save_mock)

    result = main.main()

    assert result == 0

    generate_mock.assert_called_once_with(
        "https://example.com",
        color="blue",
        background_color="yellow",
        icon_path=None,
    )

    save_mock.assert_called_once_with(
        fake_image,
        output="custom_qr",
        output_path=str(tmp_path),
        img_format="jpg",
    )


# ---------------------------
# Input validation
# ---------------------------

def test_main_with_empty_text(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--txt", ""],
    )

    generate_mock = Mock()
    save_mock = Mock()

    setup_mocks(monkeypatch, generate_mock, save_mock)

    result = main.main()

    assert result == 1
    generate_mock.assert_not_called()
    save_mock.assert_not_called()


def test_main_with_invalid_url(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--url", "invalid-url"],
    )

    generate_mock = Mock()
    save_mock = Mock()

    setup_mocks(monkeypatch, generate_mock, save_mock)

    result = main.main()

    assert result == 1
    generate_mock.assert_not_called()
    save_mock.assert_not_called()


# ---------------------------
# Generation errors
# ---------------------------

def test_main_handles_value_error(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--txt", "Hello"],
    )

    generate_mock = Mock(side_effect=ValueError("Invalid configuration"))
    save_mock = Mock()

    setup_mocks(monkeypatch, generate_mock, save_mock)

    result = main.main()

    assert result == 1
    save_mock.assert_not_called()


def test_main_handles_missing_icon(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--txt", "Hello", "--icon", "missing.png"],
    )

    generate_mock = Mock(side_effect=FileNotFoundError("Icon not found"))
    save_mock = Mock()

    setup_mocks(monkeypatch, generate_mock, save_mock)

    result = main.main()

    assert result == 1
    save_mock.assert_not_called()


def test_main_handles_invalid_icon(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--txt", "Hello", "--icon", "invalid.png"],
    )

    generate_mock = Mock(
        side_effect=UnidentifiedImageError("Invalid image")
    )
    save_mock = Mock()

    setup_mocks(monkeypatch, generate_mock, save_mock)

    result = main.main()

    assert result == 1
    save_mock.assert_not_called()


def test_main_handles_data_overflow(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--txt", "Very large input"],
    )

    generate_mock = Mock(
        side_effect=DataOverflowError("Data is too large")
    )
    save_mock = Mock()

    setup_mocks(monkeypatch, generate_mock, save_mock)

    result = main.main()

    assert result == 1
    save_mock.assert_not_called()


# ---------------------------
# Saving errors
# ---------------------------

@pytest.mark.parametrize(
    "error",
    [
        PermissionError("Permission denied"),
        ValueError("Invalid output configuration"),
        OSError("Unable to save file"),
    ],
)
def test_main_handles_save_errors(monkeypatch, error):
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--txt", "Hello"],
    )

    fake_image = object()

    generate_mock = Mock(return_value=fake_image)
    save_mock = Mock(side_effect=error)

    setup_mocks(monkeypatch, generate_mock, save_mock)

    result = main.main()

    assert result == 1
    generate_mock.assert_called_once()
    save_mock.assert_called_once()

def test_main_with_unsupported_format(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--txt", "Hello", "--format", "gif"],
    )

    generate_mock = Mock()
    save_mock = Mock()

    setup_mocks(monkeypatch, generate_mock, save_mock)

    with pytest.raises(SystemExit) as exc_info:
        main.main()

    assert exc_info.value.code == 2
    generate_mock.assert_not_called()
    save_mock.assert_not_called()