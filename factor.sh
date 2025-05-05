#!/bin/sh

if [ ! -f data/relations.json ]; then
    python3 setup.py
fi

python3 sieve.py && python3 postprocess.py && python3 linalg.py && rm -fr data
