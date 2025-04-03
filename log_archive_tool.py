import os
import argparse
import tarfile
from datetime import datetime
import logging


def setup_logging():
    logging.basicConfig(
        filename="log_archive.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
    )


def compress_logs(log_directory, output_directory):
    if not os.path.isdir(log_directory):
        print(f"Error: The provided directory {log_directory} does not exist.")
        logging.error(f"Attempted to archive non-existing directory: {log_directory}")
        return

    # Create a timestamp for the archive file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"logs_archive_{timestamp}.tar.gz"
    archive_path = os.path.join(output_directory, archive_name)

    # Check if output directory exists, create if it doesn't
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    try:
        with tarfile.open(archive_path, "w:gz") as archive:
            for root, dirs, files in os.walk(log_directory):
                for file in files:
                    full_path = os.path.join(root, file)
                    archive.add(full_path, arcname=os.path.relpath(full_path, log_directory))

        logging.info(f"Successfully archived logs from {log_directory} to {archive_path}")
        print(f"Logs have been archived to {archive_path}")
    except Exception as e:
        logging.error(f"Error compressing logs: {str(e)}")
        print(f"Error: {str(e)}")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Compress log files into a tar.gz archive.")
    parser.add_argument("log_directory", help="The directory containing the log files.")
    parser.add_argument("output_directory", help="The directory where the archive will be stored.")
    return parser.parse_args()


def main():
    setup_logging()
    args = parse_arguments()

    # Compress the logs
    compress_logs(args.log_directory, args.output_directory)


if __name__ == "__main__":
    main()
