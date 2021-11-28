# Docker - qa-auto

## Build da Imagem

```bash
docker build -t qa-auto .
```

## Executar Testes

### Todos os testes

```bash
docker run qa-auto
```

### Testes de API

```bash
docker run qa-auto pytest tests/ -m api -v
```

### Testes de UI

```bash
docker run qa-auto pytest tests/ -m ui -v
```

## Docker Compose

### Executar testes de API

```bash
docker-compose up qa-auto
```

### Executar testes de UI

```bash
docker-compose up qa-auto-ui
```

### Executar todos os serviços

```bash
docker-compose up
```

## Volumes

Os relatórios são salvos em `./reports` através de volume mount.

## Variáveis de Ambiente

Configure variáveis de ambiente no `docker-compose.yml`:

```yaml
environment:
  - API_BASE_URL=https://api.example.com
  - TIMEOUT=30
```

## Limpeza

Remover containers:

```bash
docker-compose down
```

Remover imagem:

```bash
docker rmi qa-auto
```
