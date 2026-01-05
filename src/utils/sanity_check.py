import sys
import platform

def main():
    print("Python version:", sys.version)
    print("Executable:", sys.executable)
    print("Platform:", platform.platform())

if __name__ == "__main__":
    main()