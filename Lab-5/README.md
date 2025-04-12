
# 🚀 Acesso SSH à Instância Amazon EC2 via PowerShell (Windows)

Este guia descreve como acessar sua instância Amazon EC2 usando o **PowerShell** no Windows com a chave SSH `.pem`.

---

## 🔑 Pré-requisitos

- Instância EC2 em execução
- IP público da instância
- Chave SSH no formato `.pem` (baixada no momento da criação da instância)
- PowerShell instalado (presente por padrão no Windows)

---

## ⚙️ Etapas para Conexão via PowerShell

### 1. Localize sua chave `.pem`

Certifique-se de que a chave `.pem esteja salva em um diretório conhecido. Exemplo: `C:\Users\SeuUsuario\Downloads\labsuser.pem`

> 🔒 A chave deve ter permissão restrita. Veja o próximo passo.

---

### 2. Altere as permissões da chave

Abra o PowerShell e execute o seguinte comando para restringir o acesso à chave:

```powershell
icacls "C:\Users\SeuUsuario\Downloads\labsuser.pem" /inheritance:r
icacls "C:\Users\SeuUsuario\Downloads\labsuser.pem" /grant:r "$($env:USERNAME):(R)"
```

---

### 3. Conecte-se à instância EC2

No PowerShell, use o comando abaixo para iniciar a conexão SSH (substitua `<ip-público>` pelo IP real da sua instância e o caminho da chave):

```powershell
ssh -i "C:\Users\SeuUsuario\Downloads\labsuser.pem" ec2-user@<ip-público>
```

---

### 4. Confirme a conexão

Na primeira vez, o PowerShell pedirá confirmação de confiança no host. Digite:

```text
yes
```

Se tudo estiver correto, você será conectado à instância EC2.

---

## ✅ Finalizando o Laboratório

1. No topo da página do ambiente, clique em **Encerrar laboratório**
2. Confirme clicando em **Sim**
3. Aguarde a mensagem "Encerrado AWS Lab com Sucesso"

---

**Parabéns! Conexão SSH realizada com sucesso via PowerShell. 🚀**

---



## 👩‍💻 Créditos

Desenvolvido por Ladiane Pinheiro Santana, estudante de Análise e Desenvolvimento de Sistemas – IFPA.  
Este projeto faz parte das práticas com IAM e políticas de permissão na AWS.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/ladiane-pinheiro-santana)
