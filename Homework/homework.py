#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def greet(name="Lingma"):
    """
    打招呼函数

    Args:
        name (str): 要问候的名字，默认为"Lingma"

    Returns:
        str: 问候语
    """
    greeting = f"Hello, {name}!"
    print(greeting)
    return greeting


def main():
    """主函数"""
    greet("Lingma")


if __name__ == "__main__":
    main()
print("That's the end of the conversation.")