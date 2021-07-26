brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

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
