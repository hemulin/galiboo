
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.getcwd(), moduleos.p))
sys.path.append(parent_dir)

from module.app import app

def main():
    app.run()

if __name__ == '__main__':
    main()