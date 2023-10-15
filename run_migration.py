import subprocess

subprocess.run(["flask", "db", "init"])
subprocess.run(["flask", "db", "migrate"])
subprocess.run(["flask", "db", "upgrade"])
