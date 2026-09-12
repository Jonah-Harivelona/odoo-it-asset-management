# Analyse des fonctionnalités Odoo

## Projet

**IT Asset & Maintenance Management**

- **Version :** Odoo 19 Community
- **Objectif :** analyser les fonctionnalités natives d'Odoo avant tout développement spécifique.

---

# 1. Méthode d'analyse

Pour chaque besoin métier, la démarche suivie est :

> **Besoin métier → Vérification du standard Odoo 19 Community → Classification**

Les classifications utilisées sont :

- 🟢 **Natif** : fonctionnalité disponible directement dans Odoo.
- 🔵 **Configuration** : fonctionnalité disponible mais nécessitant principalement un paramétrage.
- 🟠 **Adaptation** : fonctionnalité existante nécessitant une modification ou une adaptation.
- 🔴 **Développement spécifique** : fonctionnalité absente du standard et nécessitant du développement.

---

# 2. Analyse des fonctionnalités

## BM-01 — Gestion des équipements

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Créer et gérer des équipements | `maintenance.equipment` | 🟢 Natif |
| Catégorie d'équipement | Catégories de maintenance | 🟢 Natif |
| Détenteur / utilisateur | Affectation à un employé | 🟢 Natif |
| Équipe de maintenance | Équipe de maintenance | 🟢 Natif |
| Technicien / responsable | Responsable de l'équipement | 🟢 Natif |
| Date d'assignation | Champ de date d'assignation | 🟢 Natif |
| Lieu d'utilisation | Champ de localisation de l'équipement | 🟢 Natif |
| Date de mise au rebut | Champ disponible sur l'équipement | 🟢 Natif |
| Historique via Chatter | Chatter | 🟢 Natif |
| Statuts métier personnalisés | Workflow spécifique | 🔴 Spécifique |

### Conclusion

Odoo fournit nativement le socle nécessaire à la gestion des équipements.
Les statuts métier personnalisés seront traités lors de la conception et du développement.

---

## BM-02 — Identification / inventaire

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Numéro de série | Numéro de série sur l'équipement | 🟢 Natif |
| Traçabilité des produits stockés | Traçabilité Inventory | 🟢 Natif |
| Inventaire physique des produits | Inventaire Inventory | 🟢 Natif |
| Code-barres directement sur équipement | Non disponible sur `maintenance.equipment` dans notre environnement | 🔴 Spécifique |
| Liaison automatique numéro de série Maintenance / Inventory | Non identifiée | 🔴 Spécifique |
| Écarts d'inventaire des équipements | Non disponible nativement pour `maintenance.equipment` | 🔴 Spécifique |
| QR / Barcode → équipement | Non disponible | 🔴 Spécifique |

### Conclusion

Odoo dispose d'un système natif de numéros de série et d'inventaire pour les produits.
Cependant, la gestion d'inventaire spécifique aux équipements Maintenance et leur identification par QR/Barcode nécessiteront du développement spécifique.

---

## BM-03 — Affectation des équipements

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Affecter un équipement à un employé | Détenteur / employé | 🟢 Natif |
| Date d'affectation | Date d'assignation | 🟢 Natif |
| Consulter les équipements d'un employé | Smart button Équipements | 🟢 Natif |
| Réaffecter un équipement | Modification du détenteur | 🟢 Natif |
| Historique via Chatter | Chatter | 🟢 Natif |
| Historique structuré des affectations | Non disponible | 🔴 Spécifique |
| Prêt temporaire | Non disponible | 🔴 Spécifique |
| Date de retour d'un prêt | Non disponible | 🔴 Spécifique |

### Conclusion

L'affectation permanente d'un équipement est couverte par le standard.
La gestion structurée des prêts temporaires et de l'historique des affectations nécessitera un développement spécifique.

---

