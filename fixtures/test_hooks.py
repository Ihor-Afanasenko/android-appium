def pytest_addoption(parser):
    parser.addoption(
        "--app_type",
        help="Type of the Joom. Can be web or native",
        action="store",
    )
