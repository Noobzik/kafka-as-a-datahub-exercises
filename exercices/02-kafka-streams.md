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

Vous devez démarrer localement les éléments nécessaire à cet exercice. Clonez ce dépôt Git, placez vous dans le dossier `platform/docker` puis faites la commande suivante:

```bash
docker-compose up -d
```

Ceci va lancer sur votre machine l'ensemble des composants nécessaires, allez ensuite sur http://localhost:9021/ pour savoir l'état de votre cluster Kafka.

Pour l'usage de ce TP, vous vous connectez au broker Kafka suivant : `127.0.0.1:9092`

## Exercices
### 1. Application de traitements sur des messages

Tâches:
  * Calculer la nombre de visites moyen par URL :
    * sur les 30 dernières secondes ;
    * sur la dernière minute ;
    * sur les 5 dernières minutes.

Ces calculs doivent être implémentés sur des ["hopping window"](https://docs.confluent.io/platform/current/streams/developer-guide/dsl-api.html#hopping-time-windows)

_Attention: les messages arrivant dans les topics `visits` et `metrics` sont partitionnés par `id`, ce qui
compliquera votre tâche. Pensez à repartitionner les messages avec la bonne clé :)._

### 2. Aggrégations avancées

  * Grouper par catégorie (seconde partie des URLs en `/store` ) et compter le nombre de visites par catégorie.
  * Joindre les deux topics `visits` et `metrics` pour produire des évènements contenant les informations des deux topics, puis calculer la latence moyenne par URL en partant de cette jointure.

### 3. Interactive Queries

Rendre disponible à l'instant T chacune de vos KTables sur une API REST (sous forme JSON).

### Documentations

  * Kafka Streams: https://docs.confluent.io/current/streams/developer-guide/dsl-api.html
  * Interactive queries: https://docs.confluent.io/current/streams/developer-guide/interactive-queries.html#streams-developer-guide-interactive-queries