## BM-04 — Gestion des garanties

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Fournisseur | Champ fournisseur | 🟢 Natif |
| Référence fournisseur | Champ référence fournisseur | 🟢 Natif |
| Modèle | Champ modèle | 🟢 Natif |
| Numéro de série | Numéro de série | 🟢 Natif |
| Date d'effet | Date d'effet | 🟢 Natif |
| Coût | Coût de l'équipement | 🟢 Natif |
| Date d'expiration | Date d'expiration de garantie | 🟢 Natif |
| Détection automatique sous garantie | Non disponible | 🔴 Spécifique |
| Détection automatique garantie expirée | Non disponible | 🔴 Spécifique |
| Alerte d'expiration | Non disponible | 🔴 Spécifique |
| Filtres sous garantie / expirée | Non disponible automatiquement | 🔴 Spécifique |

### Conclusion

Les informations nécessaires à la garantie sont disponibles nativement.
Le suivi automatisé des garanties nécessitera un développement spécifique.

---

## BM-05 — Incidents / demandes IT

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Créer une demande de maintenance | Demandes de maintenance | 🟢 Natif |
| Demandeur / employé | Champ employé | 🟢 Natif |
| Équipement concerné | Champ Équipement | 🟢 Natif |
| Catégorie | Catégorie de maintenance | 🟢 Natif |
| Priorité | Priorité | 🟢 Natif |
| Équipe | Équipe de maintenance | 🟢 Natif |
| Responsable | Responsable de la demande | 🟢 Natif |
| Planification | Dates planifiées | 🟢 Natif |
| États | Workflow des demandes | 🟢 Natif |
| Chatter | Chatter | 🟢 Natif |
| Lien équipement ↔ demandes | Smart button Maintenance | 🟢 Natif |
| Distinguer Incident IT / Demande de service IT | Non disponible nativement | 🔴 Spécifique |

### Conclusion

Le module Maintenance couvre nativement la gestion des demandes et leur rattachement aux équipements.
La distinction fonctionnelle entre Incident IT et Demande de service nécessitera une adaptation ou un développement spécifique.

---

## BM-06 — Interventions internes / externes

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Intervention interne | Demande de maintenance | 🟢 Natif |
| Équipement concerné | Équipement | 🟢 Natif |
| Équipe de maintenance | Équipe | 🟢 Natif |
| Technicien / responsable | Responsable | 🟢 Natif |
| Responsable prérempli | Affectation depuis l'équipement | 🟢 Natif |
| Chatter | Chatter | 🟢 Natif |
| Prestataire externe | Non disponible dans la demande standard | 🔴 Spécifique |
| Technicien externe | Non disponible | 🔴 Spécifique |
| Équipe externe | Non disponible | 🔴 Spécifique |
| Type interne / externe | Non disponible | 🔴 Spécifique |
| Coût de l'intervention | Non disponible directement | 🔴 Spécifique |
| Durée réelle de l'intervention | Non disponible directement | 🔴 Spécifique |

### Conclusion

Les interventions internes sont couvertes par le module Maintenance.
La gestion complète des interventions externes et de leurs coûts/durées nécessitera du spécifique.

---

## BM-07 — Maintenance préventive

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Maintenance corrective | Type de maintenance | 🟢 Natif |
| Maintenance préventive | Type de maintenance | 🟢 Natif |
| Récurrence | Option récurrente | 🟢 Natif |
| Périodicité | Jours / semaines / mois / années | 🟢 Natif |
| Équipement | Équipement | 🟢 Natif |
| Équipe | Équipe de maintenance | 🟢 Natif |
| Technicien / responsable | Responsable | 🟢 Natif |
| Planification | Dates planifiées | 🟢 Natif |
| Historique | Demandes liées à l'équipement | 🟢 Natif |
| Génération automatique vérifiée dans notre test | Non obtenue lors du test | 🔴 Spécifique |

### Conclusion

Odoo fournit nativement les principaux mécanismes de maintenance préventive et de récurrence.
Dans notre environnement de test, la génération automatique d'une nouvelle demande n'a pas été observée et sera donc traitée comme spécifique dans le périmètre actuel.

---

