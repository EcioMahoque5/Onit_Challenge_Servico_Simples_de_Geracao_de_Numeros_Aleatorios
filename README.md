# Serviço Simples de Geração de Números Aleatórios

Esta aplicação é uma API desenvolvida em Flask que gera números aleatórios dentro de um intervalo especificado. O serviço aceita valores mínimos e máximos como entrada no corpo da requisição (payload) e retorna um número aleatório dentro do intervalo, inclusive.

---

## Passos para Executar a Aplicação

1. **Crie um Ambiente Virtual**

   - No diretório do projeto, crie um ambiente virtual:
     ```bash
     python -m venv venv
     ```
   - Ative o ambiente virtual:
     - **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - **Linux/Mac**:
       ```bash
       source venv/bin/activate
       ```

2. \*\*Crie o arquivo `.env`

   - Na raiz do projeto, crie um arquivo chamado `.env`.
   - Adicione a variável `SECRET_KEY` com um valor qualquer:
     ```env
     SECRET_KEY=sua_chave_secreta_aqui
     ```

3. **Instale os Pacotes Necessários**

   - Certifique-se de estar com o ambiente virtual ativado.
   - Instale os pacotes listados no arquivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Execute a Aplicação**

   - No terminal, com o ambiente virtual ativado, execute o arquivo principal:
     ```bash
     python main.py
     ```
   - A aplicação será iniciada no endereço padrão: `http://127.0.0.1:5000`.

---

## Endpoints Disponíveis

### 1. **Gerar Número Aleatório**

- **URL**: `/api/generate_random_number`
- **Método**: `POST`
- **Descrição**: Gera um número aleatório dentro de um intervalo especificado.
- **Cabeçalho**:

  ```json
  Content-Type: application/json
  ```

- **Body (JSON)**:

```json
{
  "min": 1,
  "max": 1000
}
```

- **Resposta de Sucesso (200)**:

  ```json
  {
    "success": true,
    "min": 1,
    "max": 1000,
    "random_number": 693
  }
  ```

- **Resposta de Erro (409 - Entradas Inválidas)**:
  ```json
  {
    "success": false,
    "message": "Validations errors",
    "errors": {
      "min": ["The 'min' value must be a valid integer."],
      "max": ["The 'max' value must be a valid integer."]
    }
  }
  ```

```json
{
  "success": false,
  "message": "Validations errors",
  "errors": {
    "max": ["'Max' value must be greater than or equal to 'min'."]
  }
}
```

## Estrutura do Projeto

. ├── app/
│ ├── init.py
│ ├── configs.py
│ ├── routes.py
│ └── validators.py
├── venv/
├── .env
├── main.py
├── requirements.txt
└── README.md

## Observações

- Certifique-se de que a variável `SECRET_KEY` está configurada no arquivo `.env` antes de executar a aplicação.
- Sempre ative o ambiente virtual antes de instalar os pacotes ou executar a aplicação:
  - **Windows**:
    ```bash
    venv\Scripts\activate
    ```
  - **Linux/Mac**:
    ```bash
    source venv/bin/activate
    ```

---


## Demonstração

- **Local**: `http://127.0.0.1:5000/api/generate_random_number`
- **Hospedado**: 
