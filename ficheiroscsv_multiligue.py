import csv
import os
import inquirer

# Idiomas
IDIOMAS = {
    "🇬🇧 English": "en",
    "🇵🇹 Português": "pt",
    "🇫🇷 Français": "fr"
}

TEXTOS = {
    "en": {
        "file_prompt": "Enter the name or path of the CSV file: ",
        "invalid_file": "Please provide a valid file name or path.",
        "not_found": "File not found. Try again.",
        "main_action": "What do you want to do with the references?",
        "replace": "📌 Replace references",
        "delete": "❌ Delete references",
        "exit": "🚪 Exit",
        "one_or_many": "Do you want to work with one or multiple references?",
        "one": "🔹 One reference",
        "many": "🔸 Multiple references",
        "original_ref": "Enter the original reference: ",
        "original_refs": "Enter the original references separated by commas: ",
        "new_ref": "Enter the new reference to replace: ",
        "new_refs": "Enter the new references (in same order), separated by commas: ",
        "subs_done": "🔧 {} references were replaced.",
        "save_option": "How do you want to save the data?",
        "overwrite": "📂 Overwrite original file",
        "new_file": "🆕 Create new file",
        "new_file_name": "Enter the name for the new file (without extension): ",
        "invalid_name": "Invalid name.",
        "saved": "\n✅ Data saved to: {}",
        "save_error": "\n❌ Error saving: {}",
        "bye": "👋 See you soon!",
        "done": "\n✅ Operation completed.\n"
    },
    "pt": {
        "file_prompt": "Digite o nome ou caminho do arquivo CSV: ",
        "invalid_file": "Por favor, forneça um nome ou caminho válido.",
        "not_found": "Ficheiro não encontrado. Tente novamente.",
        "main_action": "O que pretendes fazer com as referências?",
        "replace": "📌 substituir referências",
        "delete": "❌ Eliminar referências",
        "exit": "🚪 Sair",
        "one_or_many": "Pretendes trabalhar com uma ou várias referências?",
        "one": "🔹 Uma referência",
        "many": "🔸 Várias referências",
        "original_ref": "Indica a referência original: ",
        "original_refs": "Indica as referências originais separadas por vírgula: ",
        "new_ref": "Indica a nova referência para substituir: ",
        "new_refs": "Indica as novas referências (na mesma ordem), separadas por vírgula: ",
        "subs_done": "🔧 {} referências foram substituídas.",
        "save_option": "Como queres guardar os dados?",
        "overwrite": "📂 Substituir ficheiro original",
        "new_file": "🆕 Criar novo ficheiro",
        "new_file_name": "Digite o nome para o novo ficheiro (sem extensão): ",
        "invalid_name": "Nome inválido.",
        "saved": "\n✅ Dados guardados em: {}",
        "save_error": "\n❌ Erro ao guardar: {}",
        "bye": "👋 Até breve!",
        "done": "\n✅ Operação concluída.\n"
    },
    "fr": {
        "file_prompt": "Entrez le nom ou le chemin du fichier CSV : ",
        "invalid_file": "Veuillez fournir un nom ou un chemin valide.",
        "not_found": "Fichier non trouvé. Réessayez.",
        "main_action": "Que voulez-vous faire avec les références ?",
        "replace": "📌 Remplacer les références",
        "delete": "❌ Supprimer les références",
        "exit": "🚪 Quitter",
        "one_or_many": "Voulez-vous travailler avec une ou plusieurs références ?",
        "one": "🔹 Une référence",
        "many": "🔸 Plusieurs références",
        "original_ref": "Indiquez la référence d'origine : ",
        "original_refs": "Indiquez les références d'origine, séparées par des virgules : ",
        "new_ref": "Indiquez la nouvelle référence à remplacer : ",
        "new_refs": "Indiquez les nouvelles références (dans le même ordre), séparées par des virgules : ",
        "subs_done": "🔧 {} références ont été remplacées.",
        "save_option": "Comment souhaitez-vous enregistrer les données ?",
        "overwrite": "📂 Remplacer le fichier original",
        "new_file": "🆕 Créer un nouveau fichier",
        "new_file_name": "Entrez le nom du nouveau fichier (sans extension) : ",
        "invalid_name": "Nom invalide.",
        "saved": "\n✅ Données enregistrées dans : {}",
        "save_error": "\n❌ Erreur lors de l'enregistrement : {}",
        "bye": "👋 À bientôt !",
        "done": "\n✅ Opération terminée.\n"
    }
}

