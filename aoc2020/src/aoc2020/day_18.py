""" Day 18: Operation Order
The solution is based on the Shunting-yard algorithm
and the Reverse Polish Notation
"""
import os
from functools import partial
import click


def parse_input(input_path):
    """Parse the input"""
    expressions = []
    with open(os.path.abspath(input_path)) as input_file:
        for line in input_file:
            expressions.append(list(filter(lambda x: x != " ", line.rstrip("\n"))))

    return expressions


def convert_expression(expression, precedence):
    """ Convert the expression to a Reverse Polish Notation"""
    out_queue = []
    op_stack = []

    for token in expression:
        if token.isnumeric():
            out_queue.append(int(token))
        elif token in ["+", "*"]:
            while (
                len(op_stack) > 0
                and precedence[op_stack[-1]] >= precedence[token]
                and op_stack[-1] != "("
            ):
                out_queue.append(op_stack.pop())

            op_stack.append(token)

        elif token == "(":
            op_stack.append(token)

        elif token == ")":
            while len(op_stack) > 0 and op_stack[-1] != "(":
                out_queue.append(op_stack.pop())

            if len(op_stack) > 0 and op_stack[-1] == "(":
                op_stack.pop()

    while len(op_stack) > 0:
        out_queue.append(op_stack.pop())

    return out_queue


def solve_expression(expression):
    """ Solve the expression """
    stack = []
    for token in expression:
        if token in ["+", "*"]:
            op1 = stack.pop()
            op2 = stack.pop()

            if token == "+":
                stack.append(op1 + op2)
            elif token == "*":
                stack.append(op1 * op2)
        else:
            stack.append(token)

    return stack[0]


def calculate(precedence, expression):
    """ Calculate an expression based on the given precedence """
    parsed = convert_expression(expression, precedence)
    return solve_expression(parsed)


def sum_expressions(expressions, precedence):
    """ Sum the results of all the expressions """
    calculate_precedence = partial(calculate, precedence)
    return sum(map(calculate_precedence, expressions))


@click.command()
@click.argument("input_path", type=click.Path(exists=True))
def main(input_path):
    """ AOC Day 18 Main """

    expressions = parse_input(input_path)

    precedence = {
        "+": 1,
        "*": 1,
        "(": 3,
        ")": 0,
    }

    precedence_v2 = {
        "+": 2,
        "*": 1,
        "(": 3,
        ")": 0,
    }

    click.echo("Day 18: Operation Order")
    click.echo(f"Part 1: {sum_expressions(expressions, precedence)}")
    click.echo(f"Part 2: {sum_expressions(expressions, precedence_v2)}")
