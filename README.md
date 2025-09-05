# Desafio MBA Engenharia de Software com IA - Full Cycle

## Objetivo

O objetivo deste projeto é criar um chat via linha de comando (CLI) que responde a perguntas baseadas *exclusivamente* no conteúdo do arquivo `document.pdf`. Perguntas fora do contexto do PDF não serão respondidas.

## Exemplos de Uso

### Pergunta Dentro do Contexto

**Faça sua pergunta:**
```
PERGUNTA: Qual o faturamento da Empresa SuperTechIABrazil?
RESPOSTA: O faturamento foi de 10 milhões de reais.
```

### Pergunta Fora do Contexto

**Faça sua pergunta:**
```
PERGUNTA: Quantos clientes temos em 2024?
RESPOSTA: Não tenho informações necessárias para responder sua pergunta.
```

## Instalação

1. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução

1. **Inicie o banco de dados:**
   Execute o Docker Compose para subir o serviço do Weaviate.
   ```bash
   docker compose up -d
   ```

2. **Ingestão do Documento:**
   Processe e armazene o conteúdo do `document.pdf` no banco de dados vetorial.
   ```bash
   python src/ingest.py
   ```

3. **Inicie o Chat:**
   Execute o chat para começar a fazer perguntas.
   ```bash
   python src/chat.py
   ```