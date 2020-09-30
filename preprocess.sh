INPUT_FILE=$1
LANG=$2
BPE_CODE=$3
python tokenize_sentence.py $INPUT_FILE $INPUT_FILE.tok
if [ $LANG="En" ] ; then
    python spellcheck.py $INPUT_FILE.tok $INPUT_FILE.tok.spellcheck
else 
    echo $LANG
    python spellcheck.py $INPUT_FILE.tok $INPUT_FILE.tok.spellcheck -ld dic/$LANG.json
fi
cd ../fastBPE
./fast applybpe $INPUT_FILE.tok.spellcheck.bpe $INPUT_FILE.tok.spellcheck ../Crosslingual-Transfer-for-GEC/$BPE_CODE