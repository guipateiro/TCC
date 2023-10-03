$nomes = @(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
#tamanho da camada do meio
foreach ($i in $nomes) {
    # Loop para executar o programa 20 vezes
    python gera_entrada2.py $i
    python gera_entrada3.py $i
    for ($j = 1; $j -le 20; $j++) {

        # Inicie o programa com os argumentos
        python ./testemlp.py $i
    }
}