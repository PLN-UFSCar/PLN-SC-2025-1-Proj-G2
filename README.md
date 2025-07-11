# Comandos

## Testar o modelo treinado (Moses)

### 1. Preparar o ambiente

```bash
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

### 2. Permitir a execução do binário do Moses

```bash
chmod +x ./mosesdecoder_bin/moses
```

### 3. Testar modelo sem um arquivo específico

```bash
./mosesdecoder_bin/moses -f moses_working/model/moses.ini
```

### 4. Testar modelo com um arquivo específico e gerar arquivo de saída

```bash
./mosesdecoder_bin/moses -f ./moses_working/model/moses.ini < ./corpus/corpus10k.clean.en > ./corpus/corpus10k_test.output.pt
```

---

## Aplicar a métrica BLEU

O próprio Moses já possui um script para realizar o cálculo da métrica BLEU:

```bash
perl ./BLEU/multi-bleu.perl ./corpus/corpus10k.clean.pt < ./corpus/corpus10k.output.pt
```

---

## Executar o experimento com modelo pré-treinado e fine-tuning (OPUS-MT)

Para treinar e avaliar os modelos **pré-treinado** e **ajustado por fine-tuning** com base no `opus-mt-en-mul`, utilize o notebook:

**`Translation_PyTorch.ipynb`**

Este notebook realiza:
- download dos dados via Kaggle,
- login no Hugging Face Hub,
- treinamento e avaliação do modelo,
- e cálculo das métricas **BLEU**, **TER** e **avaliação qualitativa** das traduções.

### Requisitos:

1. **Token da API do Kaggle**  
   - Baixe o arquivo `kaggle.json` com suas credenciais e salve conforme instruções do notebook.

2. **Token de acesso do Hugging Face**  
   - Necessário para carregar modelos como `opus-mt-en-mul` e salvar checkpoints no Hugging Face Hub.

---

## Estrutura esperada de arquivos

```
.
├── mosesdecoder_bin/
│   └── moses
├── moses_working/
│   └── model/
│       └── moses.ini
├── corpus/
│   ├── corpus10k.clean.en
│   ├── corpus10k.clean.pt
│   ├── corpus10k.output.pt
│   └── corpus10k_test.output.pt
├── BLEU/
│   └── multi-bleu.perl
├── Translation_PyTorch.ipynb
└── README.md
```

---
