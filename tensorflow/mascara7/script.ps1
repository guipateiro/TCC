# Loop para executar o programa 20 vezes
for ($i = 19; $i -le 20; $i++) {
    for ($j = 1; $j -le 20; $j++) {
        python gera_entrada2.py
        python gera_entrada3.py
        # Inicie o programa com os argumentos
        python ./testemlp.py $i
    }
}