## BM-08 — Inventaire physique des équipements

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Inventaire physique des produits | Inventaire Inventory | 🟢 Natif |
| Préparation d'un inventaire d'équipements Maintenance | Non disponible | 🔴 Spécifique |
| Équipements attendus / trouvés | Non disponible | 🔴 Spécifique |
| Équipements manquants | Non disponible | 🔴 Spécifique |
| Équipements inconnus | Non disponible | 🔴 Spécifique |
| Gestion des écarts | Non disponible pour `maintenance.equipment` | 🔴 Spécifique |
| Validation de l'inventaire | Non disponible | 🔴 Spécifique |
| Chatter | Chatter | 🟢 Natif |
| Traçabilité spécifique des corrections | Non disponible | 🔴 Spécifique |

### Conclusion

L'inventaire physique natif d'Odoo concerne les produits et le stock.
Un processus d'inventaire physique dédié aux équipements Maintenance devra être développé.

---

## BM-09 — QR codes / identification rapide

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Identification par numéro de série | Numéro de série | 🟢 Natif |
| Barcode sur équipement Maintenance | Non disponible dans notre environnement | 🔴 Spécifique |
| QR code lié à un équipement | Non disponible | 🔴 Spécifique |
| Scan → ouverture de l'équipement | Non disponible | 🔴 Spécifique |
| Utilisation smartphone | Non disponible pour ce besoin | 🔴 Spécifique |

### Conclusion

Le numéro de série est disponible nativement.
La fonction QR/Barcode dédiée aux équipements Maintenance nécessitera un développement spécifique.

---

## BM-10 — SLA / priorités

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Priorité | Champ priorité | 🟢 Natif |
| Date planifiée | Date planifiée | 🟢 Natif |
| Fin planifiée | Date de fin planifiée | 🟢 Natif |
| Détection du retard | Calcul du retard | 🟢 Natif |
| Nombre de jours de retard | Indicateur de retard | 🟢 Natif |
| SLA selon priorité | Non disponible | 🔴 Spécifique |
| SLA selon type | Non disponible | 🔴 Spécifique |
| Délai maximum configurable | Non disponible | 🔴 Spécifique |
| Alerte SLA | Non disponible | 🔴 Spécifique |

### Test réalisé

Une demande planifiée au **2 septembre** avec une fin planifiée au **3 septembre** affichait automatiquement **8 jours de retard** dans le Chatter lors du test.

### Conclusion

Le suivi basique du retard est natif.
La gestion complète d'un SLA IT nécessitera un développement spécifique.

---

## BM-11 — Pièces et consommables

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Produits | Produits Odoo | 🟢 Natif |
| Produits consommables | Gestion des produits | 🟢 Natif |
| Stock disponible | Inventory | 🟢 Natif |
| Entrées / sorties | Mouvements de stock | 🟢 Natif |
| Quantité en stock | Stock | 🟢 Natif |
| Traçabilité des mouvements | Mouvements de stock | 🟢 Natif |
| Coût du produit | Coût | 🟢 Natif |
| Ajouter une pièce à une intervention | Non disponible | 🔴 Spécifique |
| Quantité consommée par intervention | Non disponible | 🔴 Spécifique |
| Lien pièce ↔ intervention | Non disponible | 🔴 Spécifique |
| Sortie de stock depuis l'intervention | Non disponible | 🔴 Spécifique |
| Coût des pièces par intervention | Non disponible | 🔴 Spécifique |

### Conclusion

Le stock et les produits sont gérés nativement par Odoo.
Le lien entre pièces consommées et interventions de maintenance devra être développé.

---

