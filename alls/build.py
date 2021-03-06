import os

if __name__ == '__main__':
    print("Building all images...")
    os.chdir("../stk_base")
    os.system("docker compose build --no-cache")
    os.chdir("../stk_data")
    os.system("docker compose build --no-cache")
    os.chdir("../stk_java")
    os.system("docker compose build --no-cache")
    os.chdir("../stk_node")
    os.system("docker compose build --no-cache")
    os.chdir("../run_base")
    os.system("docker compose build --no-cache")
    os.chdir("../run_data")
    os.system("docker compose build --no-cache")
    os.chdir("../run_java")
    os.system("docker compose build --no-cache")
    os.chdir("../run_node")
    os.system("docker compose build --no-cache")
