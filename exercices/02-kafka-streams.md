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

## But

### Découverte

Réimplémenter ce que vous avez fait en `01-consumer-producer.md`, partie 1, en Kafka Streams :).

Documentation Kafka Streams 
  * https://docs.confluent.io/current/streams/developer-guide/dsl-api.html

Tâches:

  * Calculer la nombre de visites moyen par URL en temps réel :
    * sur 30 secondes ;
    * sur 1 minute ;
    * sur 5 minutes.

_Attention: les messages arrivant dans les topics `visits` et `metrics` sont partitionnés par `id`, ce qui
compliquera votre tâche. Pensez à repartitionner les messages vers un topic intermédiaire avec la bonne clé :)._

### Opérations avancées

  * Grouper par catégorie (seconde partie des URLs en `/store` ) et compter le nombre de visites par catégorie.
  * Joindre les deux topics `visits` et `metrics` pour produire des évènements contenant les informations des deux topics
    * Ecrire le résultat dans le topic `votre_nom-augmented-metrics`
  * Calculer la latence moyenne par URL depuis le topic précédent, `votre_nom-augmented-metrics`.

### Interactive Queries

Rendre disponible à l'instant T chacune de vos KTables sur une API REST (sous forme JSON).

Tips: 
  * https://blog.codecentric.de/en/2017/03/interactive-queries-in-apache-kafka-streams/
  * https://docs.confluent.io/current/streams/developer-guide/interactive-queries.html#streams-developer-guide-interactive-queries

## Informations

 * Broker Kafka: `127.0.0.1:9092`