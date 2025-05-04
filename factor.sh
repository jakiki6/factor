#!/bin/sh

python3 setup.py && python3 sieve.py && python3 postprocess.py && python3 linalg.py

rm -fr data
