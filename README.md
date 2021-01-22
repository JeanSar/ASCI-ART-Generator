# ASCI-ART-Generator

Un petit generateur d'image en ASCII ART qui affiche aléatoirement une image provenant de la base de donnée disponible ici : http://www.ascii-art.de/ 

Vous pouvez générer une image en executant .ASCII.py avec la commande suivant (Ubuntu) dans le repertoire : 

python .ASCII.py

Vous pouvez également générer une nouvelle image a chaque ouverture de Terminale (sous Ubuntu) en ajoutant a la fin du fichier ~/.bashrc : 

if [ -f ~/ASCII-ART-Generator/.ASCII.py ]; then
    python ~/ASCII-ART-Generator/.ASCII.py
fi