def obter_arquivo_csv(textos):
    while True:
        arquivo_csv = input(textos["file_prompt"]).strip()
        if not arquivo_csv:
            print(textos["invalid_file"])
            continue

        if not os.path.isabs(arquivo_csv):
            arquivo_csv = os.path.join(os.getcwd(), arquivo_csv)

        if os.path.isfile(arquivo_csv):
            return arquivo_csv
        else:
            print(textos["not_found"])


def ler_csv(arquivo_csv):
    with open(arquivo_csv, mode='r', encoding='utf-8') as file:
        return list(csv.reader(file, delimiter=';'))


def filtrar_substituir(linhas, modo, referencias_originais, referencias_novas):
    cabecalho = None
    descontos = []
    resultados = []
    substituicoes = 0

    for row in linhas:
        if row[0] == 'E':
            if cabecalho and descontos:
                resultados.append(cabecalho)
                resultados.extend(descontos)
            cabecalho = row
            descontos = []

        elif row[0] == 'L':
            ref = row[2].strip()

            if modo == "substituir" and ref in referencias_originais:
                index = referencias_originais.index(ref)
                row[2] = referencias_novas[index] if index < len(referencias_novas) else ref
                descontos.append(row)
                substituicoes += 1

            elif modo == "eliminar" and ref not in referencias_originais:
                descontos.append(row)
            elif modo == "eliminar" and ref in referencias_originais:
                index = referencias_originais.index(ref)
                row[2] = referencias_novas[index] if index < len(referencias_novas) else ref
                descontos.append(row)
                substituicoes += 1

    if cabecalho and descontos:
        resultados.append(cabecalho)
        resultados.extend(descontos)

    return resultados, substituicoes


def salvar_resultados(resultados, caminho_original, textos):
    pergunta = [
        inquirer.List(
            'opcao',
            message=textos["save_option"],
            choices=[textos["overwrite"], textos["new_file"]]
        )
    ]
    resposta = inquirer.prompt(pergunta)['opcao']

    if textos["overwrite"] in resposta:
        caminho = caminho_original
    else:
        nome_novo = input(textos["new_file_name"]).strip()
        if not nome_novo:
            print(textos["invalid_name"])
            return
        pasta = os.path.dirname(caminho_original)
        caminho = os.path.join(pasta, nome_novo + ".csv")

    try:
        with open(caminho, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerows(resultados)
        print(textos["saved"].format(caminho))
    except Exception as e:
        print(textos["save_error"].format(e))


def menu():
    lingua = inquirer.prompt([
        inquirer.List("lang", message="Select language / Seleciona o idioma / Choisissez la langue", choices=list(IDIOMAS.keys()))
    ])["lang"]
    lang_code = IDIOMAS[lingua]
    textos = TEXTOS[lang_code]

    caminho_csv = obter_arquivo_csv(textos)
    linhas = ler_csv(caminho_csv)

    while True:
        acao = inquirer.prompt([
            inquirer.List("modo", message=textos["main_action"], choices=[textos["replace"], textos["delete"], textos["exit"]])
        ])["modo"]

        if textos["exit"] in acao:
            print(textos["bye"])
            break

        modo = "substituir" if textos["replace"] in acao else "eliminar"

        quantas = inquirer.prompt([
            inquirer.List("tipo", message=textos["one_or_many"], choices=[textos["one"], textos["many"]])
        ])["tipo"]

        if textos["one"] in quantas:
            referencias_originais = [input(textos["original_ref"]).strip()]
            referencias_novas = [input(textos["new_ref"]).strip()] if modo == "substituir" else []
        else:
            referencias_originais = input(textos["original_refs"]).split(',')
            referencias_originais = [r.strip() for r in referencias_originais]
            referencias_novas = input(textos["new_refs"]).split(',') if modo == "substituir" else []
            referencias_novas = [r.strip() for r in referencias_novas]

        resultados, num_subs = filtrar_substituir(linhas, modo, referencias_originais, referencias_novas)
        print(textos["subs_done"].format(num_subs))
        salvar_resultados(resultados, caminho_csv, textos)
        print(textos["done"])


if __name__ == "__main__":
    menu()
