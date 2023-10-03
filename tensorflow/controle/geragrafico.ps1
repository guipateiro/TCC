$nomes = @("mascara3","mascara5","mascara5_2","mascara7","mascara7_2")

foreach ($nome in $nomes){
    cd $nome
    python.exe geragrafico.py
    cd ..
}