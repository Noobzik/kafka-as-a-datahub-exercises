# Utilisation d'un consumer et d'un producer

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

## But

### Part 1

Calculez le nombre de visites moyen pour chaque url, mis à jour en temps réel :

  * sur les 30 dernières secondes, dans le topic `votre-nom_visits_30s` ;
  * sur la dernière minute, dans le topic `votre-nom_visits_1mn` ;
  * sur les 5 dernières minutes, dans le topic `votre-nom_visits_5mn`.

### Part 2

Vous devez maintenant envoyer les messages que vous produisez avec une clé.

L'idée est que vous puissiez garantir l'écriture des messages concernant la même URL dans la même partition.

### Part 3 (bonus)

Nous voudrions maintenant + de garanties sur l'écriture des messages, de manière à n'en perdre aucun.

Pour tous les appels de production de messages, faites en sorte que
le paramètre d'acquittement soit maintenant `acks=all`, s'assurant de 
l'écriture des messages sur tous les brokers.

## Informations

 * Broker Kafka: `127.0.0.1:9092`