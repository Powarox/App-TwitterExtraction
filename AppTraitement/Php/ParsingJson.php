<?php

class ParsingJson{
    protected $jsonFile;
    protected $jsonArray;
    protected $bidenTweetArray;
    protected $trumpTweetArray;

    public function __construct($file){
        $this->jsonFile = $file;
        $this->jsonArray = array();
        $this->bidenTweetArray = array();
        $this->trumpTweetArray = array();
    }


// ------------------ Traitement File Entrée ------------------

    // Récupère le json et le transforme en tableau
    public function getJsonToArray(){
        $jsonString = file_get_contents($this->jsonFile);
        $this->jsonArray = json_decode($jsonString, true);
        foreach($this->jsonArray as $key => $value){
            $this->jsonArray = $value;
        }
    }


// ------------------ Séparation Trump / Biden ------------------

    // Find si tweet talk about T or B
    public function findTrumpOrBiden(){
        $patternBiden = "/@?(joe)?(\s)?biden | @?biden(\s)?(joe)?/i";
        $patternTrump = "/@?(donald)?(\s)?trump | @?trump(\s)?(donald)?/i";

        foreach($this->jsonArray as $key => $value){
            if(preg_match($patternBiden, $value['text'])){
                $this->bidenTweetArray[$key] = $value;
            }
            if(preg_match($patternTrump, $value['text'])){
                $this->trumpTweetArray[$key] = $value;
            }
        }
    }

    // Return array with Trump message
    public function getTrumpArray(){
        return $this->trumpTweetArray;
    }

    // Return array with Biden message
    public function getBidenArray(){
        return $this->bidenTweetArray;
    }


// ------------------ Traitement File Sortie ------------------


    // Fichier json contenant les résultat
    public function createResultFile($name, $data){
        $jsonFile = fopen('Result/' . $name . '.json', 'w');
        $dataJson = json_encode($data);

        fputs($jsonFile, $dataJson);
        fclose($jsonFile);
    }

    // Transform file json pour la rendre correct
    public function encodeJsonFile(){
        //{"jsonArray":[,,,,,]}
    }

    // Récupération de chaque json independament
    public function jsonIndepElem(){

    }


// ------------------ Extraction Mots Important ------------------

    // Preparation pattern
    public function regexpBanWord($result = array(), $i = 0){
        $array = $this->arrayBanWord();
        $j = 0;
        foreach($array as $value){
            $result[$i] = "/\s" . $value . "\s/i";
            $i++;
            $j = $i;
        }
        $result[$j] = "/rt\s/i";
        return $result;
    }

    // Extract important word
    public function extractionImportantWord($banWord, $array){
        $arrayWithoutBanWord = array();
        $pattern = "/(@|&|'|\"|\||\(|\)|<|>|#|\.|\,|\/|\?|\!|\;|\:|\\\)/";

        foreach($array as $key => $value){
            $transition = preg_replace($pattern, " ", $value['text']);
            $arrayWithoutBanWord[$key] = preg_replace($banWord, " ", $transition);
        }
        return $arrayWithoutBanWord;
    }

    // Array Ban Word
    public function arrayBanWord(){
        $banWord = array(
            "but", "or", "and", "therefore", "or", "neither", "because",
            "I", "he", "him", "they", "she", "they", "we", "you",
            "your", "your", "my", "mine", "mine", "yours", "yours",
            "all", "yes", "no",
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n "," o "," p "," q ",
            "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "the", "the", "the", "our",
            "then", "to", "none", "also", "other", "before", "with", "have", "good", "because", "this",
            "that", "these", "those", "each", "this", "like", "how", "in", "of", "of",
            "out", "from", "two", "should", "must", "therefore", "back", "right", "start", "she",
            "they", "in", "still", "test", "is", "and", "had", "done", "times", "do",
            "force", "up", "off", "here", "he", "they", "I just", "the", "the", "the", "their", "there",
            "my", "now", "but", "mine", "minus", "word", "same", "neither", "named",
            "our", "we", "new", "or", "where", "by", "because", "word", "not", "people",
            "may", "little", "part", "most", "for", "why", "when", "what", "which", "which",
            "which", "which", "which", "his", "without", "his", "only", "if", "his", "his",
            "are", "under", "be subject", "on", "your", "while", "so", "such", "your", "your",
            "all", "all", "too much", "very", "you", "value", "way", "see", "go",
            "seen", "that", "were", "state", "were", "been", "be",
            "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "with", "at", "by", "in", "of", "in", "of", "a", "your", "best", "between",
            "entered", "from", "then", "not", "not", "from", "same",
            "or", "name", "only", "accepted", "having",
            "your", "your", "my", "mine", "mine", "yours",
            "that", "what", "who", "how", "little", "can", "worse", "then", "not",
            "each", "each", "each",
            "his", "his", "au", "aux", "se", "sur", "those", "this", "that",
            "also", "for", "small", "large", "medium", "large", "top", "bottom", "middle", "right",
            "left", "center", "said", "be", "their", "more", "less", "less",
            "es", "is", "are", "his", "will", "am", "have", "come",
            "http", "https", "", " "
        );
        return $banWord;
    }


// ------------------ Count Occurence Word ------------------

    public function traitementWord($array){
        $lowerArray = strtolower($array);   // $upperArray = strtoupper($array);

        $arrayWord = explode(" ", $lowerArray);

        return $arrayWord;
    }

    public function countOccurenceWord($array){
        $arrayCountOccurence = array();

        foreach($array as $key => $value){
            $arrayWord = $this->traitementWord($value);

            foreach($arrayWord as $word){
                if(key_exists($word, $arrayCountOccurence)){
                    $arrayCountOccurence[$word]++;
                }
                else{
                    $arrayCountOccurence[$word] = 1;
                }
            }
        }

        return $arrayCountOccurence;
    }

    public function getCountArray(){
        return $this->countArray();
    }


// ------------------ Count Occurence Word ------------------

    public function arraySorted($array){
        arsort($array);
        return $array;
    }



// ------------------ Count Occurence Word ------------------

    public function getFirstElemsArray($array, $stopValue){
        $arrayFirstElem = array();
        $stop = 0;
        foreach($array as $key => $value){
            $arrayFirstElem[$key] = $value;
            $stop++;
            if($stop == $stopValue){
                break;
            }
        }
        return $arrayFirstElem;
    }



// ------------------ Autre ------------------

    // Suppression des prépositions et des mots pas important
    public function traitementRegExp(){
        // TF-IDF ?
        foreach($array as $key => $value){
            preg_match();
        }
    }

}