## BM-12 — Reporting / tableaux de bord

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Analyse des demandes de maintenance | Menu Analyse | 🟢 Natif |
| Vue graphique | Reporting Maintenance | 🟢 Natif |
| Table croisée / Pivot | Reporting Maintenance | 🟢 Natif |
| Vue liste | Reporting Maintenance | 🟢 Natif |
| Vue Kanban | Reporting Maintenance | 🟢 Natif |
| Calendrier | Reporting Maintenance | 🟢 Natif |
| Activité | Reporting Maintenance | 🟢 Natif |
| Filtres / groupements | Vues Odoo | 🟢 Natif |
| Reporting équipements | Liste / Kanban | 🟢 Natif |
| Vue graphique équipements dédiée | Non disponible | 🔴 Spécifique |
| Vue Pivot équipements dédiée | Non disponible | 🔴 Spécifique |
| Export équipements | Export Odoo | 🟢 Natif |
| Export demandes | Export Odoo | 🟢 Natif |
| Import | Import Odoo | 🟢 Natif |
| Dashboard métier personnalisé | Non disponible | 🔴 Spécifique |
| KPI coûts | Non disponible selon les besoins métier | 🔴 Spécifique |
| KPI temps d'intervention | Donnée non disponible nativement | 🔴 Spécifique |
| KPI garanties | Non disponible | 🔴 Spécifique |
| KPI affectations | Non disponible | 🔴 Spécifique |

### Conclusion

Odoo fournit de bonnes capacités natives d'analyse des demandes de maintenance.
Les tableaux de bord et KPI métier spécifiques nécessiteront des adaptations ou développements selon les données finalement retenues.

---

## BM-13 — Sécurité et droits d'accès

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Groupe Maintenance | Groupe « Gestionnaire d'équipement » | 🟢 Natif |
| Lecture | Access Rights | 🟢 Natif |
| Écriture | Access Rights | 🟢 Natif |
| Création | Access Rights | 🟢 Natif |
| Suppression | Access Rights | 🟢 Natif |
| Règles d'enregistrement | Record Rules | 🟢 Natif |
| Accès aux équipements | Droits du groupe | 🟢 Natif |
| Accès aux demandes | Droits du groupe | 🟢 Natif |
| Restriction par équipe | Non configurée nativement pour notre besoin | 🟠 Adaptation |
| Rôle technicien distinct | Non disponible | 🔴 Spécifique |
| Rôle utilisateur/employé limité | Non disponible | 🔴 Spécifique |
| Séparation complète des rôles métier | Non disponible | 🔴 Spécifique |

### Observation

Dans notre environnement, le groupe **Gestionnaire d'équipement** dispose de droits complets sur les principaux modèles Maintenance.

Les règles d'enregistrement observées utilisent le domaine `1`, ce qui ne limite pas les enregistrements.

### Conclusion

Le mécanisme de sécurité est natif.
La séparation des rôles métier et les restrictions spécifiques devront être adaptées ou développées.

---

## BM-14 — Cycle de vie des équipements

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| État métier de l'équipement | Non disponible dans la fiche équipement | 🔴 Spécifique |
| Actif | Non disponible comme état métier | 🔴 Spécifique |
| En maintenance | Non disponible comme état métier | 🔴 Spécifique |
| En prêt | Non disponible | 🔴 Spécifique |
| Hors service | Non disponible | 🔴 Spécifique |
| Rebut | Non disponible comme workflow d'état | 🔴 Spécifique |
| Changement d'état | Non disponible | 🔴 Spécifique |
| Historique des états | Non disponible | 🔴 Spécifique |
| Automatisation des changements d'état | Non disponible | 🔴 Spécifique |

### Conclusion

La fiche `maintenance.equipment` ne fournit pas de workflow métier permettant de gérer le cycle de vie complet demandé.
Un workflow spécifique devra être développé.

---

## BM-15 — Gestion des utilisateurs / portail IT

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Rôle Portail | Rôle / Portail | 🟢 Natif |
| Association demande ↔ employé | Champ employé | 🟢 Natif |
| Création d'une demande depuis le portail | `maintenance.request` absent des droits du groupe Portail | 🔴 Spécifique |
| Consultation des demandes | Non disponible pour le groupe Portail | 🔴 Spécifique |
| Suivi du statut | Non disponible | 🔴 Spécifique |
| Historique des demandes | Non disponible | 🔴 Spécifique |
| Consultation des équipements | `maintenance.equipment` absent des droits du groupe Portail | 🔴 Spécifique |
| Restriction de visibilité par utilisateur | Non disponible pour ce besoin | 🔴 Spécifique |

