
# 🌐 Como Criar um Site Estático na AWS

Este guia ensina como hospedar um site estático utilizando a AWS (Amazon Web Services), incluindo configurações de **S3**, **EC2**, **IAM**, e o uso do **AWS CLI**. O objetivo é demonstrar como configurar um bucket S3, fazer upload dos arquivos do site, configurar o AWS CLI para facilitar o gerenciamento e automatizar o processo com um script Bash.

---

## 🛠️ Ferramentas Necessárias

- **AWS CLI** - Para interagir com os serviços da AWS.
- **S3** - Para armazenar os arquivos do seu site estático.
- **EC2** - Para instância de computação (se necessário).
- **IAM** - Para controlar as permissões de acesso.
- **Bash** - Para automação do processo.

---

## 🚀 Passo a Passo

### 1. 📦 **Criando um Bucket S3**
Primeiro, crie um bucket S3 na AWS para armazenar seus arquivos do site.

1. Acesse o Console da AWS e vá até **S3**.
2. Clique em **Criar bucket**.
3. Nomeie o bucket de acordo com o nome do seu site (ex: `meusite.com`).
4. Escolha a região e outras configurações conforme necessário.
5. Após criar o bucket, vá até a guia **Permissões** e configure as permissões públicas para acesso ao conteúdo do bucket.

### 2. ⚙️ **Configurando o AWS CLI**
Para interagir com a AWS através da linha de comando, configure o AWS CLI com as credenciais da sua conta AWS.

```bash
aws configure
```

Este comando pedirá a sua **Access Key ID**, **Secret Access Key**, região e formato de saída.

### 3. 🖥️ **Carregando Arquivos no Bucket S3**

Carregue os arquivos do seu site para o bucket S3 criado:

```bash
aws s3 sync ./meusite/ s3://meusite.com --acl public-read
```

Este comando sincroniza todos os arquivos da pasta local **meusite** para o bucket S3 e garante que os arquivos sejam públicos.

### 4. ⚙️ **Configurando o EC2 (se necessário)**

Se você precisar de um servidor EC2 para algo como um backend ou banco de dados, siga estas etapas:

1. No Console da AWS, acesse **EC2** e clique em **Launch Instance**.
2. Escolha a imagem (Amazon Machine Image - AMI), por exemplo, Ubuntu.
3. Configure as preferências de rede e armazenamento.
4. Crie um novo par de chaves ou use um existente para acessar a instância via SSH.
5. Após a instância ser lançada, configure-a conforme necessário.

### 5. 👨‍💻 **Criando um Script Bash para Automação**

Se você deseja automatizar o processo de upload para o S3, crie um script Bash como este:

```bash
#!/bin/bash
# Definindo variáveis
BUCKET_NAME="meusite.com"
FOLDER_PATH="./meusite"

# Sincronizando arquivos com S3
aws s3 sync $FOLDER_PATH s3://$BUCKET_NAME --acl public-read
```

Salve o script como `upload.sh` e execute-o sempre que desejar atualizar o conteúdo do seu site.

```bash
chmod +x upload.sh
./upload.sh
```

---

## 🔒 **Configurações de Permissão (IAM)**

Para gerenciar o acesso aos recursos da AWS, crie um **IAM User** com permissões específicas para o S3.

1. No Console da AWS, acesse **IAM**.
2. Crie um novo usuário e atribua permissões para **S3** (geralmente `AmazonS3FullAccess`).
3. Salve as credenciais (Access Key ID e Secret Access Key) para configurar o AWS CLI.

---

## 🎉 Conclusão

Agora, seu site está hospedado na AWS com S3 e EC2, e você pode facilmente gerenciar os arquivos usando o AWS CLI ou automatizar o processo com o script Bash.

---

## 📚 Recursos

- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/latest/userguide/)
- [S3 Bucket Documentation](https://docs.aws.amazon.com/s3/index.html)
- [EC2 Instances Guide](https://docs.aws.amazon.com/ec2/index.html)

---




## 👩‍💻 Créditos

Desenvolvido por Ladiane Pinheiro Santana, estudante de Análise e Desenvolvimento de Sistemas – IFPA.  
Este projeto faz parte das práticas com IAM e políticas de permissão na AWS.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/ladiane-pinheiro-santana)
