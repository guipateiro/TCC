

all:
	g++ -o mlp testemlp.cpp -I /usr/local/include/opencv4 \
	-L /usr/lib \
	-lopencv_core \
	-lopencv_imgproc \
	-lopencv_ml

fullrun: all
	python3 gera_entrada.py
	./mlp > saida.txt	
	./tratador.sh saida.txt
	python3 arredondador.py
	diff saidatratada.txt output_data.txt

purge: 
	rm -f *.txt
	rm -f *.tre
	rm -f mlp	