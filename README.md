# 🛡️ Bank Fraud Analytics Dashboard

> Dashboard interactif d'analyse exploratoire des fraudes bancaires développé avec **Python**, **Streamlit** et **Microsoft Azure App Service**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Azure](https://img.shields.io/badge/Microsoft-Azure-0078D4)
![Git](https://img.shields.io/badge/Git-Version_Control-orange)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI--CD-success)

[![Live Demo](https://img.shields.io/badge/🚀-Application_en_ligne-brightgreen)](https://bank-fraud-dashboard-c4esada6b0f0fkdp.francecentral-01.azurewebsites.net/)
[![Repository](https://img.shields.io/badge/📂-GitHub-black)](https://github.com/adys-s/bank-fraud-analytics-dashboard)

---

## 📖 Présentation

Ce projet présente une **Analyse Exploratoire des Données (EDA)** réalisée sur un jeu de données de **5 millions de transactions bancaires**.

L'objectif est d'identifier les principaux comportements frauduleux à travers des analyses statistiques et des visualisations interactives développées avec **Streamlit**.

Le projet couvre l'ensemble du cycle de développement :

- Exploration des données
- Création des visualisations
- Développement d'une application Streamlit
- Gestion du code avec Git et GitHub
- Déploiement continu avec GitHub Actions
- Hébergement sur Microsoft Azure App Service

---

## 🎯 Objectifs

- Explorer un jeu de données de fraude bancaire
- Identifier les comportements frauduleux
- Réaliser des visualisations pertinentes
- Développer un dashboard interactif
- Déployer une application web sur Microsoft Azure

---

## 📊 Pages du dashboard

Le tableau de bord comprend les sections suivantes :

-  Accueil
-  Analyse des montants des transactions
-  Analyse des types de transactions
-  Analyse des catégories de commerçants
-  Analyse des localisations
-  Analyse des moyens de paiement
-  Analyse des appareils utilisés
-  Analyse du Velocity Score
-  Matrice de corrélation
-  Conclusion

---

## 🚀 Fonctionnalités

### 📌 Analyse exploratoire des données

- Exploration du jeu de données
- Analyse statistique
- Étude de la variable cible
- Identification des indicateurs de fraude
- Interprétation des résultats

### 📌 Visualisation

Création de graphiques avec **Matplotlib** pour analyser :

- les montants des transactions
- les types de transaction
- les catégories de commerçants
- les localisations
- les moyens de paiement
- les appareils utilisés
- le Velocity Score
- les corrélations entre variables

### 📌 Dashboard interactif

Application développée avec **Streamlit** comprenant :

- une navigation multipage
- une interface intuitive
- des graphiques interactifs
- une architecture modulaire

### 📌 Déploiement Cloud

Le projet est déployé sur **Microsoft Azure App Service** avec :

- Git
- GitHub
- GitHub Actions (CI/CD)

Chaque mise à jour du dépôt GitHub déclenche automatiquement un nouveau déploiement.

---

## 🛠 Technologies utilisées

| Domaine | Technologies |
|----------|--------------|
| Langage | Python |
| Analyse de données | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| Développement Web | Streamlit |
| Versionnement | Git, GitHub |
| CI/CD | GitHub Actions |
| Cloud | Microsoft Azure App Service |

---

## 🏗 Architecture du projet

```text
bank-fraud-analytics-dashboard/
│
├── assets/
├── data/
├── images/
├── notebooks/
├── pages/
├── reports/
│
├── app.py
├── utils.py
├── requirements.txt
└── README.md
```

---

## 📸 Aperçu du projet

### 🏠 Page d'accueil

Présentation générale du projet et des principaux indicateurs.

![Accueil](assets/Page_Acc.png)

---

### 💰 Analyse des montants

Visualisation de la distribution des montants des transactions.

![Transaction Amount](images/amount_histogram.png)

---

### 📈 Matrice de corrélation

Visualisation des relations entre les variables numériques.

![Correlation Matrix](images/correlation_matrix.png)

---

## ▶️ Exécuter le projet localement

### Cloner le dépôt

```bash
git clone https://github.com/adys-s/bank-fraud-analytics-dashboard.git
```

### Accéder au projet

```bash
cd bank-fraud-analytics-dashboard
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

### Lancer l'application

```bash
streamlit run app.py
```

---

## 🌐 Démonstration

🚀 **Application en ligne**

https://bank-fraud-dashboard-c4esada6b0f0fkdp.francecentral-01.azurewebsites.net/

📂 **Dépôt GitHub**

https://github.com/adys-s/bank-fraud-analytics-dashboard

---

## 💼 Compétences mobilisées

### Data Analytics

- Analyse exploratoire des données (EDA)
- Analyse statistique
- Visualisation de données
- Interprétation des résultats

### Développement

- Python
- Streamlit
- Architecture modulaire

### Data Engineering

- Gestion de projet
- Gestion des dépendances
- Git & GitHub

### Cloud Computing

- Microsoft Azure App Service
- Déploiement d'application

### DevOps

- GitHub Actions
- Intégration et déploiement continus (CI/CD)

---

## 🎯 Résultat

Ce projet a permis de :

- réaliser une analyse exploratoire complète d'un jeu de données de fraude bancaire ;
- développer une application web interactive avec Streamlit ;
- structurer un projet Python selon les bonnes pratiques ;
- mettre en place un pipeline de déploiement continu avec GitHub Actions ;
- déployer l'application sur Microsoft Azure App Service.

---

## 👨‍💻 Auteur

**Yawa Silvère ADODO-DAHOUE**

🎓 Étudiante en Data Engineering & Data Analytics

GitHub : https://github.com/adys-s

---

⭐ N'hésitez pas à consulter le projet, tester l'application et laisser une étoile sur le dépôt GitHub si celui-ci vous a intéressé.
