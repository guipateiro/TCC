$nomes = @(5)
#tamanho da camada do meio
foreach ($i in $nomes) {
    python gera_entrada2.py $i
    python gera_entrada3.py $i
    # Loop para executar o programa 20 vezes
    for ($j = 1; $j -le 20; $j++) {

        # Inicie o programa com os argumentos
        python ./testemlp.py $i
    }
}