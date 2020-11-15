<?php

class View{
    protected $title;
    protected $content;

    public function __construct(){
        $this->title = "";
        $this->legend = "";
        $this->content = "";
    }

    // Méthode qui affiche le squelette html
    public function render($template){
        include($template);
    }

    // Méthode pour Page d'Acceuil
    public function makeHomePage($trumpJsonArray, $bidenJsonArray){
        $this->title = "American Election 2020";

        $this->legend = "<h2>US election statistics on twitter 2020</h2>";

        $this->content = '<section class="trump">';
            $this->content .= '<article>';
                $this->content .= '<ul>';
                foreach($trumpJsonArray as $key => $value){
                    $this->content .= '<li>'. $key . ' : ' . $value . '</li>';
                }
                $this->content .= '<ul>';
            $this->content .= '</article>';

            $this->content .= '<article class="zoom">';
                $this->content .= '<img src="../AppTraitement/Result/Trump/ClassicTagCloud.png" alt="Img : ClassicTagCloud">';
            $this->content .= '</article>';

            $this->content .= '<article class="zoom">';
                $this->content .= '<img src="../AppTraitement/Result/Trump/UsFlagTagCloud.png" alt="Img : UsFLagTagCloud">';
            $this->content .= '</article>';

            $this->content .= '<article class="zoom">';
                $this->content .= '<img src="../AppTraitement/Result/Trump/GraphStatHorizontal.png" alt="Img : GraphStatHorizontal">';
            $this->content .= '</article>';

            $this->content .= '<article class="zoom">';
                $this->content .= '<img src="../AppTraitement/Result/Trump/Caricature1.png" alt="Img : Caricature1">';
            $this->content .= '</article>';

            $this->content .= '<article class="zoom">';
                $this->content .= '<img src="../AppTraitement/Result/Trump/Caricature2.png" alt="Img : Caricature2">';
            $this->content .= '</article>';
        $this->content .= '</section>';


        $this->content .= '<section class="biden">';
            $this->content .= '<article>';
                $this->content .= '<ul>';
                foreach($bidenJsonArray as $key => $value){
                    $this->content .= '<li>'. $key . ' : ' . $value . '</li>';
                }
                $this->content .= '<ul>';
            $this->content .= '</article>';

            $this->content .= '<article class="zoom">';
                $this->content .= '<img src="../AppTraitement/Result/Biden/ClassicTagCloud.png" alt="Img : ClassicTagCloud">';
            $this->content .= '</article>';

            $this->content .= '<article class="zoom">';
                $this->content .= '<img src="../AppTraitement/Result/Biden/UsFlagTagCloud.png" alt="Img : UsFLagTagCloud">';
            $this->content .= '</article>';

            $this->content .= '<article class="zoom">';
                $this->content .= '<img src="../AppTraitement/Result/Biden/GraphStatHorizontal.png" alt="Img : GraphStatHorizontal">';
            $this->content .= '</article>';

            $this->content .= '<article class="zoom">';
                $this->content .= '<img src="../AppTraitement/Result/Biden/Caricature1.png" alt="Img : Caricature1">';
            $this->content .= '</article>';

            $this->content .= '<article class="zoom">';
                $this->content .= '<img src="../AppTraitement/Result/Biden/Caricature2.png" alt="Img : Caricature2">';
            $this->content .= '</article>';
        $this->content .= '</section>';
    }
}
