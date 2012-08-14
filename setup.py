from setuptools import setup, find_packages
import os
from telapi import VERSION

setup(
    name                = "TelAPI",
    version             = VERSION,
    description         = "TelAPI REST API client and InboundXML generator",
    author              = "TelAPI",
    author_email        = "help@telapi.com",
    url                 = "https://github.com/telapi/telapi-python/",
    keywords            = ["telapi", "inboundxml", "telephony", "rest"],
    install_requires    = ["requests"],
    packages            = find_packages(),
    package_data        = {'telapi': ['data/*.json']},
    classifiers         = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony"
    ],
    long_description    = """This library interacts with the TelAPI service. It allows you to use the REST API in a pythonic way to initiate and 
manage outbound calls and SMS messages as well as generate InboundXML to handle incoming calls and SMS messages. Check out http://telapi.com for free credits.""",
)
