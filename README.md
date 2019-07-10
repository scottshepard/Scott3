# Scott3
Avant Data Engineering Coding Challenge

# Usage

## Setup

Setup a virtual environment and install the required packages

    pip install -r requirements.txt

Copy the config template and fill in access key, secret key, and bucket with 
your IAM user credientals.

    cp config.yml.example config.yml

## Testing

Run the test script

    python test.py

The test script uses all four functions. It writes to a bucket in both JSON and
CSV formats, then reads that file back down and compares it.