### Conclusion

Odoo fournit nativement le mécanisme général de portail.
Cependant, dans notre environnement, les modèles `maintenance.request` et `maintenance.equipment` ne sont pas accessibles au groupe Portail.

Le portail IT self-service devra donc être développé.

---

## BM-16 — Gestion documentaire

### Fonctionnalités identifiées

| Besoin | Fonctionnalité Odoo | Classification |
|---|---|---|
| Documentation technique | Fichiers attachés à l'équipement | 🟢 Natif |
| Factures | Pièces jointes | 🟢 Natif |
| Contrats | Pièces jointes | 🟢 Natif |
| Certificats de garantie | Pièces jointes | 🟢 Natif |
| Manuels | Pièces jointes | 🟢 Natif |
| Fichiers PDF | Pièces jointes | 🟢 Natif |
| Images | Pièces jointes | 🟢 Natif |
| Plusieurs documents | Pièces jointes multiples | 🟢 Natif |
| Consultation des fichiers | Ouverture / consultation | 🟢 Natif |
| Documents liés à l'équipement | Fichiers attachés à la fiche équipement | 🟢 Natif |
| Gestion documentaire avancée | Non analysée comme fonctionnalité métier native | 🟠 Adaptation |

### Conclusion

Odoo permet nativement d'attacher et de consulter plusieurs fichiers directement depuis la fiche équipement.

La gestion documentaire avancée pourra être étudiée ultérieurement si le besoin métier évolue.

---

# 3. Synthèse globale

## Fonctionnalités principalement natives

Odoo 19 Community fournit nativement :

- gestion des équipements ;
- affectation des équipements ;
- numéros de série ;
- demandes de maintenance ;
- maintenance corrective et préventive ;
- récurrence des maintenances ;
- équipes et responsables ;
- priorités ;
- planification ;
- suivi du retard ;
- Chatter ;
- produits et consommables ;
- gestion du stock ;
- mouvements de stock ;
- coûts produits ;
- reporting des demandes ;
- vues graphiques et Pivot ;
- import / export ;
- mécanismes de sécurité ;
- portail utilisateur ;
- pièces jointes et documents.

## Fonctionnalités nécessitant du spécifique

Les principaux besoins nécessitant du développement sont :

- historique structuré des affectations ;
- gestion des prêts temporaires ;
- suivi automatique des garanties ;
- distinction Incident / Demande de service ;
- interventions externes ;
- gestion des coûts et temps d'intervention ;
- génération automatique des demandes préventives selon le besoin retenu ;
- inventaire physique des équipements ;
- QR codes / Barcode des équipements ;
- scan mobile ;
- SLA métier ;
- consommation de pièces liée aux interventions ;
- coût des pièces par intervention ;
- dashboards métier ;
- rôles métier avancés ;
- cycle de vie des équipements ;
- portail IT self-service.

---

# 4. Conclusion de l'analyse

L'analyse montre qu'Odoo 19 Community fournit une base fonctionnelle importante pour le projet **IT Asset & Maintenance Management**.

Les fonctionnalités standards couvrent principalement :

> **Équipements + Maintenance + Affectation + Stock + Reporting + Sécurité + Documents**

Les besoins spécifiques concernent principalement les fonctionnalités métier qui permettent de transformer Odoo Maintenance en véritable **IT Asset Management / IT Service Management**, notamment :

> **Cycle de vie + Inventaire des équipements + QR/Barcode + Prêts + SLA + Pièces consommées + Portail IT + Reporting métier avancé**

Aucun développement spécifique ne doit être réalisé avant la fin de cette phase d'analyse.

La prochaine phase sera la **conception de la solution**, après validation de cette analyse fonctionnelle.