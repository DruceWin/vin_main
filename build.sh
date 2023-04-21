
#!/usr/bin/env bash
# exit on error
set -o errexit

export POETRY_HOME="$(pwd)/.poetry"
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$POETRY_HOME/bin:$PATH"
poetry --version

python manage.py collectstatic --no-input
python manage.py migrate