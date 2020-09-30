# Crosslingual Transfer Learning for Grammatical Error Correction
To clone this repository together with the required `facebookresearch/XLM` and `fastBPE`:
```
git clone https://github.com/facebookresearch/XLM.git
```
```
git clone https://github.com/glample/fastBPE
cd fastBPE
g++ -std=c++11 -pthread -O3 fastBPE/main.cc -IfastBPE -o fast
```
## Download our models and bpe codes
Please download our models from below and put it in the `models` directory.
- [Russian GEC models](https://drive.google.com/file/d/1BGhW9nz4W15tEMBuEJtRnggvLiYPhDPP/view?usp=sharing)
- [Czech GEC models](https://drive.google.com/file/d/19cW5gey5xvX36gsvWpxbPZZU5PizEH-w/view?usp=sharing)
- [English GEC models](https://drive.google.com/file/d/1DdKlxV7xKGYH-9zELfdj-bHsft8ePLh2/view?usp=sharing)

Please download our bpe codes from [here](https://drive.google.com/file/d/1pNJd2n0qKeLwcD5d8OfCUWuGeahQr8HM/view?usp=sharing).

## Using the GEC model
### Preprocess
Use `preprocess.sh` to preprocess the file you want to correct errors as shown below.
```
preprocess.sh [Input_file] [Language] [bpe_code] [fastBPE_dir]
```
You can choose either En, Cs or Ru as the language.  
If you choose something other than En, get the json file for the language you need from [WordFrequency project](https://github.com/hermitdave/FrequencyWords) and save it in the `dic` directory as [Language].json.

### Correction
Use `facebookresearch/XLM/translate.py` to perform the correction. 
```
cat [input_file] | CUDA_VISIBLE_DEVICES=0 python translate.py --model_path [model_path] --output_path [output_path] --src_lang src --tgt_lang trg --batch_size 32
```
