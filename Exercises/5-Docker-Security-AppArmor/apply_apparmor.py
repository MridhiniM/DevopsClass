import docker

client = docker.from_env()

print("Building image from Dockerfile...")
client.images.build(path=".", tag="flask-apparmor")

# Check Docker's available security options
info = client.info()
security_options = info.get("SecurityOptions", [])

print("\nDocker security options:")
for option in security_options:
    print(f"  {option}")

apparmor_available = any("apparmor" in option.lower() for option in security_options)

container = None

try:
    if apparmor_available:
        print("\nAppArmor is available.")
        print("Running container with AppArmor profile...")

        container = client.containers.run(
            "flask-apparmor",
            ports={"5000/tcp": 5051},
            security_opt=["apparmor=my-apparmor-profile"],
            detach=True
        )
    else:
        print("\nAppArmor is NOT available in this Docker environment.")
        print("Running container without an AppArmor profile.")
        print("This is expected on Docker Desktop for macOS.")

        container = client.containers.run(
            "flask-apparmor",
            ports={"5000/tcp": 5051},
            detach=True
        )

    print(f"Container started: {container.short_id}")

    container_info = client.api.inspect_container(container.id)

    print("\nSecurity options applied:")
    print(container_info["HostConfig"]["SecurityOpt"])

    if apparmor_available:
        print("AppArmor profile applied successfully.")
    else:
        print("AppArmor enforcement could not be applied because it is unavailable.")

finally:
    if container:
        print("\nStopping container...")
        container.stop()
        container.remove()

print("Done.")
