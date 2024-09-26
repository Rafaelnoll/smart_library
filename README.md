# MVP Biblioteca Inteligente

Este repositório contém o código e a documentação do MVP (Produto Mínimo Viável) de uma biblioteca inteligente, desenvolvido com o uso de Raspberry Pi. O principal objetivo do projeto é facilitar a busca de livros pelos alunos, proporcionando uma experiência intuitiva e eficiente.

O sistema permite que o usuário selecione o livro desejado, e, por meio de luzes instaladas nos corredores, indica a localização exata do item. Cada usuário pode escolher uma cor, que acenderá a lâmpada correspondente no corredor onde o livro está, orientando-o visualmente até o local.

Além disso, o controle de usuários é realizado com a tecnologia RFID, garantindo um registro preciso de quem está utilizando o sistema e quais livros estão sendo consultados.

## Integrantes do Projeto

- **Bernardo Gatto**
- **Bryan Vanz**
- **Jean Hefler**
- **Luis Eduardo dos Santos**
- **Rafael Noll**


## Funcionalidades

- **Login via RFID**: Os usuários podem autenticar-se facilmente aproximando seus cartões ou tags RFID do leitor.
- **Seleção de cor para orientação visual**: Após escolher um livro, o usuário pode selecionar uma cor específica que acenderá a lâmpada no corredor onde o livro está localizado, facilitando a navegação.
- **Confirmação de retirada com RFID**: A retirada do livro é confirmada por meio do sistema RFID, garantindo um controle preciso e automatizado dos empréstimos.
- **Interface**: Uma interface simples, disponível via Raspberry Pi, permite que os usuários façam login e selecionem os livros de forma rápida e eficiente.

## Tecnologias Utilizadas

- **Raspberry Pi**: Plataforma de hardware responsável pela execução do sistema de automação e controle.
- **Python (Flask)**: Framework utilizado no backend para gerenciar a lógica de negócios e as rotas da aplicação de forma eficiente.
- **HTML, CSS, JavaScript**: Tecnologias de frontend que oferecem uma interface interativa e amigável para os usuários.
- **RFID**: Tecnologia utilizada para autenticação de usuários e controle de acesso, garantindo a identificação precisa durante as interações.

## Como Iniciar a Aplicação

Siga os passos abaixo para configurar e iniciar a aplicação corretamente:

1. **Crie um ambiente virtual utilizando `venv`**:
   Primeiro, vamos criar um ambiente virtual para garantir que as dependências da aplicação sejam isoladas do seu ambiente global Python.

   ```bash
   python -m venv env

2. **Entrar no ambiente virtual**
  - **2.1 (Linux)**
     ```bash
     source env/bin/activate

  - **2.2 (Windows)**
     ```bash
     .\env\Scripts\activate

3. **Inicial Aplicação**
     ```bash
     python index.py

