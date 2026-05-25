MISSAO = "Odyssey Prime"
EQUIPE = "Alvinegro Force"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicacao com a base",
    "Sistema de energia",
    "Suporte de oxigenio",
    "Estabilidade operacional",
]

dados_missao = [
    [25, 94, 90, 97, 91],
    [28, 82, 75, 95, 86],
    [31, 68, 61, 92, 73],
    [36, 45, 42, 88, 58],
    [38, 27, 18, 79, 37],
    [34, 57, 36, 83, 52],
]

PONTOS_CLASSIFICACAO = {
    "NORMAL": 0,
    "ATENCAO": 1,
    "CRITICO": 2,
}


def analisar_temperatura(valor):
    if valor < 18:
        return "ATENCAO", "Temperatura abaixo do ideal"
    if valor <= 30:
        return "NORMAL", "Temperatura estavel"
    if valor <= 35:
        return "ATENCAO", "Temperatura elevada"
    return "CRITICO", "Risco de superaquecimento"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRITICO", "Comunicacao com a base em nivel critico"
    if valor <= 59:
        return "ATENCAO", "Comunicacao instavel"
    return "NORMAL", "Comunicacao estavel"


def analisar_bateria(valor):
    if valor < 20:
        return "CRITICO", "Bateria em nivel critico"
    if valor <= 49:
        return "ATENCAO", "Bateria abaixo do recomendado"
    return "NORMAL", "Energia estavel"


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRITICO", "Oxigenio em nivel critico"
    if valor <= 89:
        return "ATENCAO", "Oxigenio abaixo do ideal"
    return "NORMAL", "Oxigenio adequado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRITICO", "Estabilidade operacional critica"
    if valor <= 69:
        return "ATENCAO", "Estabilidade operacional reduzida"
    return "NORMAL", "Estabilidade operacional adequada"


def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSAO ESTAVEL"
    if pontuacao <= 5:
        return "MISSAO EM ATENCAO"
    return "MISSAO CRITICA"


def analisar_tendencia(risco_primeiro, risco_ultimo):
    if risco_ultimo > risco_primeiro:
        return "A missao apresentou tendencia de piora."
    if risco_ultimo < risco_primeiro:
        return "A missao apresentou tendencia de melhora."
    return "A missao permaneceu estavel em relacao ao inicio."


def gerar_recomendacao(classificacoes_ciclo):
    if "CRITICO" in classificacoes_ciclo:
        acoes_criticas = []
        if classificacoes_ciclo[0] == "CRITICO":
            acoes_criticas.append("controle termico")
        if classificacoes_ciclo[1] == "CRITICO":
            acoes_criticas.append("comunicacao")
        if classificacoes_ciclo[2] == "CRITICO":
            acoes_criticas.append("energia")
        if classificacoes_ciclo[3] == "CRITICO":
            acoes_criticas.append("suporte a vida")
        if classificacoes_ciclo[4] == "CRITICO":
            acoes_criticas.append("estabilidade operacional")

        if len(acoes_criticas) >= 3:
            return (
                "Ativar modo de seguranca e priorizar "
                + ", ".join(acoes_criticas)
                + "."
            )
        return "Verificar sistemas criticos: " + ", ".join(acoes_criticas) + "."
    if "ATENCAO" in classificacoes_ciclo:
        return "Monitorar sistemas em atencao e preparar plano de contingencia."
    return "Manter operacao normal e continuar monitoramento."


def identificar_area_mais_afetada(pontos_por_area):
    maior_pontuacao = max(pontos_por_area)
    indice = pontos_por_area.index(maior_pontuacao)
    return areas_monitoradas[indice], maior_pontuacao


def gerar_relatorio_final(resumo):
    print("=" * 60)
    print("RELATORIO FINAL DA MISSAO")
    print("=" * 60)
    print(f"Missao: {MISSAO}")
    print(f"Equipe: {EQUIPE}")
    print()
    print(f"Quantidade de ciclos analisados: {resumo['total_ciclos']}")
    print()
    print(f"Media de temperatura: {resumo['media_temperatura']:.2f} C")
    print(f"Media de comunicacao: {resumo['media_comunicacao']:.2f}%")
    print(f"Media de bateria: {resumo['media_bateria']:.2f}%")
    print(f"Media de oxigenio: {resumo['media_oxigenio']:.2f}%")
    print(f"Media de estabilidade: {resumo['media_estabilidade']:.2f}%")
    print()
    print(f"Ciclo mais critico: Ciclo {resumo['ciclo_mais_critico']}")
    print(f"Maior pontuacao de risco: {resumo['maior_risco']}")
    print(f"Risco medio da missao: {resumo['risco_medio']:.2f}")
    print(f"Quantidade de ciclos criticos: {resumo['ciclos_criticos']}")
    print()
    print("Tendencia da missao:")
    print(resumo["tendencia"])
    print()
    print("Pontuacao acumulada por area:")
    for area, pontos in zip(areas_monitoradas, resumo["pontos_por_area"]):
        print(f"{area}: {pontos} pontos")
    print()
    print("Area mais afetada:")
    print(resumo["area_mais_afetada"])
    print()
    print("Classificacao final da missao:")
    print(resumo["classificacao_final"])
    print()
    print("Conclusao:")
    print(resumo["conclusao"])


