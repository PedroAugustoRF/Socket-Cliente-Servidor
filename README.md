---

# 💬 Sistema de Comunicação Cliente-Servidor com Sockets em Python

Este projeto implementa um **sistema simples de comunicação em rede utilizando Sockets em Python**, permitindo a troca de mensagens entre um **cliente** e um **servidor** através de conexão TCP.

A aplicação simula um **chat via terminal**, onde o cliente envia mensagens ao servidor e o servidor responde em tempo real.

O objetivo do projeto é demonstrar conceitos fundamentais de **programação em redes**, incluindo criação de sockets, estabelecimento de conexão, envio e recebimento de dados.

---

# 📚 Conceitos Aplicados

Este projeto utiliza diversos conceitos importantes de programação de redes:

* **Sockets TCP**
* **Comunicação Cliente-Servidor**
* **Endereçamento IP**
* **Portas de comunicação**
* **Envio e recebimento de dados**
* **Codificação e decodificação de mensagens**
* **Loop de comunicação contínua**

---

# 🗂 Estrutura do Projeto

```
trabalho_socket_py/
│
├── servidor.py
├── cliente.py
└── README.md
```

### 📄 servidor.py

Responsável por:

* Criar o socket do servidor
* Associar o servidor a um **IP e porta**
* Aguardar conexões de clientes
* Receber mensagens
* Enviar respostas ao cliente

### 📄 cliente.py

Responsável por:

* Criar o socket do cliente
* Conectar ao servidor
* Enviar mensagens digitadas pelo usuário
* Receber respostas do servidor

---

# ⚙️ Tecnologias Utilizadas

* **Python 3**
* **Biblioteca Socket (nativa do Python)**

Não é necessário instalar bibliotecas externas.

---

# 🚀 Como Executar o Projeto

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

---

## 2️⃣ Acesse a pasta do projeto

```bash
cd trabalho_socket_py
```

---

## 3️⃣ Execute primeiro o servidor

```bash
python servidor.py
```

Saída esperada:

```
Servidor aguardando conexão...
```

---

## 4️⃣ Execute o cliente em outro terminal

```bash
python cliente.py
```

---

# 💻 Exemplo de Funcionamento

### No servidor

```
Servidor aguardando conexão...
Conectado com ('127.0.0.1', 52144)

Cliente: Olá servidor
Você: Olá cliente
```

---

### No cliente

```
Você: Olá servidor
Servidor: Olá cliente
```

---

# 🔎 Explicação Técnica

## Criação do Socket

```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

* **AF_INET** → utiliza protocolo IPv4
* **SOCK_STREAM** → define comunicação via **TCP**

---

## Associação do Servidor à Porta

```python
servidor.bind((host, porta))
```

Define o endereço onde o servidor ficará escutando conexões.

---

## Aguardando Conexões

```python
servidor.listen()
```

Coloca o servidor em modo de escuta para conexões de clientes.

---

## Aceitando Conexão

```python
conexao, endereco = servidor.accept()
```

Estabelece a conexão entre cliente e servidor.

---

## Envio de Mensagens

```python
conexao.send(resposta.encode())
```

As mensagens são convertidas para bytes utilizando **encode()**.

---

## Recebimento de Mensagens

```python
mensagem = conexao.recv(1024).decode()
```

* **1024** → tamanho máximo do buffer de dados
* **decode()** → converte bytes novamente para string

---

# 🎯 Objetivo Educacional

Este projeto foi desenvolvido com fins acadêmicos para demonstrar:

* funcionamento básico de **comunicação em rede**
* implementação de **cliente e servidor**
* uso prático da biblioteca **socket**
* troca de mensagens em tempo real

---

# 📈 Possíveis Melhorias

Algumas evoluções possíveis para o projeto:

* suporte a **múltiplos clientes**
* criação de **interface gráfica**
* implementação de **chat em grupo**
* tratamento de **exceções de rede**
* criação de **logs de mensagens**

---

# 👨‍💻 Autor

**Eduardo Santana Cruz Almeida e apoio de Pedro Augusto Ribeiro Ferreira**
Estudantes de **Engenharia de Software**

---
