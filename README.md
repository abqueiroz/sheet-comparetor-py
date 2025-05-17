# Como Criar e Executar um Projeto em Python

Python é uma linguagem de programação versátil e amplamente utilizada. Este guia irá mostrar-te como criar e executar um projeto em Python, desde a configuração do teu ambiente até à execução do teu código.

## 1. Instalar o Python

Se ainda não tens o Python instalado, precisas de o descarregar e instalar.

* **Windows:**
    * Vai para o site oficial do Python: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
    * Descarrega a versão mais recente do Python 3.
    * Executa o instalador e certifica-te de que a opção "Add Python to PATH" está selecionada.
* **macOS:**
    * O macOS vem com o Python pré-instalado, mas normalmente é uma versão mais antiga. Podes instalar uma versão mais recente a partir do site oficial: [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/) ou usar um gestor de pacotes como o Homebrew: [https://brew.sh/](https://brew.sh/)
* **Linux:**
    * O Python geralmente já está instalado. Podes verificar a versão com o comando `python3 --version` no terminal. Se precisares de instalar ou atualizar, usa o gestor de pacotes da tua distribuição (por exemplo, `apt` para Ubuntu/Debian, `yum` ou `dnf` para Fedora/CentOS).

## 2. Escolher um Editor de Código

Um editor de código torna a escrita de código mais fácil e eficiente. Aqui estão alguns editores de código populares para Python:

* **Visual Studio Code (VS Code):** Gratuito, poderoso e com muitas extensões.
* **PyCharm:** Opção paga com uma versão Community gratuita, especificamente para Python.
* **Sublime Text:** Opção paga com avaliação gratuita, leve e personalizável.
* **Atom:** Gratuito e personalizável (descontinuado, mas ainda utilizável).

## 3. Criar um Diretório de Projeto

É boa prática organizar os teus projetos em diretórios. Abre o teu terminal ou linha de comandos e cria um novo diretório para o teu projeto.

\`\`\`bash
mkdir meu\_projeto
cd meu\_projeto
\`\`\`

## 4. Criar um Ambiente Virtual (Recomendado)

Um ambiente virtual isola as dependências do teu projeto, evitando conflitos com outros projetos.

\`\`\`bash
python3 -m venv venv # Cria um ambiente virtual chamado "venv"
\`\`\`

Ativa o ambiente virtual:

* **Windows:**

    \`\`\`bash
    venv\\Scripts\\activate
    \`\`\`
* **macOS/Linux:**

    \`\`\`bash
    source venv/bin/activate
    \`\`\`

## 5. Criar um Ficheiro Python

Cria um novo ficheiro com a extensão \`.py\`. Este ficheiro conterá o teu código Python.

\`\`\`bash
# Usando o terminal
touch main.py # Cria um ficheiro chamado main.py

# Ou cria um ficheiro no teu editor de código
\`\`\`

Abre o ficheiro no teu editor de código e escreve algum código Python.

\`\`\`python
def saudacao(nome):
    print(f"Olá, {nome}!")

if __name__ == "__main__":
    nome = input("Qual é o teu nome? ")
    saudacao(nome)
\`\`\`

## 6. Executar o teu Código Python

No teu terminal, certifica-te de que estás no diretório do teu projeto e que o teu ambiente virtual está ativado. Em seguida, executa o teu script Python:

\`\`\`bash
python main.py
\`\`\`

A saída do teu programa será exibida no terminal.

## 7. Gerir Dependências

Se o teu projeto depender de pacotes externos, usa o pip para os instalar. Cria um ficheiro \`requirements.txt\` para listar as dependências do teu projeto:

\`\`\`bash
# requirements.txt
requests==2.28.1
\`\`\`

Instala as dependências:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Estrutura do Projeto de Exemplo

Aqui está uma estrutura de projeto de exemplo para um projeto Python mais complexo:

\`\`\`
meu\_projeto/
├── venv/ # Diretório do ambiente virtual
├── src/ # Código fonte da aplicação
│ ├── main.py # Ponto de entrada principal
│ ├── utils.py # Módulos utilitários
│ └── ...
├── tests/ # Testes
│ ├── test\_main.py
│ └── ...
├── data/ # Ficheiros de dados
├── docs/ # Documentação
├── requirements.txt # Dependências do projeto
└── README.md # Descrição do projeto
\`\`\`

Este guia dá-te as bases para criar e executar projetos em Python. À medida que fores ganhando mais experiência, podes explorar tópicos mais avançados, como frameworks web, bases de dados e desenvolvimento de aplicações.
