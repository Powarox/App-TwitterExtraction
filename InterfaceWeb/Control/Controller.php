<?php

require_once('View/View.php');

class Controller{
    protected $view;

    public function __construct($view){
        $this->view = $view;
    }

    public function execute($trump, $biden){
        $trumpJsonArray = $this->getAppTraitementResult($trump);
        $bidenJsonArray = $this->getAppTraitementResult($biden);

        $trumpJsonArray = array_slice($trumpJsonArray, 0, 10);
        $bidenJsonArray = array_slice($bidenJsonArray, 0, 10);
        
        $this->view->makeHomePage($trumpJsonArray, $bidenJsonArray);
    }

    public function getAppTraitementResult($name){
        $jsonString = file_get_contents('../AppTraitement/Result/'.$name.'/AResult.json');
        $jsonArray = json_decode($jsonString, true);
        return $jsonArray;
    }
}
