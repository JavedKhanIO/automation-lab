import time
import os

LOG_DIR = "logs.txt"

if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

print("Log Aggregator started.monitoring logs...\n")

while True:
        try:
                for file in os.listdir(LOG_DIR):
                        file_path = os.path.join(LOG_DIR, file)
                        with open(file_path, "r") as f:
                                lines = f.readlines()[-5:] #shows last 5 lines
                                print(f"---{file}---")
                                for line in lines:
                                        print(line.strip())
                print("\n====================================\n")
                time.sleep(10)
        except Exception as e:
                print("error reading logs:", e)
                time.sleep(5)
