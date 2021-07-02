brain-games:
	poetry run brain-games

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	for %x in (dist/*.whl) do python -m pip install dist/%x --force-reinstall

lint:
	poetry run flake8 brain_games

.PHONY: brain-games
