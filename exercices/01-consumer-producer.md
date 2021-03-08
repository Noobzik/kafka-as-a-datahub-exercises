# Implémentation d'un consumer & d'un producer

## Environnement

Vous allez utiliser un cluster Kafka préalablement déployé.

Les informations le concernant vous seront communiqués par Teams, elles seront à saisir dans le fichier `kafka.properties`.

## Documentation

  * Kafka Client Java API: https://docs.confluent.io/current/clients/java.html#java-client

## Exercices

Clonez le dépôt Git à [cette URL](https://github.com/nekonyuu/kafka-as-a-datahub-exercises-skeletons) et ouvrez le projet sous IntelliJ.

### Production et consommation de messages

Vous allez produire des évènements de connexion au cluster, lesquels contiendront un UUID, votre nom, prénom et un timestamp d'émission de l'évènement.

La case class modélisant l'évènement à envoyer est déclarée comme suit (voir `ConnectionEvent.scala`) :

```scala
case class ConnectionEvent(
                            _id: String,
                            firstName: String,
                            lastName: String,
                            timestamp: OffsetDateTime
                          )
```

Vous devez écrire ces évènements dans un topic nommé `connection-events`, avec comme clé de message "votrePrénom-votreNom". Ensuite, consommez ce même topic pour voir vos messages ainsi que ceux des autres étudiants.

Pour cela, ouvrez le fichier `MessageProcessing.scala` et suivez les TODO :
  * Ligne 24 pour la partie producer ;
  * Ligne 46 pour la partie consumer.

Une fois terminé, faites en sorte que le consumer n'affiche que les messages émis par vous (ceux contenant votre nom et prénom).

### Offsets

On souhaite avoir plus de contrôle sur les offsets commités par le consumer.

En effet, le consumer commite automatiquement son offset toutes 
les 5 secondes.

Nous allons donc le désactiver: dans le fichier `kafka.properties`, ajoutez la property `enable.auto.commit=false`, et commentez la ligne suivante dans la méthode `run()` :

```scala
producerScheduler.schedule(producerLoop, 1, TimeUnit.SECONDS)
```

Maintenant:
  1. Lancez votre code plusieurs fois, que se passe-t-il ?
  2. Committez l'offset après chaque consommation de message, et retentez la consommation plusieurs fois, que se passe-t-il ?
  3. Changez maintenant le contenu de la variable `applicationName` en y ajoutant un nombre, par exemple. Ceci a pour effet de donner un `group_id` différent à votre consommateur. Relancez une nouvelle fois l'application. Que se passe-t-il ?
  4. Conservez ce nom, et trouvez un moyen de revenir au début des partitions :).