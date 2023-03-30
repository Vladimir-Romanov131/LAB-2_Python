import os
import argparse
import random
from pydub import AudioSegment, effects

def main():
    # парсинг аргументов командной строки
    parser = argparse.ArgumentParser(description='Create a track mix from short fragments of mp3 files')
    parser.add_argument('--source', '-s', required=True, help='source directory with mp3 files')
    parser.add_argument('--destination', '-d', help='destination file name (default: mix.mp3)')
    parser.add_argument('--count', '-c', type=int, help='number of fragments in the mix (default: all)')
    parser.add_argument('--frame', '-f', type=int, help='duration of each fragment in seconds (default: 10)')
    parser.add_argument('--log', '-l', action='store_true', help='print log messages')
    parser.add_argument('--extended', '-e', action='store_true', help='apply fade in/fade out effect to each fragment')
    args = parser.parse_args()

    # получение списка mp3-файлов в директории
    file_list = [f for f in os.listdir(args.source) if os.path.isfile(os.path.join(args.source, f)) and f.endswith('.mp3')]

    # случайный порядок файлов
    random.shuffle(file_list)

    # ограничение числа файлов для использования
    if args.count:
        file_list = file_list[:args.count]

    # определение длительности фрагментов
    if args.frame:
        frame_duration = args.frame * 1000
    else:
        frame_duration = 10000

    # создание объектов AudioSegment для каждого mp3-файла
    audio_list = [AudioSegment.from_file(os.path.join(args.source, f), format='mp3') for f in file_list]

    # обрезание каждого аудиофайла до длительности фрагментов
    audio_list = [audio[:frame_duration] for audio in audio_list]

    # добавление fade in/fade out эффекта, если указан ключ -e
    if args.extended:
        audio_list = [audio.fade_in(500).fade_out(500) for audio in audio_list]

    # склейка всех фрагментов в общий микс
    mix = audio_list[0]
    for audio in audio_list[1:]:
        mix = mix.append(audio, crossfade=500)

    # нормализация громкости микса
    mix = effects.normalize(mix)

    # сохранение микса в файл
    if args.destination:
        mix.export(args.destination, format='mp3')
    else:
        mix.export(os.path.join(args.source, 'mix.mp3'), format='mp3')

    # вывод лога процесса обработки файлов, если указан ключ -l
    if args.log:
        print('--- processing files:')
        for f in file_list:
            print(f'--- {f}')
        print('--- done!')

if __name__ == '__main__':
    main()