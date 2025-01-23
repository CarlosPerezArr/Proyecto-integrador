__config_version__ = 1

GLOBALS = {
    "serializer": "{{year}}.{{month}}.{{day}}.{{build}}",
}

FILES = [
    "glu-next/package.json",
    "glu-fastapi/pyproject.toml",
]

VERSION = [
    {"name": "year", "type": "date", "fmt": "%Y"},
    {"name": "month", "type": "date", "fmt": "%m"},
    {
        "name": "day",
        "type": "date",
        "fmt": "%d",
    },
    {"name": "build", "type": "integer", "start_value": 0},
]

ACTIONS = {
    "build": {
        "type": "conditional_reset",
        "field": "build",
        "update_fields": ["year", "month", "day"],
    },
}

VCS = {
    "name": "git-flow",
    "commit_message": "Version updated from {{ current_version }} to {{ new_version }}",  # noqa
}
