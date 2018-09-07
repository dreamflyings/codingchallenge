#!/bin/bash

for f in "*.py"; do
  yapf -i $f --style pep8
done
