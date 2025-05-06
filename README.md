# Bloqueador de Sites em Python

Este projeto é um script simples em Python desenvolvido para bloquear o acesso a sites específicos no seu computador. É uma ferramenta útil para melhorar a produtividade, evitando distrações durante períodos de trabalho ou estudo.

## 🚀 Funcionalidades

* Bloqueio de sites especificados pelo usuário.
* Modificação do arquivo `hosts` do sistema para redirecionar domínios indesejados.
* Compatível com sistemas Windows e Linux.
* Execução contínua para manter os sites bloqueados.

## 🛠️ Tecnologias Utilizadas

* Python 3.x
* Manipulação de arquivos do sistema (`hosts`)

## ⚠️ Requisitos

* Python 3 instalado no sistema.
* Permissões de administrador para modificar o arquivo `hosts`.

## 💻 Como Usar

1. Clone este repositório:

   ```
   git clone https://github.com/GuilhermmeDev/bloqueador-de-sites-py.git
   ```



2. Navegue até o diretório do projeto:

   ```
   cd bloqueador-de-sites-py
   ```



3. Execute o script com privilégios de administrador:

   * No Windows:

     ```
     python bloqueador.py
     ```
   * No Linux:

     ```
     sudo python3 bloqueador.py
     ```

4. Siga as instruções no terminal para adicionar ou remover sites da lista de bloqueio.

## 📄 Observações

* O script modifica o arquivo `hosts` do sistema, redirecionando os domínios especificados para `127.0.0.1`, efetivamente bloqueando o acesso a esses sites.
* Certifique-se de executar o script com as permissões necessárias para evitar erros de acesso.
* Para que o bloqueio seja efetivo, mantenha o script em execução durante o período desejado.
