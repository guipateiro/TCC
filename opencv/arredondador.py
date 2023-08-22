def round_float_to_int(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file:
            numbers = input_file.readlines()

        rounded_numbers = [round(float(num)) for num in numbers]

        with open(output_filename, 'w') as output_file:
            for rounded_num in rounded_numbers:
                output_file.write(f'{rounded_num:.6f}\n')

        print(f"Números arredondados escritos em '{output_filename}'.")

    except FileNotFoundError:
        print("Arquivo de entrada não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    input_file = "saida_modificado.txt"  # Nome do arquivo de entrada com os floats
    output_file = "saidatratada.txt"  # Nome do arquivo de saída com os floats arredondados
    round_float_to_int(input_file, output_file)