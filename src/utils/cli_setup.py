import errors.exceptions as exceptions

def type_machine_input(type: str):
    if verify_type_machine(type) == False:
        raise exceptions.TypeMachineException('Invalid Type!')
    else:
        pass


def verify_type_machine(type: str):
    types = {0: '@AFD', 1: '@AFN', 2: '@APD', 3: '@APN', 4: '@MT', 5: '@ALL'}

    if type in types.values():
        return True
    else:
        return False
