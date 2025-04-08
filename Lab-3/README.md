

# 💻 Laboratório AWS IAM – Gerenciamento de Usuários, Grupos e Políticas  🔐


Este laboratório tem como objetivo apresentar o serviço **AWS Identity and Access Management (IAM)**, permitindo explorar como usuários, grupos e políticas funcionam dentro da AWS. O gerenciamento de acesso é essencial para garantir a segurança e o controle de recursos em ambientes corporativos.

---

## 📑 Sumário

- [✅ Resumo das Etapas – IAM na AWS](#-resumo-das-etapas--iam-na-aws)
  - [🔹 Tarefa 1: Criar uma Política de Senha de Conta](#-tarefa-1-criar-uma-política-de-conta)
  - [🔹 Tarefa 2: Explorar Usuários e Grupos](#-Tarefa-2-Explorar-Usuários-e-Grupos)
  - [🔹 Tarefa 3: Adicionar Usuários a Grupos](#-Tarefa-3-Adicionar-Usuários-a-Grupos)
  - [🔹 Tarefa 4: Testar Permissões dos Usuários IAM](#-Tarefa-4-Testar-Permissões-dos-Usuários-IAM)
  - [🔹 Tarefa 5: Testar o login do novo usuário](#-tarefa-5-testar-o-login-do-novo-usuário)
  - [✅ Resumo da Tarefa 4](#-Resumo-da-Tarefa-4)
- [👩‍💻 Créditos](#-créditos)

---

## ✅ Resumo das Etapas – IAM na AWS

## 🔹 Tarefa 1: Criar uma Política de Senha de Conta

**Objetivo:** Reforçar os requisitos de senha para todos os usuários da conta AWS.

### ✔ Etapas:
1. Acesse o Console da AWS e vá até o serviço **IAM**.
2. No menu lateral, clique em **Configurações da conta**.
3. Clique em **Alterar política de senha**.
4. Configure conforme abaixo:
   - Comprimento mínimo: `10 caracteres`
   - Marcar todas as opções, exceto:
     - Expiração da senha requer redefinição do administrador
   - Expiração: `90 dias`
   - Histórico de senhas: impedir reutilização das últimas `5`

5. Clique em **Salvar alterações**.

**Resultado:** Política de senha reforçada e ativa para todos os usuários da conta.

---

## 🔹 Tarefa 2: Explorar Usuários e Grupos

**Objetivo:** Avaliar os usuários e os grupos de usuários existentes na conta IAM.

### 👤 Usuários Criados:
- `usuario-1`
- `usuario-2`
- `usuario-3`

### 👥 Grupos de Usuários:
- `EC2-Administrador`
- `Suporte EC2`
- `Suporte S3`

### 🔑 Permissões dos Grupos:

| Grupo             | Tipo de Política     | Permissões                                                                 |
|------------------|----------------------|---------------------------------------------------------------------------|
| Suporte EC2       | Gerenciada (AWS)     | `AmazonEC2ReadOnlyAccess` – acesso somente leitura ao EC2                |
| Suporte S3        | Gerenciada (AWS)     | `AmazonS3ReadOnlyAccess` – acesso somente leitura ao S3                  |
| EC2-Administrador | Inline (Personalizada)| Visualizar, iniciar e parar instâncias EC2                               |

**Observações:**
- Grupos simplificam o gerenciamento de permissões para múltiplos usuários.
- Políticas gerenciadas são reutilizáveis e mantidas pela AWS.
- Políticas inline são exclusivas de um grupo/usuário e usadas para casos específicos.

---


## 🔹 Tarefa 3: Adicionar Usuários a Grupos

**Objetivo:** Associar usuários aos grupos corretos, com base em seus papéis no sistema.

### 🧩 Associação de Usuários a Grupos:

| Usuário   | Grupo             | Permissão                                                       |
|-----------|-------------------|-----------------------------------------------------------------|
| usuario-1 | Suporte S3         | Acesso somente leitura ao S3                                   |
| usuario-2 | Suporte EC2        | Acesso somente leitura ao EC2                                  |
| usuario-3 | EC2-Administrador  | Visualizar, iniciar e parar instâncias EC2                     |

### ✔ Etapas:
1. Vá até **Grupos de usuários** no painel IAM.
2. Clique no grupo desejado (ex: `Suporte S3`).
3. Selecione a aba **Usuários** e clique em **Adicionar usuários**.
4. Escolha o usuário correspondente e confirme.
5. Repita o processo para os demais usuários e grupos.

**Resultado:** Cada usuário está associado corretamente a seu respectivo grupo com as permissões adequadas.

---

## 🔹 Tarefa 4: Testar Permissões dos Usuários IAM

**Objetivo:** Verificar se as permissões atribuídas aos usuários `usuario-1`, `usuario-2` e `usuario-3` estão funcionando corretamente no Console da AWS.

---

### 🧪 Etapas de Teste

#### 🔗 Acessar URL de Login IAM

1. No console do IAM, acesse o painel **Conta da AWS**.
2. Copie a **URL de login para usuários do IAM**, semelhante a:
3. Abra uma **janela privada/anônima** no seu navegador:
- **Firefox:** Menu → Nova janela privativa
- **Chrome:** Menu (três pontos) → Nova janela anônima
- **Edge:** Menu (três pontos) → Nova janela InPrivate
- **Internet Explorer:** Ferramentas → Navegação InPrivate

4. Cole a URL e pressione **Enter**.

---

### 👤 Testar Permissões de `usuario-1`

1. **Login**:
- Nome de usuário: `user-1`
- Senha: `Lab-Password1`

2. **S3**:
- Vá em **Serviços → S3**
- Acesse um bucket e visualize seu conteúdo.
- ✅ Acesso permitido (membro do grupo `S3-Support`)

3. **EC2**:
- Vá em **Serviços → EC2 → Instâncias**
- ❌ Mensagem: *Você não está autorizado a executar esta operação* (sem permissão para EC2)

4. **Logout**:
- Parte superior direita → `user-1` → Sair

---

### 👤 Testar Permissões de `usuario-2`

1. **Login**:
- Nome de usuário: `user-2`
- Senha: `Lab-Password2`

2. **EC2**:
- Vá em **Serviços → EC2 → Instâncias**
- ✅ Visualiza instâncias EC2 (permissão somente leitura)
- ❌ Ao tentar parar instância: *Você não está autorizado a executar esta operação*

3. **S3**:
- Vá em **Serviços → S3**
- ❌ Mensagem: *Você não tem permissão para listar buckets*

4. **Logout**:
- Parte superior direita → `user-2` → Sair

---

### 👤 Testar Permissões de `usuario-3`

1. **Login**:
- Nome de usuário: `user-3`
- Senha: `Lab-Password3`

2. **EC2**:
- Vá em **Serviços → EC2 → Instâncias**
- ✅ Permissão total sobre instâncias EC2 (visualizar, parar)
- Ao escolher a instância e clicar em **Parar instância**, o status muda para **Parando**

3. **Logout**:
- Feche a janela privada.




## ✅ Resumo da Tarefa 4

| Usuário   | S3 (Buckets)       | EC2 (Visualizar) | EC2 (Parar instância) |
|-----------|--------------------|------------------|------------------------|
| user-1    | ✅ Acesso           | ❌ Sem acesso     | ❌ Sem acesso          |
| user-2    | ❌ Sem acesso       | ✅ Leitura        | ❌ Sem permissão       |
| user-3    | ❌ Não testado      | ✅ Acesso total   | ✅ Pode parar instância|

---

> Com isso, foi validado que cada usuário recebeu as permissões corretas conforme seu papel no ambiente da AWS. O princípio do menor privilégio foi respeitado em todas as configurações.

---



## 👩‍💻 Créditos

Desenvolvido por Ladiane Pinheiro Santana, estudante de Análise e Desenvolvimento de Sistemas – IFPA.  
Este projeto faz parte das práticas com IAM e políticas de permissão na AWS.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/ladiane-pinheiro-santana)
