import functools
from datetime import datetime

def log_transacao(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        print(f"{datetime.now()}: {func.__name__.upper()}")
        resultado = func(*args, **kwargs)
        return resultado
    
    return envelope

class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1