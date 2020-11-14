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
    public function makeHomePage(){
        $this->title = "Accueil";

        $this->legend = "<h2>Statistique of the US election 2020</h2>";

        $this->content = '<section class="trump">';
            $this->content .= '<article>';
                $this->content .= '<p>Trump</p>';
            $this->content .= '</article>';

            $this->content .= '<article>';
                $this->content .= '<p>IMG</p>';
            $this->content .= '</article>';

            $this->content .= '<article>';
                $this->content .= '<p>IMG</p>';
            $this->content .= '</article>';

            $this->content .= '<article>';
                $this->content .= '<p>Text</p>';
            $this->content .= '</article>';
        $this->content .= '</section>';


        $this->content .= '<section class="biden">';
            $this->content .= '<article>';
                $this->content .= '<p>Biden</p>';
            $this->content .= '</article>';

            $this->content .= '<article>';
                $this->content .= '<p>IMG</p>';
            $this->content .= '</article>';

            $this->content .= '<article>';
                $this->content .= '<p>IMG</p>';
            $this->content .= '</article>';

            $this->content .= '<article>';
                $this->content .= '<p>Text</p>';
            $this->content .= '</article>';
        $this->content .= '</section>';
    }

    // public function makeTrumpSection(){
    //     $trump =
    // }
    //
    // public function makeBidenSection(){
    //     $biden =
    // }

}
