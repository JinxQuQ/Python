# yield也可以配合with语句使用，以下是官方文档给的案例

import smtplib
import pytest


@pytest.fixture(scope="module")
def smtp():
    with smtplib.SMTP("smtp.gmail.com") as smtp:
        yield smtp
        # provide the fixture value
