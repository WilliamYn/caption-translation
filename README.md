# Caption_translation
Service de traduction (anglais vers francais) de phrases et de mots qui préserve le contexte entre ceux-ci. Ce service a été créé pour être utilisé sur le output de https://github.com/WilliamYn/learning-captioning-model et https://github.com/WilliamYn/pretrained-captioning.

## Description
Ce service est basé sur le module Deep Translator de Python. Il utilise en arrière-plan l’API de Google Traduction en effectuant des manipulations pour conserver le contexte des mots traduits.

Il est important de noter que le module ne fait que traduire les étiquettes, il ne réévalue pas les prédictions avec les mots nouvellement traduits. 

Ce service est présentement le plus lent que le service de captioning dû au fait que toutes les traductions de mots clés sont faites séparément et individuellement, pour minimiser les erreurs qui pourraient survenir lors de la traduction dû à l’encapsulation des mots clés dans les phrases. 

La traduction se base sur une fonctionnalité intéressante de l’outil de traduction de Google qui est de supporter la traduction de texte de page HTML. Cela fait en sorte que la présence de balises quelconques, en quantité raisonnable, ne nuit pas à la traduction de celui-ci. La traduction prend en entrée la liste des mots clés à traduire ainsi que les phrases depuis lesquelles les mots clés ont été générés. Pour conserver le contexte des mots, nous ajoutons des marqueurs pour identifier le mot traduit lors de la traduction des phrases contenant le mot. Ces marqueurs sont sous la forme de balises <span> et sont placés avant et après le mot à traduire dans les phrases de façon à encadrer le mot. Ensuite, les phrases sont traduites, et tous les mots se trouvant entre les balises sont récupérés et sont sauvegardés dans une liste qui correspond aux traductions contextuelles du mot choisi. Ces traductions peuvent être des mots composés, tout comme elles peuvent être multiples si le mot à traduire est présent dans plusieurs phrases et possède différentes significations. Dans ce dernier cas, la liste de traduction comportera plusieurs éléments. Il n’y a pas de signification particulière à l’ordre de la liste de traduction.

Ce processus est répété pour chaque mot de la liste de mot clés, ce qui constitue la raison principale de la lenteur de l’algorithme.

La traduction de l’ensemble des mots clés en une passe, avec l’ensemble des mots délimités a été essayé sans grand succès. Le problème majeur avec cette approche est que la présence d’un trop grand nombre de balises nuit grandement à la conservation du contexte lors de la traduction des phrases. Plus le nombre de balises est grand, plus la traduction devient graduellement “mot à mot”, c’est-à-dire que la phrase traduite n’est plus cohérente tant en contexte qu’en syntaxe. Un exemple clair de cela est lorsqu’on traduit la phrase suivante : “he leaves to work”. Un trop grand nombre de balises nous donnait la traduction suivante: “il feuille pour travail”. De plus, la traduction du français vers l’anglais amène parfois certains mots à changer de position, disparaitre ou apparaitre. Lorsqu’il y a plusieurs balises, elles tendent à ne pas suivre proprement les mots qu’elles encadrent dans ces cas-ci.

## Déploiement
Il y a une image Docker disponnible sur Docker Hub sous le nom de wayr/translation_flask_app
https://hub.docker.com/r/wayr/translation_flask_app

## Utilisation
Le Docker déploie une application Flask sur la route 80 du conteneur. Il n'y a qu'une seule route rendue disponnible par ce service, qui est la route par défault ("/"). Pour effectuer la traduction, on envoie une requête post avec un JSON des éléments à traduire à cette route.

### Input JSON
  ```
{
    "tags": [
        ["tag1", 0.38],
        ["tag2", 0.12],
        ...,
        ["tagX", 0.01]
    ],
    "english_captions": [
        "The sentence the tags were generated from.",
        ...,
        "Another sentence the tags were generated from."
    ]
}
```
### Output JSON
 ```
{
    "tags": [
        ["tag1", 0.38, ["traduction1"]],
        ["tag2", 0.12, ["traduction2"]],
        ...,
        ["tagX", 0.01, ["traductionX1", "traductionX2", ...]]
    ],
    "english_captions": [
        ("The sentence the tags were generated from.","La phrase à partir de laquelle les balises ont été générées.")
        ...,
        ("Another sentence the tags were generated from.", "Une autre phrase à partir de laquelle les balises ont été générées.")
    ]
}
  ```
