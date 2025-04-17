
# 💻 Instalar e Configurar a AWS CLI

## Visão Geral do Laboratório

A AWS Command Line Interface (AWS CLI) é uma ferramenta de linha de comando que fornece uma interface para interagir com produtos e serviços da Amazon Web Services (AWS).

Você pode instalar a AWS CLI na sua máquina local ou em uma máquina virtual, como uma instância do Amazon EC2 (Elastic Compute Cloud).

Nesta atividade, você instalará e configurará a AWS CLI em uma instância do Red Hat Linux, pois esse tipo de instância não tem a AWS CLI pré-instalada.

Durante esta atividade, você:
- Estabelecerá uma conexão SSH com a instância.
- Configurará a CLI com chave de acesso à conta AWS.
- Utilizará a CLI para interagir com o IAM.

## 📦 Objetivos

- Instalar e configurar a AWS CLI.
- Conectar a AWS CLI a uma conta AWS.
- Acessar o IAM usando a AWS CLI.



## Acessando o AWS Management Console

1. Escolha **Iniciar laboratório**.
2. Aguarde a mensagem **"Status do laboratório: pronto"** e feche o painel.
3. Escolha **AWS** ao lado de "Iniciar Laboratório" para abrir o Console da AWS.
4. Habilite pop-ups se necessário.
5. **Importante:** Não altere a região padrão do laboratório.

---

## Tarefa 1: Conectar à instância do Red Hat EC2 via SSH

### Usuários do Windows

1. Acesse o menu **Detalhes** > **Mostrar**.
2. Baixe o arquivo `labsuser.ppk`.
3. Anote o endereço **PublicIP**.
4. Baixe e abra o **PuTTY**.
5. Configure o PuTTY para se conectar à instância (consulte tutorial oficial da AWS).

### Usuários de macOS e Linux

1. Acesse o menu **Detalhes** > **Mostrar**.
2. Baixe `labsuser.pem`.
3. Copie o **PublicIP**.
4. No terminal:
```bash
cd ~/Downloads
chmod 400 labsuser.pem
ssh -i labsuser.pem ec2-user@<endereço-ip>
```

---

## ✅ Tarefa 2: Instalar a AWS CLI

No terminal SSH:

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip -u awscliv2.zip
sudo ./aws/install
aws --version
aws help
```

---

## ✅ Tarefa 3: Observar o IAM no Console

1. No Console da AWS, procure e selecione **IAM**.
2. Vá em **Usuários > awsstudent**.
3. Na aba **Permissões**, clique na seta ao lado de `lab_policy` e veja o botão **{ } JSON**.
4. Em **Credenciais de segurança**, anote o **ID da chave de acesso**.

---

## ✅ Tarefa 4: Configurar a AWS CLI

```bash
aws configure
```
Insira os dados conforme solicitado:
- Access Key ID: [copiar do painel]
- Secret Access Key: [copiar do painel]
- Região: `us-west-2`
- Formato de saída: `json`

---

## ✅ Tarefa 5: Verificar IAM pela AWS CLI

```bash
aws iam list-users
```

A resposta será um JSON com usuários do IAM.

---

## Desafio: Baixar `lab_policy` via AWS CLI

1. Use a documentação oficial da CLI.
2. Liste as políticas com escopo `Local`.
3. Obtenha o número da versão da política.
4. Use a CLI para obter a política completa no formato JSON.
5. Salve a saída em um arquivo:

```bash
aws iam get-policy-version --policy-arn <ARN-da-Política> --version-id <ID-da-Versão> > lab_policy.json
```

---

## Resumo

Este laboratório demonstrou como instalar e configurar a AWS CLI em uma instância EC2, além de acessar e interagir com o serviço IAM pela linha de comando.


## 👩‍💻 Créditos

Desenvolvido por Ladiane Pinheiro Santana, estudante de Análise e Desenvolvimento de Sistemas – IFPA.  
Este projeto faz parte das práticas com IAM e políticas de permissão na AWS.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/ladiane-pinheiro-santana)
