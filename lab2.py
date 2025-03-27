import hashlib

# Simulação de conteúdos que poderiam ter gerado os hashes
possiveis_conteudos = [
    "A primeira das instituições criadas pelo Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP.",
    "A FEI é uma instituição vinculada estatutariamente à Companhia de Jesus.",
    "Em 20 de janeiro de 1951 foi realizada a sessão solene da congregação para a Colação de Grau da primeira turma da Faculdade de Engenharia Industrial.",
    "A Capela Santo Inácio de Loyola foi construída no ano de 1978, em concreto aparente.",
    "Tendo como função principal a promoção do aprimoramento profissional no campo administrativo e tecnológico, o IECAT (Instituto de Especialização em Ciências Administrativas e Tecnológicas) foi criado em 1982",
    "Dentro de uma proposta de integração e de agregação de competências, visando a excelência de seus cursos, as instituições FEI, FCI e ESAN foram transformadas no Centro Universitário da FEI no ano de 2002",
    "O Centro Universitário da FEI passou a fazer parte do seleto grupo que produz ciência no Brasil, quando a CAPES aprovou o primeiro curso de Mestrado em Engenharia Elétrica em 2005.",
    "Em 2016 foi realizada a primeira edição do congresso de inovação - Megatendências 2050.",
    "Em 2012 o Centro Universitário FEI celebrou 70 anos de história e de excelência na inovação e na formação de mais de 50 mil profissionais altamente qualificados para o setor empresarial, entre Administradores, Engenheiros e Cientistas da Computação.",
    "Em 1999 iniciam-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação.",
    
]

def calcular_hashes(conteudo):
    sha256 = hashlib.sha256(conteudo.encode()).hexdigest()
    md5 = hashlib.md5(conteudo.encode()).hexdigest()
    return sha256, md5

def carregar_hashes_do_arquivo(caminho):
    pares_hashes = []
    with open(caminho, 'r') as f:
        for linha in f:
            if '-' in linha:
                sha256, md5 = linha.strip().split(' - ')
                pares_hashes.append((sha256, md5))
    return pares_hashes

def verificar_hashes(pares_hashes, textos_possiveis):
    for sha_arquivo, md5_arquivo in pares_hashes:
        encontrou = False
        for texto in textos_possiveis:
            sha_calc, md5_calc = calcular_hashes(texto)
            if sha_arquivo == sha_calc and md5_arquivo == md5_calc:
                print(f"Hash correspondente encontrado: '{texto}'")
                encontrou = True
                break
        if not encontrou:
            print(f"Nenhum conteúdo correspondente para:\nSHA256: {sha_arquivo}\nMD5: {md5_arquivo}\n")

# Caminho para o arquivo lab2.txt
caminho_arquivo = 'lab2.txt'

pares = carregar_hashes_do_arquivo(caminho_arquivo)
verificar_hashes(pares, possiveis_conteudos)