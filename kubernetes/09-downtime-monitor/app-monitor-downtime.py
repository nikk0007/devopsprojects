import subprocess
import time
from datetime import datetime, timezone

def get_local_time():
    return time.strftime('%Y-%m-%d %H:%M:%S')

def get_utc_time():
    utc_time = datetime.utcnow()
    return utc_time.strftime('%Y-%m-%d %H:%M:%S UTC')

def check_app_status():
    url = 'https://google.com'
    
    try:
        # Run curl command and capture the output
        result = subprocess.run(['curl', '-v', url], capture_output=True, text=True, timeout=60)
        print(">> " + result.stdout)
        local_timestamp = get_local_time()
        utc_timestamp = get_utc_time()

        with open('app_status_log.txt', 'a') as log_file:
            # Check if the string "Connected to google.com" is present in the response
            if 'The document has moved' in result.stdout:
                log_file.write(f"{local_timestamp} / {utc_timestamp} - App is up and running\n")
            else:
                log_file.write(f"{local_timestamp} / {utc_timestamp} - App is down\n")

    except subprocess.TimeoutExpired:
        local_timestamp = get_local_time()
        utc_timestamp = get_utc_time()
        with open('app_status_log.txt', 'a') as log_file:
            log_file.write(f"{local_timestamp} / {utc_timestamp} - Timeout: App is down\n")
    except Exception as e:
        local_timestamp = get_local_time()
        utc_timestamp = get_utc_time()
        with open('app_status_log.txt', 'a') as log_file:
            log_file.write(f"{local_timestamp} / {utc_timestamp} - Error connecting to the app: {e}\n")

if __name__ == "__main__":
    # Run the check every minute
    while True:
        check_app_status()
        time.sleep(60)  # Sleep for 60 seconds before checking again