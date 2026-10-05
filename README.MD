# Backup.pi

Ao pensar em mudar de sistema operacional, percebi que tinham algumas pastas de arquivos que eram importantes e eu não gostaria de perdê-las. 
Como forma de exercitar os meu conhecimentos em python, resolvi criar um script simples que pode ser executado via linha de comando, recebendo 
como argumento o caminho para um arquivo .txt que contem a lista de pastas a serem incluídas no backup.

Ao final será gerado um arquivo chamado 'backup.zip' no working directory contendo o conteúdo compactado das pastas indicadas.

## Tecnologias Utilizadas
- **Python** (versão 3.14.7 - aplicação)
- **Pytest** (versão 9.1.1 - testes unitários)

## Como utilizar

1. Clone o repositório:
```bash
git clone https://github.com/gaiusfonseca/backup-pi.git
cd backup-py
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate # Linux
```

3. Instale as dependências:
```bash
pip install -U pytest
```

4. Crie um arquivo com extensão '.txt', por exemplo 'folders_to_backup.txt' e 
insira nele o caminho absoluto das pastas que deseja realizar o backup. uma pasta por linha.
    Exemplo:
```PlainText
/home/user/Documentos
/home/user/Imagens
```

5. Configure a permissão de execução no script:
```bash
chmod +x backup.py # Linux
```

6. Execute o script passando como argumento o arquivo com as pastas a serem copiadas:
```bash
./backup.py folders_to_backup.txt
```

## Como rodar os testes
1. Primeiro se certifique de que o pytest está instalado:
```bash
pytest --version
```

2. Execute o pytest na raiz do projeto:
```bash
pytest
```