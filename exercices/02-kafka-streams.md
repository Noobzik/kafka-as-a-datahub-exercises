# Kafka Streams

## Contexte

Vous venez d'arriver dans la société MediaSeller, site d'e-commerce vendant de multiples produits
multimedia, des livres, appareils photo, etc.

Vous prenez part à un workshop mis en place par l'équipe pour travailler sur les données
produites par le site web de la société afin de pouvoir en sortir des tendances, ainsi que des 
informations techniques utiles.

Ces évènements de visite sont modélisés comme suit:

```json
{
    "id": "5db37baf-06ed-4a9b-8e69-9b4f34ed959e",
    "sourceIp": "42.42.183.75",
    "url": "/store/tech/tv",
    "timestamp": "2019-03-02T09:21:05.305622Z",
}
```

Ils sont tous envoyés dans un topic kafka nommé `visits`.

Nous allons aussi utiliser un second topic kafka, `metrics`, contenant les informations suivantes :

```json
{
  "id": "5db37baf-06ed-4a9b-8e69-9b4f34ed959e",
  "timestamp": "2019-03-02T12:03:36.495084Z",
  "latency": 553
}
```

L'ID donné dans ce message correspond à l'ID d'event de visite dans le topic `visits`.

## Environnement

Vous allez utiliser un cluster Kafka préalablement déployé.

Les informations le concernant vous seront communiqués par Teams, elles seront à saisir dans le fichier `kafka.properties`.

## Exercices

Clonez le dépôt Git à [cette URL](https://github.com/nekonyuu/kafka-as-a-datahub-exercises-skeletons) et ouvrez le projet sous IntelliJ.

Les fichiers `StreamProcessing.scala` et `WebServer.scala` contiennent l'ensemble du code à manipuler pour ces exercices, 
ponctués de TODOs au fil de ceux-ci.

### 1. Application de traitements sur des messages

Vous devez calculer la nombre de visites par URL :
  * sur les 30 dernières secondes ;
  * sur la dernière minute ;
  * sur les 5 dernières minutes.

Ces calculs doivent être implémentés sur des ["hopping window"](https://docs.confluent.io/platform/current/streams/developer-guide/dsl-api.html#hopping-time-windows)

Pour implémenter cela, allez dans le fichier `StreamProcessing.scala` et commencez ligne 40.

_Attention: les messages arrivant dans les topics `visits` et `metrics` sont partitionnés par `id`, ce qui
compliquera votre tâche. Pensez à repartitionner les messages avec la bonne clé :)._

### 2. Aggrégations avancées

  * Grouper par catégorie (seconde partie des URLs en `/store` ) et compter le nombre de visites par catégorie
    * sur les 30 dernières secondes ;
    * sur la dernière minute ;
    * sur les 5 dernières minutes.
  * Joindre les deux topics `visits` et `metrics` pour produire des évènements contenant les informations des deux topics, puis calculer la latence moyenne par URL en partant de cette jointure.

### 3. Interactive Queries

Rendez disponible le résultat de chacune de vos KTables sur une API REST (sous forme JSON), actualisé au fil de l'eau. 

Pour cela, vous devez :
  * Matérialiser les KTables que vous avez construit dans des stores, dans le fichier `StreamProcessing.scala`
  * requêter ces nouveaux stores dans l'API REST implémentée avec Akka HTTP dans le fichier `WebServer.scala`, suivez les TODO pour l'implémentation.

### Documentations

  * Kafka Streams: https://docs.confluent.io/current/streams/developer-guide/dsl-api.html
  * Interactive queries: https://docs.confluent.io/current/streams/developer-guide/interactive-queries.html#streams-developer-guide-interactive-queries