# Kafka as a Data Hub

## Plan du cours

  * Pipelines de données et Messaging
    * Impact du Big Data sur les flux de données
    * Le messaging comme dorsale de données
    * Pourquoi Kafka est venu au monde ?
  * Concepts et Architecture de Kafka
    * Kafka-centric architecture
    * "Queue as a Journal"
    * Différences de Kafka avec les systèmes traditionnels
    * Zookeeper, pourquoi ?
  * Consumers/Producers
    * Fonctionnement d'un producer
    * Fonctionnement d'un consumer
  * Réplication, durabilité et impact sur les performances
    * Performance - Disponibilité - Durabilité
        * Acquittement de messages
        * Paramètres autour de la tolérance à la panne
    * Fonctionnement de la réplication sur Kafka (ISR, replicas, leaders/followers)
  * Rétention de données
    * Compression (compact)
    * Nettoyage (clean)
  * Kafka Streams
    * Pourquoi un nouvel arrivant ?
    * Notions basiques
    * Deep Dive sur le Domain Specific Language fourni
      * Aggrégations, filtres, transformations, ...

## Exercices

  * [Utilisation des clients Kafka officiels (Consumer/Producer)](exercices/01-consumer-producer.md)
  * [Kafka Stream](exercices/02-kafka-streams.md)
