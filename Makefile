.PHONY: install build package-install brain-games

install:
	uv sync

test-coverage:
	uv run pytest --cov=brain_games --cov-report=xml:coverage.xml

build:
	uv build

package-install:
	uv pip install --force-reinstall dist/*.whl

brain-games:
	uv run brain-games
	
lint:
	uv run ruff check brain_games
	
test:
	uv pip install pytest  # Установка зависимостей
	uv run pytest -v


