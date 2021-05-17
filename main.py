from calculate_pi import *


def main():
    print(f'Iniciando...')
    throw_needles(1000000, create_chart=True)
    #generate_estimates(10000, 50)
    #estimate_pi(0.01, 10000)


if __name__ == '__main__':
    main()
