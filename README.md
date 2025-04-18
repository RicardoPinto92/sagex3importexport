# 🇬🇧 Enlgish Version
# 🔧 Reference Replacement Tool for CSV Files (SAGE X3)

This project is an interactive tool developed in **Python** to facilitate handling of CSV files used in **SAGE X3**, particularly in the processes of importing **tariffs and commercial discounts**.

## 🧩 Purpose

SAGE X3 uses CSV files to import tariff data that include item references and corresponding discounts. Often, there is a need to **keep** only certain references or **remove** others, as well as **replace** them with new references. Doing this manually on large files is tedious, error-prone, and inefficient.

This tool solves that in a simple and interactive way!

## ⚙️ Features

- ✅ Reads `.csv` files with typical SAGE X3 import tariff structure.
- ✅ Choose between:
  - **Keeping** only specific references.
  - **Removing** one or more references.
- ✅ Replace selected references with new ones.
- ✅ Option to:
  - **Overwrite** the original file.
  - **Create a new file** with the result, in the same folder as the original.
- ✅ Terminal interface with interactive menus using `inquirer` library.

## 🖼️ CSV Structure Example

```csv
E;Tariff123;;;
L;0001;REF001;10%;...
L;0001;REF002;15%;...
E;Tariff456;;;
L;0002;REF003;5%;...
```

## 📦 Requirements

- Python 3.6+
- `inquirer` library  
  Install it with:

```bash
pip install inquirer
```

## 🚀 How to Use

1. **Run the script:**

```bash
python substituidor.py
```

2. **Follow the interactive menu:**
   - Enter the path to the CSV file.
   - Choose whether to **keep** or **remove** references.
   - Define whether you will work with **one** or **multiple** references.
   - Enter references to keep or remove.
   - Enter new references (if replacing).
   - Choose to **overwrite the original file** or **create a new one**.

3. The resulting file is saved and ready for import into SAGE X3.

## 📝 Notes

- The file must follow the structure with lines starting with:
  - `"E"` to indicate the tariff header
  - `"L"` to indicate discount or detail lines
- Only `"L"` lines are processed for reference replacement.
- Substitutions are made only in the item reference column.

## 📌 Example

```
? What do you want to do with the references?
  ❯ 📌 Keep references
    ❌ Remove references
    🚪 Exit

? Are you working with one or multiple references?
  ❯ 🔹 One reference
    🔸 Multiple references

Enter the original reference: REF001
Enter the new reference to replace it: REF100

Enter the name or path of the CSV file: tariffs.csv

🔧 1 references were replaced.

How do you want to save the data?
  ❯ 📂 Overwrite original file
    🆕 Create new file
```

## 🤝 Contributions

Feel free to suggest improvements, report issues, or adapt the logic for other SAGE internal structures.

## 🧑‍💻 Author

This script was developed to optimize administrative workflows for managing item tariffs and discounts in SAGE X3.

---

# 🇵🇹 Versão em Português

## 🔧 Ferramenta de Substituição de Referências em Ficheiros CSV (SAGE X3)

Este projeto é uma ferramenta interativa desenvolvida em **Python** para facilitar a manipulação de ficheiros CSV utilizados no **SAGE X3**, nomeadamente nos processos de importação de **tarifas e descontos comerciais**.

## 🧩 Objetivo

O SAGE X3 recorre a ficheiros CSV para importar dados de tarifas que incluem referências de artigos e respetivos descontos. Muitas vezes, há necessidade de **manter** apenas determinadas referências ou de **eliminar** outras, bem como **substituí-las** por novas referências. Fazer isto manualmente num ficheiro extenso é trabalhoso, propenso a erros e ineficiente.

Esta ferramenta resolve isso de forma simples e interativa!

## ⚙️ Funcionalidades

- ✅ Leitura de ficheiros `.csv` com estrutura típica de importação de tarifas do SAGE X3.
- ✅ Escolha entre:
  - **Manter** apenas determinadas referências.
  - **Eliminar** uma ou várias referências.
- ✅ Substituição das referências selecionadas por novas referências.
- ✅ Possibilidade de:
  - **Sobrescrever** o ficheiro original.
  - **Criar um novo ficheiro** com o resultado, na mesma pasta do ficheiro original.
- ✅ Interface de terminal com menus interativos via biblioteca `inquirer`.

## 🖼️ Exemplo de Estrutura CSV

```csv
E;Tarifa123;;;
L;0001;REF001;10%;...
L;0001;REF002;15%;...
E;Tarifa456;;;
L;0002;REF003;5%;...
```

## 📦 Requisitos

- Python 3.6+
- Biblioteca `inquirer`  
  Podes instalar com:

```bash
pip install inquirer
```

## 🚀 Como Usar

1. **Executa o script:**

```bash
python substituidor.py
```

2. **Segue os menus interativos:**
   - Indica o caminho para o ficheiro CSV.
   - Escolhe se queres **manter** ou **eliminar** referências.
   - Define se vais tratar **uma** ou **várias** referências.
   - Introduz as referências a manter ou eliminar.
   - Introduz as novas referências (caso pretendas substituir).
   - Escolhe se queres **substituir o ficheiro original** ou **criar um novo**.

