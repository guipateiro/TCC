#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Uso: $0 <nome_do_arquivo>"
    exit 1
fi

input_file="$1"
output_file="${input_file%.txt}_modificado.txt"

if [ ! -f "$input_file" ]; then
    echo "Arquivo '$input_file' não encontrado."
    exit 1
fi

sed 's/[;[]\|]//g' "$input_file" > "$output_file"
echo "Caracteres '[', ']' e ';' removidos em '$output_file'."