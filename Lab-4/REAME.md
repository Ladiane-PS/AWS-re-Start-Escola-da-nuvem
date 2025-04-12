# 🚀 Projeto AWS – Criação de Banco de Dados com Amazon RDS

Este guia apresenta um passo a passo prático para criar e configurar um banco de dados na Amazon Web Services (AWS) utilizando o serviço Amazon RDS.

---

## 📑 Sumário

- [✅ Resumo das Etapas](#-resumo-das-etapas--criação-de-banco-de-dados-com-amazon-rds)
  - [🔹 Tarefa 1: Criar um grupo de segurança para a instância do RDS DB](#-tarefa-1-criar-um-grupo-de-segurança-para-a-instância-do-rds-db)
  - [🔹 Tarefa 2: Criar um grupo de sub-redes de banco de dados](#-tarefa-2-criar-um-grupo-de-sub-redes-de-banco-de-dados)
  - [🔹 Tarefa 3: Criar uma instância de banco de dados do Amazon RDS](#-tarefa-3-criar-uma-instância-de-banco-de-dados-do-amazon-rds)
  - [🔹 Tarefa 4: Interaja com seu banco de dados](#-tarefa-4-interaja-com-seu-banco-de-dados)
  - [✅ Finalizando](#-finalizando)
- [👩‍💻 Créditos](#-créditos)

---

## ✅ Resumo das Etapas – Criação de Banco de Dados com Amazon RDS

### 🔹 Tarefa 1: Criar um grupo de segurança para a instância do RDS DB

1. No Console da AWS, vá para **EC2**.
2. No menu à esquerda, clique em **Security Groups** (Grupos de segurança).
3. Clique em **Create Security Group**.
    - Nome do grupo de segurança: `DB Security Group` 
    - Descrição: `Permit access from Web Security Group`
    - VPC: VPC de laboratório 

4. Na aba **Inbound Rules**, adicione a regra de entrada:
   - Tipo: **MySQL/Aurora**
   - Fonte: Digite `sg` no campo de pesquisa e selecione Web Security Group .
6. Clique em **Create**.

---

### 🔹 Tarefa 2: Criar um grupo de sub-redes de banco de dados

1. No AWS Management Console, selecione o **Menu Serviços** e, em seguida, selecione **RDS** em **Banco de dados** .
2. No painel de navegação esquerdo, clique em **Grupos de sub-rede**. e depois **Criar grupo de sub-rede de banco de dados**
    - **Nome:** `DB Subnet Group`
    - **Descrição:** `DB Subnet Group`
    - **ID da VPC:** `VPC do laboratório`

3. Na seção Adicionar sub-redes para Zonas de disponibilidade , clique:
     - Selecionea primeira zona de disponibilidade
     - Selecionea segunda zona de disponibilidade
4. Adicione uma **sub-rede pública ou privada** conforme necessário para seu banco de dados.
5. Preencha os detalhes da sub-rede e clique em **Create**.

---

### 🔹 Tarefa 3: Criar uma instância de banco de dados do Amazon RDS

1. Acesse o Console da AWS e selecione **RDS**.
2. Clique em **Databases** > **Create database**.
3. Escolha o **motor do banco de dados** (ex: **MySQL**).
4. Configure as opções conforme necessário:
   - **Nome do banco de dados**: `meu_banco_de_dados`
   - **ID da instância do banco de dados**: `db-meubanco`
   - **Credenciais de administrador**: 
     - **Usuário**: `admin`
     - **Senha**: Escolha uma senha segura.
   - **Classe da instância**: `db.t2.micro` (para uso gratuito, se aplicável).
   - **Armazenamento**: Defina 20 GB ou o necessário.
5. Na configuração de rede, selecione a **VPC** e a **sub-rede** criada na Tarefa 2.
6. Adicione o **grupo de segurança** criado na Tarefa 1 para a instância RDS.
7. Clique em **Create database**.

---

### 🔹 Tarefa 4: Interaja com seu banco de dados

1. Após a criação da instância, clique sobre a instância RDS criada.
2. Na aba de detalhes, copie o **endpoint** (DNS) da instância.
3. Utilize um cliente MySQL ou qualquer ferramenta de sua escolha para se conectar ao banco de dados.

   Comando para conexão via terminal:
   
   ```bash
   mysql -h <endpoint-do-banco> -u admin -p
✅ Finalizando
Agora você tem um banco de dados Amazon RDS configurado e acessível, com segurança, rede e recursos bem definidos.




## 👩‍💻 Créditos

Desenvolvido por Ladiane Pinheiro Santana, estudante de Análise e Desenvolvimento de Sistemas – IFPA.  
Este projeto faz parte das práticas com IAM e políticas de permissão na AWS.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/ladiane-pinheiro-santana)
