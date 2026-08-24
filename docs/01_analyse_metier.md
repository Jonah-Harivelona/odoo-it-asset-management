# Analyse métier — IT Asset & Maintenance Management

## 1. Contexte

L'entreprise dispose d'un parc informatique composé notamment d'ordinateurs, téléphones, écrans, imprimantes, serveurs et autres équipements.

La gestion du parc est actuellement dispersée entre différents outils et méthodes, ce qui rend le suivi des équipements, des affectations, des incidents et des maintenances difficile.

Le projet vise à étudier puis mettre en place une solution centralisée avec **Odoo 19 Community**.

---

## 2. Problématique

L'entreprise doit pouvoir connaître à tout moment :

* les équipements qu'elle possède ;
* leur état et leur localisation ;
* leur utilisateur actuel ;
* leur historique d'affectation ;
* leurs informations de garantie ;
* les incidents et interventions associés ;
* les maintenances prévues.

### Problématique principale

> **Comment centraliser et fiabiliser la gestion du parc informatique et de sa maintenance afin d'assurer un suivi complet du cycle de vie des équipements et des interventions IT ?**

---

## 3. Objectifs

Le projet doit permettre de :

* centraliser les informations des équipements ;
* suivre leur cycle de vie ;
* gérer les affectations permanentes et les prêts temporaires ;
* suivre les garanties ;
* gérer les demandes et incidents IT ;
* suivre les interventions internes et externes ;
* planifier les maintenances préventives ;
* réaliser des inventaires physiques ;
* suivre les pièces et consommables utilisés ;
* définir des priorités et délais de traitement ;
* fournir des indicateurs de pilotage ;
* assurer la sécurité et la traçabilité des opérations.

---

## 4. Acteurs

| Acteur                  | Rôle                                             |
| ----------------------- | ------------------------------------------------ |
| **Employé**             | Utilise les équipements et signale les problèmes |
| **Technicien IT**       | Traite les demandes et réalise les interventions |
| **Responsable IT**      | Supervise le parc et l'activité IT               |
| **Prestataire / SAV**   | Réalise certaines interventions externes         |
| **Administrateur Odoo** | Administre la solution                           |

---

## 5. Besoins métier principaux

### Gestion du parc

* Enregistrer et identifier les équipements.
* Suivre leur état, localisation et cycle de vie.
* Gérer les garanties.
* Gérer les affectations et prêts temporaires.
* Conserver l'historique.

### Support et maintenance

* Créer et suivre les demandes IT.
* Affecter les demandes aux techniciens.
* Enregistrer les interventions.
* Gérer les interventions externes / SAV.
* Planifier les maintenances préventives.
* Suivre les priorités et délais de traitement.

### Inventaire et pilotage

* Réaliser des inventaires physiques.
* Utiliser des codes-barres ou QR codes lorsque nécessaire.
* Suivre les pièces et consommables.
* Produire des indicateurs et rapports.

### Sécurité

* Adapter les droits d'accès selon les rôles.
* Assurer la traçabilité des opérations.

---

## 6. Processus métier cible

### Cycle de vie d'un équipement

```text
Acquisition
    ↓
Réception
    ↓
Enregistrement
    ↓
Stock
    ↓
Affectation / Prêt
    ↓
Utilisation
    ↓
Maintenance / Incident
    ↓
Réparation interne / externe
    ↓
Retour en service
    ↓
Réaffectation
    ↓
Déclassement / Mise au rebut
```

### Traitement d'un incident

```text
Employé
    ↓
Demande IT
    ↓
Priorisation
    ↓
Affectation
    ↓
Diagnostic
    ↓
Intervention
    ↓
Résolution
    ↓
Clôture
```

---

## 7. Périmètre

### Inclus

* Gestion des équipements
* Affectations et prêts
* Garanties
* Incidents et demandes IT
* Interventions
* Maintenance
* Inventaire
* Notifications
* Sécurité
* Reporting
* Portail utilisateur
* Dashboard

### Hors périmètre initial

* Comptabilité complète
* Gestion RH complète
* Gestion avancée des contrats fournisseurs
* Gestion financière complète des actifs
* Gestion avancée des licences logicielles

---

## 8. Critères de réussite

La solution devra permettre au responsable IT de répondre rapidement à des questions telles que :

* Quels équipements possède l'entreprise ?
* Qui utilise chaque équipement ?
* Où se trouve-t-il ?
* Quel est son état et son historique ?
* Sa garantie est-elle valide ?
* Quelles demandes sont ouvertes ?
* Quelles interventions sont en cours ?
* Quelles maintenances sont prévues ?
* Quel est l'état global du parc ?

---

## 9. Approche du projet

Avant tout développement spécifique, chaque besoin sera analysé afin de déterminer s'il peut être couvert par :

1. une **fonctionnalité native Odoo** ;
2. une **configuration Odoo** ;
3. une **adaptation légère** ;
4. ou un **développement spécifique**.

L'objectif est de privilégier le standard Odoo et de développer uniquement lorsque cela est réellement nécessaire.

---


