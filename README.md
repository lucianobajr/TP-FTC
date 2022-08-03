# TP-FTC

## Structure folders

    ├── data                      # arquivos de entrada
    ├── docs                      # documentação 
    ├── src                       # Source 
    │   ├── errors                  # expections errors              
    │   ├── utils                   # setups to machines and utils
    │   ├── packages              # pacotes
    │   │    ├── dfa.py           # Automato Finito Determinístico    
    │   │    │── fna.py           # Automato Finito Não determinístico
    │   ├──  cli.py              # Arquivo Principal cli
    │   ├──  gui.py              # Arquivo Principal gui       
    │   

## Architecture

![SO](https://user-images.githubusercontent.com/45442173/182651535-8ba41749-c875-4767-b22d-71e79bcf3908.png)


## Libraries Required
- customtkinter
- json

### Install Libraries required run:

    $ pip3 install customtkinter
    $ pip3 install customtkinter --upgrade
    $ pip3 install json

## AFD

Composto por 5 tuplas `{Q, Σ, q, F, δ}`. 

    Q : conjunto de todos os estados.
    Σ : conjunto de símbolos de entrada ou alfabeto. (Símbolos que a máquina recebe como entrada).
    q : Estado inicial.
    F : conjunto de estado final.
    δ : Função de Transição, definida como δ : Q X Σ --> Q.

## AFN

Composto por 5 tuplas (Q, Σ, δ, I, F ).

    Q : conjunto de todos os estados.
    Σ : alfabeto. (Símbolos que a máquina recebe como entrada).
    I : subconjunto de Q, é um conjunto não vazio de estados iniciais.
    F : subconjunto de Q, é o conjunto de estados finais.
    δ : a função de transição, é uma função total de E × Σ para P(E).

## APD

Composto por 7 tuplas (Q, Σ, Γ, q0, Z, F, δ).

    Q:  é o conjunto de estados
    ∑:  é o conjunto de símbolos de entrada
    Γ:  é o conjunto de símbolos de empilhamento (que podem ser empurrados e retirados da pilha)
    q0: é o estado inicial
    Z:  é o símbolo de empilhamento inicial (que está inicialmente presente na pilha)
    F:  é o conjunto dos estados finais
    δ:  é uma função de transição que mapeia Q x {Σ ∪ ∈} x Γ em Q x Γ*. Em um determinado estado, o PDA lerá o símbolo de entrada e o símbolo da pilha (topo da pilha) e passará para um novo estado e alterará o símbolo da pilha.

## GUI

![interface](https://user-images.githubusercontent.com/45442173/182651519-0579cf66-9409-43db-9a9b-7031dee12052.png)