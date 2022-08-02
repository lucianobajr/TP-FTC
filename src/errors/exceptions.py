# Classe para relatar exceções dos automatos

class AutomatonException(Exception):
    pass

class CLIException(Exception):
    pass
# Não é um DFA
class InvalidDFAClass(AutomatonException):
    pass

# É um estado inválido para o autômato.
class InvalidStateError(AutomatonException):
    pass

# É um simbolo inválido para o autômato.
class InvalidSymbolError(AutomatonException):
    pass

# Possui um estado está faltando na definição do autômato
class MissingStateError(AutomatonException):
    pass

# Possui um simbolo faltando na definição do autômato
class MissingSymbolError(AutomatonException):
    pass

# Estado Inicial inconsistente
class InitialStateError(AutomatonException):
    pass

# Estado Final inconsistente
class FinalStateError(AutomatonException):
    pass

# A entrada foi rejeitada pelo autômato
class RejectionException(AutomatonException):
    pass

# Tipo de Máquina é inválido
class TypeMachineException(CLIException):
    pass