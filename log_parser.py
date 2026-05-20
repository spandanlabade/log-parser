with open("server.log", "r") as file:
    for line in file:
        parts = line.split()

        ip = parts[0]
        method = parts[1]
        path = parts[2]
        status = int(parts[3])

        if status == 404:
            print(f"404 detected from {ip}")
            print(f"Request: {method} {path}")
            print()