$nomes = @("masc_invert", "mascara3","mascara5","mascara5_2","mascara7","mascara7_2","mascara5_esparsa","mascara5_esparsa_bit_meio","perceptron")

foreach ($nome in $nomes){
    cd $nome
    python.exe geragrafico.py
    cd ..
}