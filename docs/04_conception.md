# Phase 4 — Conception

## 1. Objectif

Cette phase transforme les décisions de la Phase 3 en une conception fonctionnelle et technique prête pour le développement.

Principes :

* privilégier le standard Odoo ;
* développer uniquement lorsque le standard ne suffit pas ;
* conserver la traçabilité ;
* définir les relations, workflows et droits avant le développement.

---

## 2. Architecture générale

Le projet sera développé sous forme d'un module spécifique :

`it_asset_management`

Principales dépendances :

* `maintenance`
* `stock`
* `hr`
* `contacts`
* `mail`

Le modèle central reste :

`maintenance.equipment`

Les modèles standards Odoo seront réutilisés pour les équipements, la maintenance, les employés, les produits et le stock.

---

## 3. Conception des 16 BM

| BM    | Fonction                    | Conception                                  |
| ----- | --------------------------- | ------------------------------------------- |
| BM-01 | Gestion des équipements     | Extension de `maintenance.equipment`        |
| BM-02 | Identification / inventaire | Numéro de série + identifiant interne       |
| BM-03 | Affectation                 | Détenteur natif + gestion des prêts         |
| BM-04 | Garanties                   | Garantie native + suivi complémentaire      |
| BM-05 | Incidents / demandes IT     | Adaptation de Maintenance + workflow IT     |
| BM-06 | Interventions               | Gestion interne / externe liée aux demandes |
| BM-07 | Maintenance préventive      | Fonctionnalités natives Maintenance         |
| BM-08 | Inventaire physique         | Inventaire spécifique + lignes d'inventaire |
| BM-09 | QR codes                    | Développement spécifique                    |
| BM-10 | SLA / priorités             | Priorité native + SLA spécifique            |
| BM-11 | Pièces / consommables       | Produits et stock Odoo + consommation       |
| BM-12 | Reporting                   | Vues Odoo + indicateurs spécifiques         |
| BM-13 | Sécurité                    | Groupes, droits et règles Odoo              |
| BM-14 | Cycle de vie                | États spécifiques des équipements           |
| BM-15 | Portail IT                  | Portail utilisateur + demandes IT           |
| BM-16 | Documents                   | Chatter + pièces jointes Odoo               |

---

## 4. Modèles spécifiques envisagés

Les modèles spécifiques seront créés uniquement lorsque nécessaire :

```text
it.asset.loan
it.asset.warranty
it.asset.inventory
it.asset.inventory.line
it.asset.sla
```

Les demandes IT et les interventions seront d'abord basées sur les modèles standards Odoo et étendues si nécessaire.

---

## 5. Cycle de vie d'un équipement

```text
Disponible
    ↓
Affecté / Prêté
    ↓
En maintenance
    ↓
En réparation externe
    ↓
Disponible / Affecté
```

Un équipement peut également devenir :

`Déclassé / Mis au rebut`

Les changements d'état doivent rester cohérents avec les opérations réalisées.

---

## 6. Flux principaux

### Support IT

```text
Demande
  ↓
Priorité / SLA
  ↓
Technicien
  ↓
Intervention
  ↓
Résolution
  ↓
Clôture
```

### Prêt

```text
Disponible
  ↓
Prêté
  ↓
Retour
  ↓
Disponible / Affecté
```

### Inventaire

```text
Préparation
  ↓
Contrôle physique
  ↓
Comparaison
  ↓
Écarts
  ↓
Validation
```

### Réparation externe

```text
Incident
  ↓
SAV / Prestataire
  ↓
Réparation externe
  ↓
Retour
  ↓
Remise en service
```

---

## 7. Sécurité

Trois niveaux principaux seront prévus :

* **Utilisateur** : demandes et équipements qui le concernent ;
* **Technicien** : traitement des demandes et interventions ;
* **Responsable IT** : gestion et supervision du parc.

Les droits seront gérés avec les mécanismes standards Odoo :

* groupes ;
* Access Rights ;
* Record Rules.

---

## 8. Structure du module

```text
it_asset_management/
├── models/
├── views/
├── security/
├── data/
├── demo/
├── __init__.py
└── __manifest__.py
```

Les fichiers seront ajoutés progressivement selon les besoins réels du développement.

---

## 9. Ordre de développement

1. **Fondations** — module, dépendances, sécurité, menus
2. **Équipements** — extension, identification, cycle de vie
3. **Affectations / Prêts / Garanties**
4. **Demandes IT / SLA**
5. **Interventions / Pièces**
6. **Inventaire / QR codes**
7. **Reporting / Portail**
8. **Tests / Documentation / Finalisation**

---

## 10. Critère de fin de conception

La Phase 4 est validée lorsque :

* les 16 BM sont couverts ;
* les modèles Odoo à utiliser sont identifiés ;
* les développements spécifiques sont définis ;
* les principaux workflows sont établis ;
* la sécurité et l'ordre de développement sont définis.

Le développement pourra alors commencer avec la **Phase 5 — Développement**.
