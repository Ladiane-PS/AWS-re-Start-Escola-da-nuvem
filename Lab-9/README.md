
# **AWS Systems Manager - Laboratório de Prática** 🖥️

## Visão Geral 🔍

O **AWS Systems Manager** é um conjunto de ferramentas poderosas para gerenciar recursos da Amazon Web Services (AWS). Ele permite centralizar dados operacionais, automatizar tarefas e configurar uma variedade de recursos em escala. Com o Systems Manager, é possível gerenciar instâncias do Amazon EC2, servidores locais, máquinas virtuais, e muito mais.

Neste laboratório, você aprenderá a utilizar o **Systems Manager** para:

- 📋 Verificar configurações e permissões
- ⚙️ Executar tarefas em vários servidores
- 🔄 Atualizar configurações ou definições do aplicativo
- 💻 Acessar a linha de comando em uma instância

**Duração**: Aproximadamente 30 minutos ⏳

---

## Acessando o AWS Management Console 🌐

1. **Iniciar o laboratório** 🚀:
   - Escolha **Iniciar laboratório** para iniciar o laboratório.
   - Aguarde até que a mensagem "Status do laboratório: pronto" apareça e, em seguida, feche o painel.

2. **Acessar o Console de Gerenciamento da AWS**:
   - Ao lado de "Iniciar Laboratório", selecione **AWS** para abrir o Console da AWS em uma nova aba.
   - Certifique-se de permitir pop-ups, caso necessário.

3. **Configuração do Console**:
   - Organize o Console para que ele fique ao lado deste documento, facilitando sua navegação.
   - **Não altere a região** da AWS, a menos que seja explicitamente instruído.

---

## **Tarefas do Laboratório** 🛠️

### **Tarefa 1: Gerar Listas de Inventário para Instâncias Gerenciadas** 📝

1. No Console do AWS, pesquise por **Systems Manager** na barra de pesquisa.
2. No painel de navegação esquerdo, clique em **Gerenciador de frotas**.
3. Selecione **Configurar inventário** e preencha as informações:
   - Nome: `Inventory-Association`
   - Alvo: Selecione **Instância Gerenciada**
4. Escolha **Configurar Inventário**.
5. Após o sucesso, navegue até o link **ID do nó** e selecione a aba **Inventário** para revisar os aplicativos instalados.

---

### **Tarefa 2: Instalar um Aplicativo Personalizado Usando o Comando Executar** ⚙️

1. No painel esquerdo do Console, em **Gerenciamento de nós**, clique em **Executar Comando**.
2. Selecione o comando **Executar** e escolha o documento de instalação do **Dashboard de Fabricação de Widgets**.
3. Selecione **Instância Gerenciada** e execute o comando.
4. Após 1-2 minutos, verifique se o status está como **Sucesso**.
5. Valide a instalação:
   - Abra uma nova aba do navegador e cole o **IP público** fornecido.
   - O painel de widgets será exibido.

---

### **Tarefa 3: Usar o Parameter Store para Gerenciar as Configurações do Aplicativo** 🔒

1. Retorne ao **AWS Systems Manager** e acesse **Armazenamento de parâmetros**.
2. Clique em **Criar parâmetro** e preencha:
   - Nome: `/dashboard/show-beta-features`
   - Descrição: `Display beta features`
   - Valor: `True`
3. O aplicativo automaticamente exibirá recursos adicionais conforme a configuração do parâmetro.

---

### **Tarefa 4: Usar o Gerenciador de Sessões para Acessar Instâncias** 🖥️

1. No painel de navegação esquerdo, acesse **Gerenciador de Sessão**.
2. Selecione **Iniciar sessão** e escolha **Instância Gerenciada**.
3. Execute comandos no shell interativo, como:
   ```bash
   ls /var/www/html
   ```
4. Verifique a saída para listar os arquivos do aplicativo instalado.
5. Execute também:
   ```bash
   curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone
   ```
6. Este comando retorna a zona de disponibilidade da instância EC2.

---

## **Conclusão** 🎉

Parabéns! Você completou com sucesso as seguintes tarefas:

- ✅ **Verificação de configurações e permissões**
- ✅ **Execução de tarefas em vários servidores**
- ✅ **Atualização de configurações ou definições do aplicativo**
- ✅ **Acesso à linha de comando em uma instância**

Agora você pode **encerrar o laboratório**. Se estiver satisfeito, clique em **Encerrar laboratório** no topo da página.

---

## **Recursos Adicionais** 📚

- [O que é o AWS Systems Manager?](https://aws.amazon.com/systems-manager/)
- [Gerenciador de Sessões do AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)

Para mais informações sobre treinamento e certificação da AWS, consulte a [página de treinamento e certificação da AWS](https://aws.amazon.com/training/).

---




## 👩‍💻 Créditos

Desenvolvido por Ladiane Pinheiro Santana, estudante de Análise e Desenvolvimento de Sistemas – IFPA.  
Este projeto faz parte das práticas com IAM e políticas de permissão na AWS.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/ladiane-pinheiro-santana)