def executar_missao():
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missao: {MISSAO}")
    print(f"Equipe: {EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)
    print()

    soma_temperatura = 0
    soma_comunicacao = 0
    soma_bateria = 0
    soma_oxigenio = 0
    soma_estabilidade = 0

    riscos_por_ciclo = []
    pontos_por_area = [0, 0, 0, 0, 0]
    ciclos_criticos = 0

    for indice, ciclo in enumerate(dados_missao, start=1):
        temperatura, comunicacao, bateria, oxigenio, estabilidade = ciclo

        analises = [
            analisar_temperatura(temperatura),
            analisar_comunicacao(comunicacao),
            analisar_bateria(bateria),
            analisar_oxigenio(oxigenio),
            analisar_estabilidade(estabilidade),
        ]

        classificacoes = [resultado[0] for resultado in analises]
        pontuacao_ciclo = 0
        for i, classificacao in enumerate(classificacoes):
            pontos = PONTOS_CLASSIFICACAO[classificacao]
            pontuacao_ciclo += pontos
            pontos_por_area[i] += pontos

        classificacao_ciclo = classificar_ciclo(pontuacao_ciclo)
        if classificacao_ciclo == "MISSAO CRITICA":
            ciclos_criticos += 1

        recomendacao = gerar_recomendacao(classificacoes)
        riscos_por_ciclo.append(pontuacao_ciclo)

        soma_temperatura += temperatura
        soma_comunicacao += comunicacao
        soma_bateria += bateria
        soma_oxigenio += oxigenio
        soma_estabilidade += estabilidade

        print(f"CICLO {indice}")
        print("-" * 60)
        print(
            f"Temperatura: {temperatura} C | {analises[0][0]} | {analises[0][1]}"
        )
        print(
            f"Comunicacao: {comunicacao}% | {analises[1][0]} | {analises[1][1]}"
        )
        print(f"Bateria: {bateria}% | {analises[2][0]} | {analises[2][1]}")
        print(f"Oxigenio: {oxigenio}% | {analises[3][0]} | {analises[3][1]}")
        print(
            f"Estabilidade: {estabilidade}% | {analises[4][0]} | {analises[4][1]}"
        )
        print()
        print(f"Pontuacao de risco do ciclo: {pontuacao_ciclo}")
        print(f"Classificacao do ciclo: {classificacao_ciclo}")
        print(f"Recomendacao: {recomendacao}")
        print()

    total_ciclos = len(dados_missao)
    maior_risco = max(riscos_por_ciclo)
    ciclo_mais_critico = riscos_por_ciclo.index(maior_risco) + 1
    risco_medio = sum(riscos_por_ciclo) / total_ciclos
    tendencia = analisar_tendencia(riscos_por_ciclo[0], riscos_por_ciclo[-1])
    area_mais_afetada, _ = identificar_area_mais_afetada(pontos_por_area)

    classificacao_final = classificar_ciclo(round(risco_medio))
    if "piora" in tendencia or ciclos_criticos > 0:
        conclusao = (
            "A missao apresentou instabilidade relevante. "
            "Manter contingencia ativa e reforcar monitoramento."
        )
    else:
        conclusao = (
            "A missao permaneceu controlada durante os ciclos analisados."
        )

    resumo = {
        "total_ciclos": total_ciclos,
        "media_temperatura": soma_temperatura / total_ciclos,
        "media_comunicacao": soma_comunicacao / total_ciclos,
        "media_bateria": soma_bateria / total_ciclos,
        "media_oxigenio": soma_oxigenio / total_ciclos,
        "media_estabilidade": soma_estabilidade / total_ciclos,
        "ciclo_mais_critico": ciclo_mais_critico,
        "maior_risco": maior_risco,
        "risco_medio": risco_medio,
        "ciclos_criticos": ciclos_criticos,
        "tendencia": tendencia,
        "pontos_por_area": pontos_por_area,
        "area_mais_afetada": area_mais_afetada,
        "classificacao_final": classificacao_final,
        "conclusao": conclusao,
    }

    gerar_relatorio_final(resumo)


if __name__ == "__main__":
    executar_missao()

