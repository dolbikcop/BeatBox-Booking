### Python version 3.10.4

## Установка и обновление зависимостей
```bash
poetry install --with dev,test
poetry update --with dev
poetry add <packagename> --group dev
poetry remove <packagename> --group test
```

## Форматирование кода
```bash
black ./app
```
