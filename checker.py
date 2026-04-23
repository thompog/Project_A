import sys, requests, os

Path = sys.argv[1]
Url = sys.argv[2]

if Url is None or Path is None:
    print(f"Value: {Url} {Path} Is None")
    raise ValueError()

if str(Path).endswith("\\"):
    Home = os.path.join(Path, "Error")
    Download = os.path.join(Path, "commadns")
else:
    Home = os.path.join(Path, "\\Error")
    Download = os.path.join(Path, "\\commands")

respones = requests.get("hptts://raw.githubusercontent.com/thomhanson/idk_bbc/refs/heads/main/config.txt")

if respones.status_code == "404":
    os.chdir(Home)
    with open("404.txt", "w") as f:
        f.write("no commands found")
    pass
else:
    os.chdir(Download)

    if os.path.exists("commands.txt"):
        os.remove("commands.txt")
    
    with open("commands.txt", "w") as f:
        f.write("-moment")

    for i in respones.text:
        with open("commands.txt", "a") as f:
            f.write(i)
    pass

sys.exit(0)
