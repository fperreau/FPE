#!/usr/bin/python3
import subprocess

def test(device_path):
    result=subprocess.run(['sudo','lvs'], capture_output=True, text=True, check=True)
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)

if __name__ == "__main__":
    device_path="/dev/vg00"
    new_size="10G"
    test(device_path)
   