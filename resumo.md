Resumo – Prova P1 (Parte 2)

É um método dentro da classe, mas que não usa self nem cls.

Serve pra funções “extras” que têm a ver com a classe, mas não precisam acessar nem o objeto nem a própria classe.

Tipo uma função utilitária guardada lá dentro só pra organizar melhor.

Dataclasses

Chegaram no Python 3.7 pra facilitar a vida.

Criam sozinhas coisas chatas como __init__, __repr__, __eq__.

São perfeitas pra classes que basicamente servem pra guardar dados.

Eventos de Domínio

Ideia que vem do DDD (Domain-Driven Design).

Representam algo importante que aconteceu no sistema.

Exemplo: quando uma categoria é criada, ativada, desativada, etc.

Bom pra acompanhar histórico e integrar com outros sistemas sem misturar lógica de negócio.

Decoradores

São funções que embrulham outras funções ou classes pra dar um poder extra.

Você não muda o código original, só adiciona comportamento.

Exemplos que usamos muito: @staticmethod, @classmethod, @property.

DDD (Domain-Driven Design)

Jeito de pensar o sistema com foco no negócio e não só em código.

A ideia é que o código “fale a linguagem” do domínio (da regra de negócio).

Normalmente se divide em: Entidades, Value Objects, Repositórios, Serviços e Eventos de Domínio.