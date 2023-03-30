import os
import argparse
import shutil
import datetime

# функция для получения даты последней модификации файла в формате datetime
def get_file_modification_date(file_path):
    modification_time = os.path.getmtime(file_path)
    return datetime.datetime.fromtimestamp(modification_time)

# функция для создания директории, если её ещё нет
def create_directory_if_not_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# функция для перемещения файлов из одной директории в другую
def move_files(files, dest_dir):
    for file_path in files:
        shutil.move(file_path, dest_dir)

# парсинг аргументов командной строки
parser = argparse.ArgumentParser(description='Reorganize files in source directory based on their modification date and size')
parser.add_argument('--source', type=str, help='Source directory path', required=True)
parser.add_argument('--days', type=int, help='Number of days before today to consider files as old', required=True)
parser.add_argument('--size', type=int, help='Maximum file size in bytes to consider as small', required=True)
args = parser.parse_args()

# получаем текущую дату и дату, отстоящую от неё на --days дней
today = datetime.datetime.now()
old_day = today - datetime.timedelta(days=args.days)

# создаем директории Archive и Small
archive_dir = os.path.join(args.source, 'Archive')
small_dir = os.path.join(args.source, 'Small')
create_directory_if_not_exists(archive_dir)
create_directory_if_not_exists(small_dir)

# перебираем все файлы в --source директории
for file_name in os.listdir(args.source):
    file_path = os.path.join(args.source, file_name)

    # проверяем, является ли файл старым
    if get_file_modification_date(file_path) < old_day:
        move_files([file_path], archive_dir) # перемещаем файл в директорию Archive

    # проверяем, является ли файл маленьким
    elif os.path.getsize(file_path) < args.size:
        move_files([file_path], small_dir) # перемещаем файл в директорию Small
