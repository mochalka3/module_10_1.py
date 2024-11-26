import time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


if __name__ == "__main__":
    start_time = time.time()

    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')

    end_time = time.time()
    print(f'Работа функций заняла: {end_time - start_time:.6f} секунд')

    threads = []

    for count, name in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
        thread = Thread(target=write_words, args=(count, name))
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()  # Ожидаем завершения всех потоков

    end_threads_time = time.time()
    print(f'Работа потоков заняла: {end_threads_time - end_time:.6f} секунд')
