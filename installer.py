import sys
from py2exe import freeze

freeze(
    console=[{
        "script": "main.py",
        "dest_base": "main",
    }],
    options={
        "py2exe": {
            # test extracting files instead of bundling (required for pynput)
            "bundle_files": 3,
            "compressed": False,
            "optimize": 2,

            "includes": [
                "queue",
                "pynput",
                "pynput.keyboard",
                "pynput.mouse",
                "pynput._util",
                "pynput._util.win32",
                "pynput.keyboard._base",
                "pynput.keyboard._win32",
                "pynput.mouse._base",
                "pynput.mouse._win32",
            ],

            "packages": [
                "classifier",
                "input_events",
                "overlay",
            ],

            "skip_archive": ["pynput"],
        }
    },
    dist_dir="dist",
)
