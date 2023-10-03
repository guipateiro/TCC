$nomes = @(1,15,30,45,60,75,90,109,150)

python gera_entrada2.py
python gera_entrada3.py
#tamanho da camada do meio
foreach ($i in $nomes) {    
    # Loop para executar o programa 20 vezes
    for ($j = 1; $j -le 20; $j++) {
        # Inicie o programa com os argumentos
        python ./testemlp.py $i
    }
}