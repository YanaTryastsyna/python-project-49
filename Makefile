.PHONY: install build package-install brain-games

install:
	uv sync

build:
	uv build

package-install:
	uv pip install --force-reinstall dist/*.whl

brain-games:
	uv run brain-games



