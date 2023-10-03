# Loop para executar o programa 20 vezes
$nomes = @(1,5,10,15,18)

foreach ($i in $nomes) {
    python gera_entrada2.py $i
    python gera_entrada3.py $i
    for ($j = 1; $j -le 20; $j++) {

        # Inicie o programa com os argumentos
        python ./testemlp.py $i
    }
}