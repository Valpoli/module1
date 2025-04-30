import sys
sys.path.append("modules/moduleA")
sys.path.append("modules/moduleB")

from module1.core import run_all

if __name__ == "__main__":
    print("== Module1 runner ==")
    run_all()
