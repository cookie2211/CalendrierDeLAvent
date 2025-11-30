<!DOCTYPE html>
<html lang="en">
    <head>
        <meta chartset="UTF-8">
        <meta name="viewport" content="width=device-width, inital-scale=1.0">
        <link rel="stylesheet" media="screen" type="text/css" title="style" href="../static/style.css" \>
        <script> 
        // c'est une ptn de fonction qui renvoie sur la bonne page web en fonction de ce que tu passes en paramètres.
        // A REFAIRE PROP CA SENT L'IA FEIGNASSE !!
            function oriente(page, speciale) {
              cible='/templates/jour_'+page+'.html';
              if (page == speciale && window.matchMedia("(orientation: portrait)").matches) {
                cible='jour_'+page+'_mobile.html';
              }
              window.open(cible, '_self');
              console.log(window.location);
            }
        </script>
        <title>Calendrier de l'avent</title>
    </head>
    <body>
        <h1 class="titre">Mon calendrier de l'avent</h1>
        <?php
            //init un tableau vide
            $tab = [];
            for ($i = 1; $i <25; $i++){
                $tab[$i-1] = $i;
            }
            shuffle($tab); //ça ça mélange le tableau aléatoirement
            
            for ($i = 0; $i < 24; $i++){ //affiche les boutons en fctn de la couleur
                if ($tab[$i] != 24){
                    echo "<button onclick='oriente($tab[$i], 3)' class = 'vert'>$tab[$i] </button>";
                }
                else{
                    echo "<button class = 'vert jaune'>$tab[$i] </button>";
                }
            }
        ?>  
    </body>
</html>
