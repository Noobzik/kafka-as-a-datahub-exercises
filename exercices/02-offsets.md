# Gestion d'offsets avec le consumer

## Contexte

On reprend le même contexte que `01-consumer-producer.md`.

## But

On souhaite avoir plus de contrôle sur les offsets commités par le consumer.

En effet, le consumer commite automatiquement son offset toutes 
les 5 secondes.

Nous allons donc le désactiver: en Java, mettre la property `enable.auto.commit` à false.

### Part 1

Ne touchez à rien et lancer votre code plusieurs fois, que se passe-t-il ?

### Part 2

Committez l'offset après chaque consommation de message, et retentez la 
consommation plusieurs fois, que se passe-t-il ?

### Part 3

Donnez maintenant un `group_id` à votre consommateur, et retentez encore une 
fois l'opération. Que se passe-t-il ?

### Part 4

Conservez ce nom, et trouvez un moyen de revenir au début des partitions :).

## Informations

 * Broker Kafka: `127.0.0.1:9092`