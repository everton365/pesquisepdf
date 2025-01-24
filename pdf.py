import os
import PyPDF2

def procurar_chave_em_pdfs(pasta, chave):
    """
    Procura uma chave de acesso em todos os arquivos PDF de uma pasta e abre o arquivo encontrado.

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
                        os.startfile(caminho_pdf)  # Abre o arquivo no programa padrão do sistema
                        break
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

    if not encontrados:
        print("Chave não encontrada em nenhum arquivo PDF.")

# Configuração
pasta = input("Digite o caminho da pasta onde estão os arquivos PDF: ").strip()
chave = input("Digite a chave de acesso que deseja buscar: ").strip()

# Verifica se a pasta existe
if os.path.exists(pasta) and os.path.isdir(pasta):
    procurar_chave_em_pdfs(pasta, chave)
else:
    print("Caminho inválido. Por favor, insira um caminho válido para a pasta.")
