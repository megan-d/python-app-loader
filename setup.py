from setuptools import setup

APP = ["app.py"]
DATA_FILES = []
OPTIONS = {
    "plist": {
        "CFBundleName": "FileApp",
    }
}
setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
