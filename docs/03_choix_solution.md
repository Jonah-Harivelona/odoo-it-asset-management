# Phase 3 — Choix de la solution

**Objectif :** convertir chaque besoin métier (BM) en décision fonctionnelle/technique, classée :
🟢 Natif · 🔵 Configuration · 🟠 Adaptation · 🔴 Développement spécifique.
Principe : réutiliser le standard Odoo au maximum, développer seulement le nécessaire.

---

## BM-01 — Gestion des équipements
**Besoin :** gérer le parc IT (PC, écrans, imprimantes, téléphones…) avec infos, détenteur, localisation, garantie, historique.
**Constat :** `maintenance.equipment` couvre déjà nom, catégorie, détenteur, équipe, technicien, lieu, fournisseur, modèle, n° série, coût, garantie, chatter, demandes liées.
**Décision :** `maintenance.equipment` = objet central ; natif conservé + adaptations ciblées.
**Classification :** 🟢 + 🟠
**Périmètre :** créer/gérer équipements, infos techniques, n° série, détenteur/localisation, garantie, historique, lien maintenance.

## BM-02 — Identification / inventaire
**Besoin :** identification unique + traçabilité (n° série).
**Constat :** n° série natif (équipement + produits Inventory) ; QR code non couvert.
**Décision :** n° série = identifiant principal ; QR traité en BM-09.
**Classification :** 🟢 + 🟠
**Périmètre :** identification par n° série, traçabilité, recherche, suivi inventaire, préparation QR.

## BM-03 — Affectation des équipements
**Besoin :** affecter à un employé ; distinguer permanent/prêt/retour/historique.
**Constat :** affectation + traçabilité chatter natives ; cycle prêt→usage→retour absent.
**Décision :** garder l'affectation native + développer gestion prêts/retours.
**Classification :** 🟢 + 🔴
**Périmètre :** affectation permanente, prêt temporaire, date début/retour prévue/effective, historique mouvements.

## BM-04 — Gestion des garanties
**Besoin :** suivi garanties + alertes échéance + retours SAV.
**Constat :** date d'expiration native ; statut garantie, alertes, SAV, historique absents.
**Décision :** garder la date native + développer la logique métier complémentaire.
**Classification :** 🟢 + 🔴
**Périmètre :** dates garantie, statut, suivi échéances, retour SAV, historique.

## BM-05 — Incidents / demandes IT
**Besoin :** déclarer/suivre un incident ou une demande IT jusqu'à résolution.
**Constat :** module Maintenance gère les demandes liées aux équipements, mais pas un vrai Service Desk (catégorie, priorité, responsable, résolution).
**Décision :** base technique = Maintenance ; développement spécifique pour la gestion IT.
**Classification :** 🟠 + 🔴
**Périmètre :** création demande, catégorisation, équipement, demandeur, responsable, priorité, statut, suivi, résolution, historique.

## BM-06 — Interventions internes / externes
**Besoin :** suivre interventions (technicien interne ou prestataire externe), durée, coût.
**Constat :** Maintenance gère les demandes/interventions de base, sans distinction interne/externe complète.
**Décision :** adapter les demandes de maintenance pour couvrir interne/externe.
**Classification :** 🟠 + 🔴
**Périmètre :** type intervention, technicien interne, prestataire externe, date, durée, coût, compte rendu, équipement, historique.

## BM-07 — Maintenance préventive
**Besoin :** planifier la maintenance selon une périodicité.
**Constat :** Odoo Maintenance couvre déjà demandes préventives, récurrence, périodicité, intervalles.
**Décision :** utiliser le standard + configuration ; pas de développement pour l'instant.
**Classification :** 🟢 + 🔵
**Périmètre :** maintenance préventive, périodicité, récurrence, planification, suivi.

## BM-08 — Inventaire physique des équipements
**Besoin :** inventaire physique du parc + détection d'écarts réel/enregistré.
**Constat :** Inventory gère nativement produits/traçabilité, mais pas de contrôle physique dédié à `maintenance.equipment`.
**Décision :** réutiliser Inventory quand pertinent + développer un mécanisme dédié.
**Classification :** 🟢 + 🔴
**Périmètre :** lancement inventaire, vérification, équipements trouvés/manquants, écarts, historique.

## BM-09 — QR codes / identification rapide
**Besoin :** identifier rapidement un équipement via QR code.
**Constat :** non couvert par le standard Odoo 19 CE.
**Décision :** développement spécifique complet.
**Classification :** 🔴
**Périmètre :** génération QR, association à l'équipement, affichage/impression, identification rapide, accès fiche.

## BM-10 — SLA / priorités
**Besoin :** prioriser et suivre les demandes IT selon des délais.
**Constat :** priorité représentable nativement, mais pas de vrai mécanisme SLA (délais, échéance, dépassement).
**Décision :** ajouter une gestion SLA spécifique aux demandes IT.
**Classification :** 🟠 + 🔴
**Périmètre :** niveaux priorité, délais prise en charge/résolution, échéances, détection dépassement, suivi performance.
*Test concret :* demande planifiée le 2/09, fin prévue le 3/09 → Odoo affiche automatiquement "8 jours de retard" dans le Chatter (détection native du retard = 🟢).

