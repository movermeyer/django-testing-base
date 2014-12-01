VENV_NAME ?= venv
PIP ?= pip

ACTIVATE_VENV = . $(VENV_NAME)/bin/activate
SETUP = ./setup.py

pip: venv
	$(ACTIVATE_VENV) && \
	$(PIP) install -r pip_requirements.txt && \
	$(PIP) install -e .

venv:
	virtualenv -p python3 $(VENV_NAME)

clean:
	-rm -rf dist *.egg-info

