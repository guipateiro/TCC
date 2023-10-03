# Loop para executar o programa 20 vezes
python gera_entrada2.py
python gera_entrada3.py
for ($i = 1; $i -le 18; $i++) {
    for ($j = 1; $j -le 20; $j++) {

        # Inicie o programa com os argumentos
        python ./testemlp.py $i
    }
}