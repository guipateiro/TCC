# Loop para executar o programa 20 vezes
for ($i = 1; $i -le 18; $i++) {
    if ($i -eq 1 -or $i -eq 5 -or $i -eq 10 -or $i -eq 15 -or $i -eq 18) {
        for ($j = 1; $j -le 20; $j++) {

            # Inicie o programa com os argumentos
            python ./testemlp2.py $i
        }
    }  
}     