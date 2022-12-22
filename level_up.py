#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import click


@click.group()
def cl():
    pass


@cl.command()
@click.argument("routes")
@click.option("-s", "--start")
@click.option("-f", "--finish")
@click.option("-n", "--number")
def add_route(routes, start, finish, number):
    """
    Добавить данные о маршруте
    """
    routes = load_routes(routes)
    routes.append(
        {
            'start': start,
            'finish': finish,
            'number': number
        }
    )
    with open(routes, "w", encoding="utf-8") as file_out:
        json.dump(routes, file_out, ensure_ascii=False, indent=4)
    click.secho("Маршрут добавлен", fg='orange')


@cl.command()
@click.argument('routes')
def display_route(routes):
    """
    Отобразить спискок маршрутов
    """
    if routes:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Начальный пункт",
                "Конечный пункт",
                "Номер маршрута"
            )
        )
        print(line)

        for idx, worker in enumerate(routes, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    worker.get('start', ''),
                    worker.get('finish', ''),
                    worker.get('number', 0)
                )
            )
        print(line)
    else:
        print("Список маршрутов пуст.")


@cl.command()
@click.argument('routes')
@click.option("-N", "--numb")
def select_route(routes, period):
    """
    Выбрать маршрут
    """
    result = []
    for employee in routes:
        if employee.get('number') == period:
            result.append(employee)

    return result


def load_routes(routes):
    with open(routes, "r", encoding="utf-8") as f_in:
        return json.load(f_in)


def main():
    cl()


if __name__ == '__main__':
    main()