
# 💻 Laboratório AWS IAM – Gerenciamento de Usuários, Grupos e Políticas

## 📚 Visão Geral

Este laboratório tem como objetivo apresentar o serviço **AWS Identity and Access Management (IAM)**, permitindo explorar como usuários, grupos e políticas funcionam dentro da AWS. O gerenciamento de acesso é essencial para garantir a segurança e o controle de recursos em ambientes corporativos.

## 🎯 Objetivos

Ao final deste laboratório, você será capaz de:

- Criar e aplicar uma política de senha personalizada no IAM.
- Explorar usuários e grupos pré-criados no IAM.
- Inspecionar políticas aplicadas aos grupos de usuários.
- Adicionar usuários a grupos com permissões específicas.
- Localizar e utilizar o URL de login do IAM.
- Compreender os efeitos das políticas no acesso aos serviços da AWS.

## 🛠️ Pré-requisitos

- Conta de laboratório AWS Academy ou ambiente de prática com acesso ao IAM.
- Navegador habilitado para pop-ups.

## ⏱️ Duração

Aproximadamente **60 minutos**.

## 📌 Etapas Realizadas

### ✅ Tarefa 1: Criar uma Política de Senha

1. Acesse o serviço **IAM** via Console AWS.
2. Vá em **Configurações da conta** → **Alterar política de senha**.
3. Configure os requisitos:
   - Mínimo de **10 caracteres**.
   - Marque as opções: letras maiúsculas, minúsculas, números e caracteres especiais.
   - Expiração em **90 dias**.
   - Impedir reutilização das **últimas 5 senhas**.
4. Clique em **Salvar alterações**.

🔒 Resultado: A conta agora possui uma política de senha mais segura e exigente.

### ✅ Tarefa 2: Explorar Usuários e Grupos IAM

#### 👤 Usuários IAM

- Três usuários foram identificados: `usuario-1`, `usuario-2`, `usuario-3`.
- O `usuario-1` não tem permissões nem pertence a nenhum grupo.

#### 👥 Grupos IAM

Três grupos foram criados previamente:

| Grupo           | Tipo de Política         | Permissões Principais                                |
|------------------|---------------------------|--------------------------------------------------------|
| EC2-Admin        | Política **inline**       | Visualizar, iniciar e parar instâncias EC2.            |
| EC2-Support      | Política **gerenciada**   | Somente leitura sobre EC2, ELB, CloudWatch, AutoScale. |
| S3-Support       | Política **gerenciada**   | Somente leitura de buckets e objetos no Amazon S3.     |

## 🧠 Conceitos-Chave

- **Usuários IAM**: Representam indivíduos ou serviços que acessam a AWS.
- **Grupos IAM**: Conjunto de usuários com permissões comuns.
- **Políticas IAM**:
  - **Gerenciadas**: Criadas pela AWS ou pelo administrador.
  - **Inline**: Específicas de um único usuário ou grupo.
- **Declaração de Política**:
  - `"Effect"`: `Allow` ou `Deny`.
  - `"Action"`: Ações permitidas (ex: `ec2:DescribeInstances`).
  - `"Resource"`: Recursos afetados (ex: `*` ou recurso específico).

## 🧪 Resultado Esperado

Ao seguir as instruções, o ambiente IAM estará configurado com:
- Políticas de senha fortalecidas.
- Grupos com permissões distintas e controladas.
- Compreensão do efeito das políticas no acesso de usuários aos serviços AWS.

## 📎 Observações

- Políticas **gerenciadas** facilitam a manutenção e reutilização.
- Políticas **inline** são úteis para exceções pontuais.
- Sempre revise as permissões antes de atribuir a usuários.
