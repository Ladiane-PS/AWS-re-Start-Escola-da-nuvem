# 🚀 Projeto AWS – Criar VPC e Iniciar Servidor Web

Este guia apresenta um passo a passo prático para criação de uma infraestrutura básica na AWS, utilizando o serviço VPC e EC2 para subir um servidor web.

---

## 📑 Sumário

- [✅ Resumo das Etapas](#-resumo-das-etapas--criar-vpc-e-iniciar-servidor-web-na-aws)
  - [🔹 Tarefa 1: Criar a VPC](#-tarefa-1-criar-a-vpc)
  - [🔹 Tarefa 2: Criar Sub-redes adicionais](#-tarefa-2-criar-sub-redes-adicionais)
  - [🔹 Tarefa 3: Associar Sub-redes às Tabelas de Rotas](#-tarefa-3-associar-sub-redes-às-tabelas-de-rotas)
  - [🔹 Tarefa 4: Criar Grupo de Segurança](#-tarefa-4-criar-grupo-de-segurança)
  - [🔹 Tarefa 5: Iniciar Instância EC2 (Servidor Web)](#-tarefa-5-iniciar-instância-ec2-servidor-web)
  - [✅ Finalizando](#-finalizando)
- [👩‍💻 Créditos](#-créditos)

---

## ✅ Resumo das Etapas – Criar VPC e Iniciar Servidor Web na AWS

### 🔹 Tarefa 1: Criar a VPC

1. Acesse o **VPC** pelo console da AWS.  
2. Clique em **Criar VPC** > selecione **VPC e mais**.  
3. Configure os campos abaixo:

- **IPv4 CIDR:** `10.0.0.0/16`  
- **AZs:** `1`  
- **Sub-rede pública:** `10.0.0.0/24`  
- **Sub-rede privada:** `10.0.1.0/24`  
- **Gateway NAT:** `1 AZ`

4. Nomeie os recursos:

- **VPC:** `Lab VPC`  
- **Sub-redes:** `Public Subnet 1, Private Subnet 1`  
- **Tabelas de rotas:** `Public Route Table, Private Route Table`

5. Clique em **Criar VPC** e depois em **Exibir VPC**.

---

### 🔹 Tarefa 2: Criar Sub-redes adicionais

1. Vá em **Sub-redes** > **Criar sub-rede**.  
2. Crie uma sub-rede pública:

- **Nome:** `Public Subnet 2`  
- **CIDR:** `10.0.2.0/24`

3. Crie uma sub-rede privada:

- **Nome:** `Private Subnet 2`  
- **CIDR:** `10.0.3.0/24`

---

### 🔹 Tarefa 3: Associar Sub-redes às Tabelas de Rotas

1. Vá em **Tabelas de rotas**.  
2. Associe:

- `Public Subnet 2` à **Public Route Table**  
- `Private Subnet 2` à **Private Route Table**

---

### 🔹 Tarefa 4: Criar Grupo de Segurança

1. Vá em **Grupos de segurança** > **Criar grupo de segurança**.  
2. Configure:

- **Nome:** `Web Security Group`  
- **Descrição:** Enable HTTP access  
- **VPC:** Lab VPC

3. Em **Regras de entrada**, adicione:

- **Tipo:** HTTP  
- **Fonte:** Anywhere IPv4  
- **Descrição:** Permit web requests

---

### 🔹 Tarefa 5: Iniciar Instância EC2 (Servidor Web)

1. Vá para **EC2** > **Instâncias** > **Iniciar instância**.  
2. Configure:

- **Nome:** `Web Server 1`  
- **AMI:** Amazon Linux 2  
- **Tipo:** `t3.micro`  
- **Par de chaves:** `vockey`  

3. Rede:

- **VPC:** `Lab VPC`  
- **Sub-rede:** `Public Subnet 2`  
- **IP público:** Habilitar  
- **Grupo de segurança:** `Web Security Group`

4. Em **Dados do usuário**, cole o seguinte script:

```
#!/bin/bash
# Instalar Apache Web Server e PHP
yum install -y httpd mysql php

# Baixar arquivos de laboratório
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RESTRT-1/267-lab-NF-build-vpc-web-server/s3/lab-app.zip
unzip lab-app.zip -d /var/www/html/

# Ligar servidor web
chkconfig httpd on
service httpd start
```
## ✅ Finalizando

Acesse o IP público da instância no navegador.
Se tudo estiver correto, você verá o site web funcionando com os arquivos do laboratório.

## 👩‍💻 Créditos

Desenvolvido por **Ladiane Pinheiro Santana**, estudante de Análise e Desenvolvimento de Sistemas – IFPA.  
Orientado para práticas com **AWS**, **VPC**, **EC2** e **infraestrutura de redes**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/ladiane-pinheiro-santana)

