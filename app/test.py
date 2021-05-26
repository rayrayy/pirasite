import subprocess

result = subprocess.run(['boot'],
                                    capture_output=True,
                                    text=True,
                                    check=True)