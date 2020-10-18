<?php

class ParsingJson{
    protected $fileJson;
/*    protected $trumpArray;
    protected $bidenArray;*/
    
    public function __construct($file){
        $this->fileJson;
    }
    
    // Récupère le json et le transforme en tableau
    public function getJsonToArray(){
        $this->fileJson;
    }
    
    // Return array with Trump message
    public function getTrumpArray(){
        return $trumpArray;
    }
    
    // Return array with Biden message
    public function getBidenArray(){
        return $bidenArray;
    }
    
    // Suppression des prépositions et des mots pas important 
    public function traitementRegExp(){
        // TF-IDF ? 
        foreach($array as $key => $value){
            preg_match();
        }
    }
    
    
    
}