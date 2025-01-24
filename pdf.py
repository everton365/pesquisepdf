import os
import PyPDF2

def procurar_chave_em_pdfs(pasta, chave):
    """
    Procura uma chave de acesso em todos os arquivos PDF de uma pasta e lista os arquivos encontrados.
    
    :param pasta: Caminho da pasta com os PDFs.
    :param chave: Chave de acesso a ser procurada.
    """
    arquivos_pdf = [f for f in os.listdir(pasta) if f.lower().endswith('.pdf')]
    encontrados = []

    for arquivo in arquivos_pdf:
        caminho_pdf = os.path.join(pasta, arquivo)
        try:
            with open(caminho_pdf, 'rb') as pdf_file:
                leitor = PyPDF2.PdfReader(pdf_file)
                for pagina in leitor.pages:
                    if chave in pagina.extract_text():
                        encontrados.append(caminho_pdf)
                        print(f"Chave encontrada no arquivo: {arquivo}")
                        break
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

    if not encontrados:
        print("Chave não encontrada em nenhum arquivo PDF.")
        return

    while True:
        print("\nArquivos encontrados:")
        for i, arquivo in enumerate(encontrados, 1):
            print(f"{i}. {arquivo}")

        try:
            escolha = int(input("\nDigite o número do arquivo que deseja abrir (ou 0 para sair): "))
            if escolha == 0:
                print("Saindo...")
                break
            elif 1 <= escolha <= len(encontrados):
                os.startfile(encontrados[escolha - 1])  # Abre o arquivo escolhido
            else:
                print("Escolha inválida.")
        except ValueError:
            print("Por favor, insira um número válido.")

# Configuração
pasta = input("Digite o caminho da pasta onde estão os arquivos PDF: ").strip()
chave = input("Digite a chave de acesso que deseja buscar: ").strip()

# Verifica se a pasta existe
if os.path.exists(pasta) and os.path.isdir(pasta):
    procurar_chave_em_pdfs(pasta, chave)
else:
    print("Caminho inválido. Por favor, insira um caminho válido para a pasta.")
