# 🐍 Compilado de Pequenos Projetos em Python

Bem-vindo a este repositório onde você encontrará uma coleção de pequenos projetos desenvolvidos em Python. Estes projetos são ideais para iniciantes que desejam aprender, praticar ou aprimorar suas habilidades em programação Python.

---
# 💼 Sistema Bancário em Python

Este projeto simula um sistema bancário simples, implementado em Python. Ele oferece funcionalidades como depósitos, saques, transferências e criação de usuários e contas.

---

## 📋 Funcionalidades

- **Gerenciamento de Contas**: Criação de contas bancárias e usuários.
- **Transações**: Depósitos, saques e transferências entre contas.
- **Histórico de Transações**: Consulta do extrato detalhado de cada conta.
- **Limite de Saques**: Respeito ao limite de saques diários e valor máximo de saque.

---

## 📂 Estrutura de Classes

O projeto utiliza a orientação a objetos com as seguintes classes:

### `Cliente`
Representa um cliente do banco, armazenando o endereço e as contas associadas.

### `PessoaFisica`
Subclasse de `Cliente`, que adiciona atributos específicos como nome, CPF e data de nascimento.

### `Conta`
Representa uma conta bancária, com métodos para sacar, depositar e acessar o saldo e histórico de transações.

### `ContaCorrente`
Subclasse de `Conta` com regras adicionais, como limite de saque e quantidade máxima de saques diários.

### `Historico`
Armazena todas as transações de uma conta.

### `Transacao`, `Saque` e `Deposito`
Classes abstratas e concretas que representam as operações bancárias.

---

# Projeto de Controle de Ponto com Tkinter, MySQL e CSV

Este projeto implementa um sistema de controle de ponto utilizando `Tkinter` para a interface gráfica, `MySQL` para o armazenamento de dados de usuários e registros de entradas/saídas, e `CSV` para exportar os dados localmente.

## Estrutura do Projeto

O projeto contém as seguintes funcionalidades:

1. **Registro de Usuários**
2. **Registro de Entradas e Saídas**
3. **Exportação de Registros para CSV**
4. **Recuperação de Senha**

### Dependências

O projeto utiliza as seguintes bibliotecas:

```python
import csv
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import customtkinter
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import sys

