# 🛡️ Bank Fraud Analytics Dashboard

> Dashboard interactif d'analyse exploratoire des fraudes bancaires développé avec **Python**, **Streamlit** et **Microsoft Azure**.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Azure](https://img.shields.io/badge/Microsoft-Azure-0078D4)
![GitHub](https://img.shields.io/badge/GitHub-Actions-black)

---

# 📖 Présentation

Ce projet présente une **Analyse Exploratoire des Données (EDA)** réalisée sur un jeu de données contenant **5 millions de transactions bancaires**.

L'objectif est d'explorer les données, d'identifier les comportements frauduleux et de mettre en évidence les principaux indicateurs de fraude à travers un **dashboard interactif**.

Le projet couvre l'ensemble du cycle de développement, depuis l'analyse des données jusqu'au déploiement de l'application sur **Microsoft Azure**.

---

# 🎯 Objectifs du projet

- Explorer les transactions bancaires
- Comprendre les comportements frauduleux
- Réaliser des visualisations pertinentes
- Préparer les données pour le Machine Learning
- Développer un dashboard interactif
- Déployer une application web sur Microsoft Azure

---

# 📊 Analyses réalisées

Le dashboard est composé des pages suivantes :

- 🏠 Accueil
- 💰 Analyse des montants des transactions
- 💳 Analyse des types de transactions
- 🛍 Analyse des catégories de commerçants
- 🌍 Analyse des localisations
- 💳 Analyse des moyens de paiement
- 📱 Analyse des appareils utilisés
- ⚡ Analyse du Velocity Score
- 📈 Matrice de corrélation
- ✅ Conclusion

---

# 🚀 Réalisations du projet

Au cours de ce projet, les étapes suivantes ont été réalisées :

## 📌 1. Analyse exploratoire des données (EDA)

- Exploration du jeu de données
- Analyse statistique
- Étude de la variable cible
- Recherche des indicateurs de fraude
- Interprétation des résultats

---

## 📌 2. Création des visualisations

Création de graphiques avec **Matplotlib** afin d'analyser :

- le montant des transactions
- le type de transaction
- les catégories de commerçants
- les localisations
- les moyens de paiement
- les appareils utilisés
- le Velocity Score
- les corrélations entre variables

---

## 📌 3. Développement du Dashboard

Développement d'une application interactive avec **Streamlit** comprenant :

- une page d'accueil
- plusieurs pages d'analyse
- une navigation multipage
- une interface responsive
- une architecture modulaire

---

## 📌 4. Gestion du projet

Le projet a été organisé selon les bonnes pratiques de développement :

- architecture modulaire
- séparation du code
- fonctions réutilisables
- gestion des dépendances
- commentaires du code

---

## 📌 5. Versionnement

Le projet a été versionné avec :

- Git
- GitHub

---

## 📌 6. Intégration Continue (CI/CD)

Le déploiement est automatisé grâce à :

- GitHub Actions

À chaque mise à jour du dépôt GitHub, l'application est automatiquement redéployée.

---

## 📌 7. Déploiement Cloud

L'application est déployée sur :

- Microsoft Azure App Service

Le projet est donc accessible directement depuis un navigateur.

---

# 🛠 Technologies utilisées

## Langages

- Python

## Analyse de données

- Pandas
- NumPy

## Visualisation

- Matplotlib
- Seaborn

## Développement Web

- Streamlit

## Cloud

- Microsoft Azure App Service

## Versionnement

- Git
- GitHub

## CI/CD

- GitHub Actions

---

# 🏗 Architecture du projet

```text
bank-fraud-analytics-dashboard/
│
├── assets/
│   └── logo.png
│
├── data/
│   └── financial_fraud_detection_dataset.csv
│
├── images/
│
├── notebooks/
│   └── EDA_Financial_Fraud.ipynb
│
├── pages/
│   ├── 1_Transaction_Amount.py
│   ├── 2_Transaction_Type.py
│   ├── 3_Merchant_Category.py
│   ├── 4_Location.py
│   ├── 5_Payment_Channel.py
│   ├── 6_Device_Used.py
│   ├── 7_Velocity_Score.py
│   ├── 8_Correlation.py
│   └── 9_Conclusion.py
│
├── reports/
│   └── EDA_Financial_Fraud.html
│
├── app.py
├── utils.py
├── requirements.txt
└── README.md
```

---

# 📸 Aperçu du projet

## 🏠 Accueil

La page d'accueil présente les indicateurs clés du projet et les objectifs de l'analyse.

![Accueil](assets/Page_Acc.png)


---

## 💰 Analyse des montants

Cette visualisation illustre la distribution des montants des transactions bancaires au sein du jeu de données.

![Transaction Amount](images/amount_histogram.png)

---

## 📈 Matrice de corrélation

Cette visualisation met en évidence les relations entre les différentes variables du jeu de données.

![Correlation Matrix](images/correlation_matrix.png)

---

# ▶️ Exécuter le projet localement

## Cloner le dépôt

```bash
git clone https://github.com/adys-s/bank-fraud-analytics-dashboard.git
```

## Accéder au projet

```bash
cd bank-fraud-analytics-dashboard
```

## Installer les dépendances

```bash
pip install -r requirements.txt
```

## Lancer l'application

```bash
streamlit run app.py
```

---

# 🌐 Démonstration

## Application en ligne

👉 **Azure App Service**

**Lien :**

*(Ajouter l'URL Azure ici)*

---

# 💼 Compétences développées

À travers ce projet, les compétences suivantes ont été mobilisées :

### Data Analytics

- Analyse exploratoire des données
- Analyse statistique
- Visualisation de données
- Interprétation des résultats

### Développement

- Python
- Streamlit
- Architecture modulaire
- Réutilisation de fonctions

### Data Engineering

- Gestion de projet
- Git
- GitHub
- Gestion des dépendances

### Cloud Computing

- Microsoft Azure
- Azure App Service
- Déploiement d'application web

### DevOps

- GitHub Actions
- Déploiement continu (CI/CD)

---

# 🎯 Résultat

Ce projet a permis de :

- réaliser une analyse exploratoire complète sur un jeu de données de fraude bancaire ;
- développer une application web interactive avec Streamlit ;
- organiser le projet selon les bonnes pratiques de développement ;
- versionner le code avec Git et GitHub ;
- automatiser le déploiement avec GitHub Actions ;
- déployer l'application sur Microsoft Azure.

Le projet est désormais entièrement fonctionnel et accessible en ligne.

---

# 👨‍💻 Auteur

**Yawa Silvère ADODO-DAHOUE**

Étudiante en Data Engineering & Data Analytics

GitHub :
https://github.com/adys-s

LinkedIn :
*(Ajouter ton profil LinkedIn)*

---

⭐ Si ce projet vous a intéressé, n'hésitez pas à le consulter, à laisser une étoile sur GitHub ou à me contacter pour échanger autour de la Data, du Cloud et du Machine Learning.# bank-fraud-analytics-dashboard
Interactive dashboard for exploratory analysis of banking fraud transactions built with Python, Streamlit and Microsoft Azure.
