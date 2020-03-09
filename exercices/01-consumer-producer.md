# Implémentation d'un consumer & d'un producer

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

## Environnement

Vous devez démarrer localement les éléments nécessaire à cet exercice. Clonez ce dépôt Git, placez vous dans le dossier `platform/docker` puis faites la commande suivante:

```bash
docker-compose up -d
```

Ceci va lancer sur votre machine l'ensemble des composants nécessaires, allez ensuite sur http://localhost:9021/ pour savoir l'état de votre cluster Kafka.

Pour l'usage de ce TP, vous vous connectez au broker Kafka suivant : `127.0.0.1:9092`

Vous pouvez partir d'un template selon votre langage de prédilection:

  * Scala
    * https://git.esgi.nyuu.eu/nekonyuu/kafka-as-a-datahub-project-template-scala
    * Akka HTTP, Kafka Streams
  * Java
    * https://git.esgi.nyuu.eu/nekonyuu/kafka-as-a-datahub-project-template-java
    * Kafka Streams, REST framework à votre charge

## Documentation

  * Kafka Client Java API: https://docs.confluent.io/current/clients/java.html#java-client

## Questions

### Application de traitements sur des messages

Calculez le nombre de visites moyen pour chaque url, mis à jour en temps réel :

  * sur les 30 dernières secondes, résultat à envoyer dans le topic `visits_30s` ;
  * sur la dernière minute, résultat à envoyer dans le topic `visits_1mn` ;
  * sur les 5 dernières minutes, résultat à envoyer dans le topic `visits_5mn`.

**Les résultats sont à envoyer à chaque mise à jour dans les topics mentionnés.**

### Production de messages

Vous devez maintenant envoyer les messages que vous produisez avec une clé.

L'idée est que vous puissiez garantir l'écriture des messages concernant la même URL dans la même partition.

Vous pouvez vérifier ceci dans la vue Topics du dashboard de votre cluster (http://localhost:9021 pour rappel).

### Offsets

On souhaite avoir plus de contrôle sur les offsets commités par le consumer.

En effet, le consumer commite automatiquement son offset toutes 
les 5 secondes.

Nous allons donc le désactiver: mettre la property `enable.auto.commit` à false.

  1. Ne touchez à rien et lancez votre code plusieurs fois, que se passe-t-il ?
  2. Committez l'offset après chaque consommation de message, et retentez la consommation plusieurs fois, que se passe-t-il ?
  3. Donnez maintenant un `group_id` à votre consommateur, et retentez encore une fois l'opération. Que se passe-t-il ?
  4. Conservez ce nom, et trouvez un moyen de revenir au début des partitions :).

### Acquittement

Nous voudrions maintenant + de garanties sur l'écriture des messages, de manière à n'en perdre aucun.

Pour tous les appels de production de messages, faites en sorte que
le paramètre d'acquittement soit maintenant `acks=all`, s'assurant de 
l'écriture des messages sur tous les brokers.