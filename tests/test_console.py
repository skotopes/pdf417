import pytest

from mock import patch

from pdf417 import console


@pytest.fixture
def arguments():
    return console.parser.parse_args(['encode'])


@patch('pdf417.console.encode', return_value="RETVAL")
@patch('pdf417.console.render_image')
def test_encode(render_image, encode, capsys, arguments):
    arguments.text = "foo"

    console.encode_data(arguments)

    encode.assert_called_once_with(
        arguments.text,
        columns=6,
        encoding='utf-8',
        security_level=2,
        numeric_compaction=False,
        truncate=False,
    )

    render_image.assert_called_once_with(
        'RETVAL',
        bg_color='#FFFFFF',
        fg_color='#000000',
        padding=20,
        ratio=3,
        scale=3
    )
