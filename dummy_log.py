import os
import random
import datetime

# Define log directory and number of files
log_dir = "dummy_logs"
num_files = 5  # Change this to generate more files
num_entries_per_file = 10  # Number of log entries per file

# Ensure the directory exists
os.makedirs(log_dir, exist_ok=True)

# Sample log levels and messages
log_levels = ["INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"]
sample_messages = [
    "User login successful",
    "Connection timeout occurred",
    "File not found error",
    "Database connection established",
    "API request failed with status 500",
    "Cache cleared successfully",
    "Memory usage high, consider scaling",
    "Authentication failed for user admin",
]

# Function to generate random log entries
def generate_log_entry():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level = random.choice(log_levels)
    message = random.choice(sample_messages)
    return f"{timestamp} [{level}] - {message}"

# Create and populate log files
for i in range(1, num_files + 1):
    file_path = os.path.join(log_dir, f"log_{i}.txt")
    with open(file_path, "w") as file:
        for _ in range(num_entries_per_file):
            file.write(generate_log_entry() + "\n")

print(f"Dummy log directory '{log_dir}' created with {num_files} log files.")
