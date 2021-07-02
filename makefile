brain-games:
    poetry run brain-games

install:
    poetry install

build:
	poetry build

publish:
    publish --dry-run.

package-install:
    for %x in (dist/*.whl) do python -m pip install dist/%x --force-reinstall

.PHONY: brain-games