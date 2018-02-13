#!/bin/sh

export PYTHONPATH=pylint:$PYTHONPATH
echo $PYTHONPATH
pylint --rcfile ./objectcalisthenics.pylintrc lcd
