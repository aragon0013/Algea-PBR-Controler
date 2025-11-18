import time
import sys
import signal
import select

def handle_sigterm(signum, frame):
    print("SIGTERM erhalten, sauber beenden...")
    measure["running"] = False

measure = {"running":True}
counter = 0

signal.signal(signal.SIGTERM, handle_sigterm)
sys.stdout.write("initialize sensor program...\n")
sys.stdout.flush()
time.sleep(2)

while measure["running"]:
    sys.stdout.write("__________________\n")
    sys.stdout.write(f"Loop{counter}\n")
    sys.stdout.write("sensor01:pH_data\n")
    sys.stdout.write("sensor02:conductivity_data\n")
    sys.stdout.write("sensor03:temperature_data\n")
    sys.stdout.flush()
    counter += 1
    time.sleep(2)