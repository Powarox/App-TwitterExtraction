<?php

require_once("ParsingJson.php");


$jsonString = file_get_contents("us_election20_tweet_pr.json");
$jsonArray = json_decode($jsonString, true );;


/*$bidenTweetArray = array();
$trumpTweetArray = array();


$patternBiden = "/@?(joe)?(\s)?biden | @?biden(\s)?(joe)?/i";
$patternTrump = "/@?(donald)?(\s)?trump | @?trump(\s)?(donald)?/i";


foreach($jsonArray as $key => $value){
    foreach($value as $k => $v){
        if(preg_match($patternBiden, $v['text'])){
            $bidenTweetArray[$k] = $v;
        }
        if(preg_match($patternTrump, $v['text'])){
            $trumpTweetArray[$k] = $v;
        }
    }
}


var_dump($bidenTweetArray);
var_dump($trumpTweetArray);*/

$banWord = array(
    "but", "or", "and", "therefore", "or", "neither", "because",
    "I", "he", "him", "they", "she", "they", "we", "you",
    "your", "your", "my", "mine", "mine", "yours", "yours",
    "all", "all", "all",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n "," o "," p "," q ",
    "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "the", "the", "the", "our",
    "then", "to", "none", "also", "other", "before", "with", "have", "good", "because", "this",
    "that", "these", "those", "each", "this", "like", "how", "in", "of", "of", "in",
    "out", "from", "two", "should", "must", "therefore", "back", "right", "start", "she",
    "they", "in", "still", "test", "is", "and", "had", "done", "done", "times", "do",
    "force", "up", "off", "here", "he", "they", "I just", "the", "the", "the", "their", "there",
    "my", "now", "but", "my", "mine", "minus", "my", "word", "same", "neither", "named",
    "our", "we", "new", "or", "where", "by", "because", "word", "not", "people",
    "may", "little", "part", "most", "for", "why", "when", "what", "which", "which",
    "which", "which", "which", "his", "without", "his", "only", "if", "his", "his",
    "are", "under", "be subject", "on", "your", "while", "so", "such", "your", "your",
    "all", "all", "too much", "very", "you", "value", "way", "see", "go", "your", "you",
    "seen", "that", "were", "state", "were", "been", "be",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "with", "at", "by", "in", "of", "in", "of", "a", "your", "best", "between",
    "entered", "from", "then", "not", "not", "from", "same",
    "or", "name", "only", "accepted", "having",
    "your", "your", "my", "mine", "mine", "yours", "yours", "all", "all", "all",
    "that", "what", "who", "how", "little", "can", "worse", "then", "not",
    "each", "each", "each",
    "his", "his", "au", "aux", "se", "sur", "this", "those", "this", "ca", "this", "this", "that ",
    "also", "for", "small", "large", "medium", "large", "top", "bottom", "middle", "right",
    "left", "center", "said", "be", "their", "their", "more", "less", "less",
    "es", "is", "are", "his", "will", "am", "have", "come",
    "http", "/", "."
);


$arrayWithoutBanWord = array();

foreach($jsonArray as $key => $value){
    foreach($value as $k => $v){
        $arrayWithoutBanWord[$k] = str_replace($banWord, "", $v["text"]);
    }
}


var_dump($arrayWithoutBanWord);






//$parsingJson = new ParsingJson();