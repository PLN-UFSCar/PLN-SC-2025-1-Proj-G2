# Comandos

## Testar o modelo treinado

1. Preparar o ambiente
	``` 
	sudo apt update
   sudo apt install -y \
   build-essential \
   git \
   cmake \
   libboost-all-dev \
   libbz2-dev \
   zlib1g-dev \
   liblzma-dev \
   libxml2-dev \
   libssl-dev \
   python3-dev \
   wget \
   unzip \
   curl \
   gawk \
   default-jre \
   perl \
   pkg-config
	```

2. Permitir a execução do  ./mosesdecoder_bin/moses
	```
	chmod +x ./mosesdecoder_bin/moses
	```
3. Testar modelo sem um arquivo específico

	``` 
	./mosesdecoder_bin/moses -f moses_working/model/moses.ini
	```
	
4. Testar modelo com um arquivo específico e gerando um arquivo de saída

	``` 
	./mosesdecoder_bin/moses -f ./moses_working/model/moses.ini < ./corpus/corpus10k.clean.en > ./corpus/corpus10k_test.output.pt
	```

## Aplicar a métrica BLEU

O próprio Moses já possui um script para realizar o cálculo da métrica BLEU.
```
perl ./BLEU/multi-bleu.perl ./corpus/corpus10k.clean.pt < ./corpus/corpus10k.output.pt
```

