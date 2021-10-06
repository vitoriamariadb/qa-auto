#!/usr/bin/env python3
import sys
import subprocess

def run_tests(test_type="all"):
    if test_type == "api":
        cmd = ["pytest", "tests/", "-m", "api", "-v"]
    elif test_type == "ui":
        cmd = ["pytest", "tests/", "-m", "ui", "-v"]
    else:
        cmd = ["pytest", "tests/", "-v"]

    subprocess.run(cmd)

def run_tui():
    subprocess.run(["python", "tui.py"])

def main():
    print("qa-auto - Framework de Automação de Testes")
    print("Versão: 0.5.0")
    print()
    print("Opções:")
    print("1. Executar testes API")
    print("2. Executar testes UI")
    print("3. Executar todos os testes")
    print("4. Interface TUI")
    print("0. Sair")
    print()

    choice = input("Escolha uma opção: ").strip()

    if choice == "1":
        run_tests("api")
    elif choice == "2":
        run_tests("ui")
    elif choice == "3":
        run_tests("all")
    elif choice == "4":
        run_tui()
    elif choice == "0":
        sys.exit(0)
    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()
