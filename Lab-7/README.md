# 💻 Criação de Instâncias do Amazon EC2

## 📖 Visão Geral do Laboratório
A AWS fornece várias maneiras de iniciar instâncias EC2. Neste laboratório você irá:
- 🚀 Iniciar um **Bastion Host** via **AWS Management Console**  
- 🔐 Conectar-se ao Bastion Host com **EC2 Instance Connect**  
- 🌐 Lançar um **Servidor Web** via **AWS CLI**

O diagrama a seguir ilustra a arquitetura final, com uma VPC pública contendo um Bastion Host e um Servidor Web.

---

## 🎯 Objetivos
- Iniciar uma instância EC2 usando o Console da AWS  
- Conectar-se à instância com EC2 Instance Connect  
- Lançar outra instância EC2 via AWS CLI

---


## 🛠️ Pré‑requisitos
- Conta AWS com permissão para EC2  
- Acesso ao **AWS Management Console**  
- AWS CLI instalada (no Bastion Host)  

---

## 📋 Passo a Passo

### 📋 Tarefa 1: Iniciar o Bastion Host (Console)
1. **Iniciar laboratório** e abrir o Console AWS (não mude a região).  
2. Pesquise **EC2** e clique em **Iniciar instância**.  
3. **Nome & Tags**: `Bastion host`.  
4. **AMI**: Amazon Linux 2 (ou 2023).  
5. **Tipo**: `t3.micro`.  
6. **Par de chaves**: “Prosseguir sem par de chaves”.  
7. **Rede**:  
   - VPC: `Lab VPC`  
   - Sub‑rede: `Sub‑rede Pública`  
   - IP público: **Habilitar**  
8. **Segurança**:  
   - Nome: `Bastion security group`  
   - Descrição: `Permit SSH connections`  
9. **Armazenamento**: 8 GiB (padrão).  
10. **Função IAM**: `Bastion-Role`.  
11. Clique em **Iniciar instância** e **Exibir todas as instâncias**.

---

### 📋 Tarefa 2: Conectar ao Bastion Host
12. Selecione a instância `Bastion host`.  
13. Clique em **Conectar** → **EC2 Instance Connect** → **Connect**.  
14. Agora você está no terminal da instância.

---

### 📋 Tarefa 3: Lançar o Servidor Web (AWS CLI)
#### 1️⃣ Obter parâmetros via CLI
```bash
# Defina a região
AZ=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)
export AWS_DEFAULT_REGION=${AZ::-1}

# AMI mais recente
AMI=$(aws ssm get-parameters   --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2   --query 'Parameters[0].Value' --output text)
echo "AMI: $AMI"

# Sub‑rede pública
SUBNET=$(aws ec2 describe-subnets   --filters "Name=tag:Name,Values=Sub-rede pública"   --query Subnets[].SubnetId --output text)
echo "SUBNET: $SUBNET"

# Security Group Web
SG=$(aws ec2 describe-security-groups   --filters "Name=group-name,Values=WebSecurityGroup"   --query SecurityGroups[].GroupId --output text)
echo "SG: $SG"
```

#### 2️⃣ Baixar e visualizar script de dados do usuário
```bash
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSJAWS-1-23732/171-lab-JAWS-create-ec2/s3/UserData.txt
cat UserData.txt
```

#### 3️⃣ Lançar instância servidor web
```bash
INSTANCE=$(aws ec2 run-instances   --image-id $AMI   --subnet-id $SUBNET   --security-group-ids $SG   --user-data file://UserData.txt   --instance-type t3.micro   --iam-instance-profile Name=WebServer-Role   --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer}]'   --query 'Instances[0].InstanceId' --output text)
echo "INSTÂNCIA: $INSTANCE"
```

#### 4️⃣ Aguardar e verificar status
```bash
# Aguarde até “running”
aws ec2 describe-instances --instance-ids $INSTANCE   --query 'Reservations[].Instances[].State.Name' --output text
```

#### 5️⃣ Testar servidor web
```bash
DNS=$(aws ec2 describe-instances --instance-ids $INSTANCE   --query 'Reservations[].Instances[].PublicDnsName' --output text)
echo "Acesse: http://$DNS"
```

---

## 🎯 Desafios Opcionais
- 🔒 **Conectar** à instância “Misconfigured Web Server” e corrigir regras de segurança.  
- 🛠️ **Ajustar** instalação do servidor web na instância mal configurada e validar acesso HTTP.

---

## ✅ Conclusão
Você concluiu com sucesso:
- Início de instâncias via Console e CLI  
- Conexão segura com EC2 Instance Connect  
- Lançamento de servidor web automatizado  

---

## 📚 Recursos Adicionais
- 📘 [Documentação EC2](https://docs.aws.amazon.com/ec2/)  
- 📘 [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/)  
- 📘 [Data de usuário & scripts EC2](https://docs.aws.amazon.com/ec2/latest/userguide/user-data.html)


## 👩‍💻 Créditos

Desenvolvido por Ladiane Pinheiro Santana, estudante de Análise e Desenvolvimento de Sistemas – IFPA.  
Este projeto faz parte das práticas com IAM e políticas de permissão na AWS.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/ladiane-pinheiro-santana)
