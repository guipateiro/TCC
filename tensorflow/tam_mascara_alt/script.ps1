for ($i = 14; $i -le 20; $i++) {
    python gera_entrada2.py $i
    python gera_entrada3.py $i
    for ($j = 1; $j -le 20; $j++) {

        # Inicie o programa com os argumentos
        python ./testemlp.py $i
    }
}
