import argparse
import configparser
import numpy as np


def parse_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)

    n0 = float(config.get('DEFAULT', 'n0'))
    h = float(config.get('DEFAULT', 'h'))
    nk = float(config.get('DEFAULT', 'nk'))
    a = float(config.get('DEFAULT', 'a'))
    b = float(config.get('DEFAULT', 'b'))
    c = float(config.get('DEFAULT', 'c'))

    return n0, h, nk, a, b, c


def calculate_y(x, a, b, c):
    return a - np.cos(b * x + c) ** 2


def main():
    parser = argparse.ArgumentParser(description='Calculate function values.')
    parser.add_argument('--config', type=str, help='Path to the config file', default='config.json')

    args = parser.parse_args()

    # Считываем параметры из конфигурационного файла
    n0, h, nk, a, b, c = parse_config(args.config)

    # Генерируем значения x
    x_values = np.arange(n0, nk + h, h)

    # Вычисляем значения y
    y_values = calculate_y(x_values, a, b, c)

    # Записываем результаты в файл
    with open('results.txt', 'w') as f:
        for x, y in zip(x_values, y_values):
            f.write(f"{x:.2f}, {y:.2f}\n")


if __name__ == '__main__':
    main()