## BM-11 — Pièces et consommables
**Besoin :** gérer pièces/consommables utilisés en intervention + suivi stock.
**Constat :** Inventory gère déjà produits, consommables, quantités, mouvements, traçabilité.
**Décision :** Inventory = moteur stock ; ajouter uniquement le lien pièces↔interventions.
**Classification :** 🟢 + 🟠
**Périmètre :** catalogue pièces, consommables, quantités dispo, consommation en intervention, historique, impact stock.

## BM-12 — Reporting / tableaux de bord
**Besoin :** vision synthétique du parc et de l'activité IT.
**Constat :** listes/filtres/recherches/vues statistiques natifs ; tableau de bord métier dédié absent.
**Décision :** réutiliser les vues natives + développer un reporting métier complémentaire.
**Classification :** 🟢 + 🔴
**Périmètre :** nb équipements, équipements par état/affectation, garanties proches échéance, incidents, demandes IT, maintenances, interventions, équipements déclassés.

## BM-13 — Sécurité et droits d'accès
**Besoin :** accès limité selon le rôle utilisateur.
**Constat :** utilisateurs, groupes, droits, règles d'accès, permissions natifs.
**Décision :** utiliser la sécurité Odoo native + définir les rôles du projet.
**Classification :** 🟢 + 🔵
**Périmètre :** rôles (Administrateur IT, Responsable IT, Technicien IT, Utilisateur/Employé), droits définis par rôle.

## BM-14 — Cycle de vie des équipements
**Besoin :** suivre l'état réel d'un équipement (stock, affecté, en maintenance, réparation externe, attente retour, déclassé/rebut).
**Constat :** infos partielles côté maintenance/rebut, workflow métier complet absent.
**Décision :** ajouter un statut de cycle de vie spécifique.
**Classification :** 🟠 + 🔴
**Périmètre :** définition des états, changement contrôlé, historique, intégration maintenance/retours/réparations externes, déclassement/rebut.

## BM-15 — Gestion des utilisateurs / portail IT
**Besoin :** interaction utilisateur avec le service IT sans accès admin complet (consulter équipements, créer/suivre demandes, historique).
**Constat :** utilisateurs/contacts/employés/portail natifs ; portail métier IT spécifique absent.
**Décision :** réutiliser les mécanismes natifs + développer le portail IT spécifique.
**Classification :** 🟠 + 🔴
**Périmètre :** portail utilisateur, consultation équipements affectés, création/suivi demandes, historique, accès selon droits.

## BM-16 — Gestion documentaire
**Besoin :** conserver/retrouver documents liés (factures, BL, garanties, contrats, rapports, justificatifs).
**Constat :** chatter + pièces jointes natifs.
**Décision :** utiliser les mécanismes documentaires natifs, organisés autour équipements/demandes/interventions.
**Classification :** 🟢 + 🟠
**Périmètre :** pièces jointes équipements, documents interventions/garanties, consultation depuis fiches, historique documentaire.

---

## Synthèse des décisions

| BM | Décision |
|----|----------|
| BM-01 | 🟢+🟠 |
| BM-02 | 🟢+🟠 |
| BM-03 | 🟢+🔴 |
| BM-04 | 🟢+🔴 |
| BM-05 | 🟠+🔴 |
| BM-06 | 🟠+🔴 |
| BM-07 | 🟢+🔵 |
| BM-08 | 🟢+🔴 |
| BM-09 | 🔴 |
| BM-10 | 🟠+🔴 |
| BM-11 | 🟢+🟠 |
| BM-12 | 🟢+🔴 |
| BM-13 | 🟢+🔵 |
| BM-14 | 🟠+🔴 |
| BM-15 | 🟠+🔴 |
| BM-16 | 🟢+🟠 |

---

## Architecture fonctionnelle retenue

**Socle standard :**
- Maintenance : équipements, demandes, maintenance préventive.
- Inventory : produits, n° série, stock, mouvements, traçabilité.
- Contacts/Employees/Users : utilisateurs, employés, détenteurs, prestataires.
- Chatter/pièces jointes : historique, communication, documents.

**Extensions spécifiques à développer :**
prêts/retours · suivi avancé garanties · demandes IT · interventions internes/externes · inventaire physique dédié · QR codes · SLA · cycle de vie équipements · portail IT · reporting métier.

---

## Principe directeur

> Réutiliser au maximum le standard Odoo 19 Community et développer uniquement les fonctionnalités nécessaires à la couverture des besoins métier.

## Résultat Phase 3 → Phase 4

Les 16 BM ont une décision claire et un périmètre défini. La Phase 4 (Conception) devra définir : modèles Odoo, champs, relations, workflows, statuts, rôles, menus, vues, règles de sécurité, processus métier, architecture du module.