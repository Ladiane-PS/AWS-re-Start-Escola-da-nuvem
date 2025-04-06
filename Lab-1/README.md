# 🚀 Projeto AWS – Subir Servidor Web com Amazon EC2 e Apache

Este guia apresenta um passo a passo prático para criação de um servidor web simples usando uma instância EC2 na AWS com Apache HTTP Server.

---

## 📑 Sumário

- [✅ Resumo das Etapas](#-resumo-das-etapas--subir-servidor-web-com-ec2-e-apache)
  - [🔹 Tarefa 1: Acessar o serviço EC2](#-tarefa-1-acessar-o-serviço-ec2)
  - [🔹 Tarefa 2: Configurar a Instância EC2](#-tarefa-2-configurar-a-instância-ec2)
  - [🔹 Tarefa 3: Inserir Script de Inicialização (Apache)](#-tarefa-3-inserir-script-de-inicialização-apache)
  - [🔹 Tarefa 4: Executar e Testar a Instância](#-tarefa-4-executar-e-testar-a-instância)
  - [✅ Finalizando](#-finalizando)
- [👩‍💻 Créditos](#-créditos)

---

## ✅ Resumo das Etapas – Subir Servidor Web com EC2 e Apache

### 🔹 Tarefa 1: Acessar o serviço EC2

1. Acesse o [Console da AWS](https://aws.amazon.com/console).
2. Selecione uma **região** (ex: `us-east-1`).
3. No menu, clique em **EC2**.
4. Vá em **Instâncias** > **Executar instâncias**.

---

### 🔹 Tarefa 2: Configurar a Instância EC2

1. **Nome da instância:** `Servidor Web EC2`
2. **Imagem da AMI:** `Amazon Linux 2 (64-bit x86)`
3. **Tipo de instância:** `t2.micro` (gratuito)
4. **Par de chaves:** *Nenhuma* (usar acesso via navegador)
5. **Rede:** Manter padrão
6. **Sub-rede:** Qualquer disponível
7. **Auto-atribuir IP público:** Habilitado
8. **Grupo de segurança:**
   - Criar um novo grupo
   - Nome: `Apache Web SG`
   - Tipo: `HTTP`
   - Porta: `80`
   - Fonte: `Anywhere (0.0.0.0/0)`

---

### 🔹 Tarefa 3: Inserir Script de Inicialização (Apache)

Na seção **Dados do usuário**, cole o script abaixo para instalar e iniciar o Apache automaticamente:

```
#!/bin/bash
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo "<html><h1>Servidor Web Apache - EC2</h1><p>Funcionando corretamente!</p></html>" > /var/www/html/index.html
```
### 🔹 Tarefa 4: Executar e Testar a Instância
1. Clique em Executar instância

2. Acesse a aba Instâncias em execução

3. Aguarde o status ficar 2/2 verificações aprovadas

4. Copie o DNS público ou o IP público

5. Acesse via navegador:

```
http://<DNS-ou-IP-público>

```
Se tudo estiver certo, verá a mensagem:
```
Servidor Web Apache - EC2
Funcionando corretamente!

```
## ✅ Finalizando
- ✅ Apache instalado com sucesso

- ✅ Página HTML servida pela EC2

- ⚠️ Importante: Encerre a instância para evitar cobranças desnecessárias:
Ações > Instância > Encerrar instância
## 👩‍💻 Créditos

Desenvolvido por Ladiane Pinheiro Santana, estudante de Análise e Desenvolvimento de Sistemas – IFPA.
Este projeto faz parte das práticas com EC2, servidor web Apache e inicialização automatizada com shell script na AWS

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/ladiane-pinheiro-santana)

