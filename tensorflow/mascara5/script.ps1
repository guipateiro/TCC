# Loop para executar o programa 20 vezes
for ($i = 12; $i -le 18; $i++) {
    for ($j = 1; $j -le 20; $j++) {

        # Inicie o programa com os argumentos
        python ./testemlp.py $i
    }
}