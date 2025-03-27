import hashlib

def calcular_hashes(texto):
    sha256 = hashlib.sha256(texto.encode('utf-8')).hexdigest()
    md5 = hashlib.md5(texto.encode('utf-8')).hexdigest()
    return sha256, md5

def verificar_frases(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        for linha in file:
            if not linha.strip():
                continue
            try:
                frase, sha_esperado, md5_esperado = linha.strip().split(" - ")
                frase = frase.strip('"')  # remove aspas do início e fim, se houver
                sha_calc, md5_calc = calcular_hashes(frase)

                print(f'\nFrase: "{frase}"')
                print(f'SHA256 esperado: {sha_esperado}')
                print(f'SHA256 calculado: {sha_calc}')
                print(f'MD5 esperado:    {md5_esperado}')
                print(f'MD5 calculado:   {md5_calc}')

                sha_ok = sha_calc == sha_esperado
                md5_ok = md5_calc == md5_esperado

                if sha_ok and md5_ok:
                    print("Passou: SHA256 e MD5 corretos")
                else:
                    print("Não passou:")
                    if not sha_ok and not md5_ok:
                        print("- Nenhum hash confere. Possíveis causas:")
                        print("  • Frase diferente da original usada no hash")
                        print("  • Espaço ou pontuação diferentes")
                        print("  • Aspas indevidas")
                    elif not sha_ok:
                        print("- SHA256 incorreto")
                    elif not md5_ok:
                        print("- MD5 incorreto")
            except ValueError:
                print(f"\nErro ao processar linha: {linha.strip()}")
                print("Formato esperado: \"frase\" - SHA256 - MD5")

# Caminho do arquivo com frases
arquivo = "frases.txt"
verificar_frases(arquivo)
