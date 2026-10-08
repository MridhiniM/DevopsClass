import docker

client = docker.from_env()

container = None

try:
    container = client.containers.run(
        "flask-apparmor",
        ports={"5000/tcp": 5051},
        detach=True
    )

    print(f"Container started: {container.short_id}")

    # Test reading /etc/passwd
    exit_code, output = container.exec_run(
        ["cat", "/etc/passwd"]
    )

    print(
        f"Attempt to read /etc/passwd: "
        f"Exit Code {exit_code}, Output: {output.decode()}"
    )

    # Test executing /bin/bash
    exit_code, output = container.exec_run(
        ["/bin/bash", "-c", "echo Bash executed"]
    )

    print(
        f"Attempt to execute /bin/bash: "
        f"Exit Code {exit_code}, Output: {output.decode()}"
    )

finally:
    if container:
        container.stop()
        container.remove()
        print("Container stopped and removed.")