3. O ficheiro resultante é gravado e pronto para importação no SAGE X3.

## 📝 Notas

- O ficheiro deve seguir a estrutura com linhas iniciadas por:
  - `"E"` para indicar o cabeçalho da tarifa
  - `"L"` para indicar os descontos ou linhas de detalhe
- Apenas as linhas de tipo `"L"` são processadas em termos de substituição de referências.
- As substituições são feitas apenas nas colunas da referência de artigo.

## 📌 Exemplo de Utilização

```
? O que pretendes fazer com as referências? (Use seta ↑ ↓)
  ❯ 📌 Manter referências
    ❌ Eliminar referências
    🚪 Sair

? Pretendes trabalhar com uma ou várias referências?
  ❯ 🔹 Uma referência
    🔸 Várias referências

Indica a referência original: REF001
Indica a nova referência para substituir: REF100

Digite o nome ou caminho do arquivo CSV: tarifas.csv

🔧 1 referências foram substituídas.

Como queres guardar os dados?
  ❯ 📂 Substituir ficheiro original
    🆕 Criar novo ficheiro
```

## 🤝 Contribuições

Sinta-se à vontade para propor melhorias, reportar erros ou adaptar a lógica a outras estruturas internas do SAGE.

## 🧑‍💻 Autor

Este script foi desenvolvido com foco em otimizar fluxos de trabalho administrativos no contexto de gestão de artigos e descontos no SAGE X3.

---

# 🇫🇷 Version Française

## 🔧 Outil de Remplacement de Références dans les Fichiers CSV (SAGE X3)

Ce projet est un outil interactif développé en **Python** pour faciliter la manipulation de fichiers CSV utilisés dans **SAGE X3**, notamment dans les processus d'importation de **tarifs et remises commerciales**.

## 🧩 Objectif

SAGE X3 utilise des fichiers CSV pour importer des données tarifaires contenant des références d'articles et leurs remises associées. Il est souvent nécessaire de **conserver** certaines références uniquement, d’en **supprimer** d'autres ou de les **remplacer** par de nouvelles. Faire cela manuellement dans un grand fichier est fastidieux, source d’erreurs et inefficace.

Cet outil permet de le faire de manière simple et interactive !

## ⚙️ Fonctionnalités

- ✅ Lecture de fichiers `.csv` avec la structure typique d'importation tarifaire de SAGE X3.
- ✅ Choix entre :
  - **Conserver** uniquement certaines références.
  - **Supprimer** une ou plusieurs références.
- ✅ Remplacement des références sélectionnées par de nouvelles références.
- ✅ Possibilité de :
  - **Remplacer** le fichier original.
  - **Créer un nouveau fichier** avec les résultats, dans le même dossier que l’original.
- ✅ Interface en ligne de commande avec menus interactifs via la bibliothèque `inquirer`.

## 🖼️ Exemple de Structure CSV

```csv
E;Tarif123;;;
L;0001;REF001;10%;...
L;0001;REF002;15%;...
E;Tarif456;;;
L;0002;REF003;5%;...
```

## 📦 Prérequis

- Python 3.6+
- Bibliothèque `inquirer`  
  À installer avec :

```bash
pip install inquirer
```

## 🚀 Comment Utiliser

1. **Lancer le script :**

```bash
python substituidor.py
```

2. **Suivre les menus interactifs :**
   - Indiquer le chemin du fichier CSV.
   - Choisir si vous voulez **conserver** ou **supprimer** des références.
   - Définir si vous travaillez avec **une** ou **plusieurs** références.
   - Entrer les références à conserver ou à supprimer.
   - Entrer les nouvelles références (en cas de remplacement).
   - Choisir de **remplacer le fichier original** ou **créer un nouveau fichier**.

3. Le fichier résultant est enregistré et prêt à être importé dans SAGE X3.

## 📝 Remarques

- Le fichier doit respecter la structure suivante :
  - `"E"` indique l’en-tête du tarif
  - `"L"` indique les lignes de remise ou de détail
- Seules les lignes `"L"` sont traitées pour le remplacement des références.
- Les remplacements se font uniquement sur la colonne des références d’articles.

## 📌 Exemple d'Utilisation

```
? Que voulez-vous faire avec les références ?
  ❯ 📌 Conserver les références
    ❌ Supprimer les références
    🚪 Quitter

? Travaillez-vous avec une ou plusieurs références ?
  ❯ 🔹 Une référence
    🔸 Plusieurs références

Entrez la référence originale : REF001
Entrez la nouvelle référence pour la remplacer : REF100

Indiquez le chemin ou nom du fichier CSV : tarifs.csv

🔧 1 références ont été remplacées.

Comment souhaitez-vous enregistrer les données ?
  ❯ 📂 Remplacer le fichier original
    🆕 Créer un nouveau fichier
```

## 🤝 Contributions

N’hésitez pas à proposer des améliorations, signaler des bugs ou adapter la logique à d'autres structures internes de SAGE.

## 🧑‍💻 Auteur

Ce script a été développé pour optimiser les processus administratifs de gestion des articles et des remises dans SAGE X3.
