import argparse
import os
import shutil


def parse_arguments():
    parser = argparse.ArgumentParser(description='Recursively copy and sort files based on extension.')
    parser.add_argument('source_dir', type=str, help='Path to the source directory')
    parser.add_argument('destination_dir', type=str, nargs='?', default='dist',
                        help='Path to the destination directory (default: dist)')
    return parser.parse_args()


def recursive_copy(source_dir, destination_dir):
    try:
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        for item in os.listdir(source_dir):
            source_item_path = os.path.join(source_dir, item)

            if os.path.isdir(source_item_path):
                recursive_copy(source_item_path, destination_dir)
            elif os.path.isfile(source_item_path):
                file_extension = os.path.splitext(item)[1][1:]
                target_dir = os.path.join(destination_dir, file_extension if file_extension else 'no_extension')
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)

                shutil.copy2(source_item_path, target_dir)
    except Exception as e:
        print(f"Error processing {source_dir}: {e}")


if __name__ == "__main__":
    args = parse_arguments()
    recursive_copy(args.source_dir, args.destination_dir)
