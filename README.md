# TP-FTC

## Structure folders

    ├── data                      # arquivos de entrada
    ├── docs                      # documentação 
    ├── out                       # output              
    ├── src                       # Source    
    │   ├── packages              # pacotes
    │   │    ├── dfa.py           # Automato Finito Determinístico    
    │   │    │
    │   ├──  main.py              # Arquivo Principal
    ├── Makefile                  # Build Scripts       
    │   


## AFD

Composto por 5 tuplas `{Q, Σ, q, F, δ}`. 

    Q : conjunto de todos os estados.
    Σ : conjunto de símbolos de entrada ou alfabeto. (Símbolos que a máquina recebe como entrada)
    q : Estado inicial.
    F : conjunto de estado final.
    δ : Função de Transição, definida como δ : Q X Σ --> Q.