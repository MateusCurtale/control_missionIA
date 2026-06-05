import ollama

# dados = [temperatura, comunicacao, bateria, oxigenio, estabilidade]
dados_missao = [
    [24, 92, 88, 96, 90],
    [27, 80, 72, 94, 85],
    [31, 65, 58, 91, 70],
    [36, 42, 38, 87, 55],
    [39, 28, 19, 78, 35],
    [34, 55, 32, 82, 50],
]

pontuacao_total = [0] * len(dados_missao)  # Inicializa a pontuação total para cada leitura
AREAS = ["Temperatura", "Comunicação", "Bateria", "Oxigênio", "Estabilidade"]

# Analisa a temperatura.
def analisar_temperatura(dados):

    print("\n=== ANÁLISE DE TEMPERATURA ===")
    
    # Percorre cada leitura de dados e avalia a temperatura, atribuindo pontuações conforme os critérios estabelecidos.
    for i, leitura in enumerate(dados):
        temperatura = leitura[0]
        if temperatura < 18:  # Atenção caso a temperatura esteja abaixo de 18°C
            print(f"CICLO {i+1}: ATENÇÃO: Temperatura BAIXA   ({temperatura} °C)")
            pontuacao_total[i] += 1

        elif temperatura > 30 and temperatura <= 35: # Atenção caso a temperatura esteja entre 30°C e 35°C
            print(f"CICLO {i+1}: ATENÇÃO: Temperatura ALTA ({temperatura} °C)")
            pontuacao_total[i] += 1

        elif temperatura > 35:  # Alerta crítico caso a temperatura esteja acima de 35°C
            print(f"CICLO {i+1}: ALERTA: Superaquecimento CRÍTICO ({temperatura} °C)")
            pontuacao_total[i] += 2

        else: # Temperatura normal
            print(f"CICLO {i+1}: Temperatura NORMAL ({temperatura} °C)")
            pontuacao_total[i] += 0

# Analisa a comunicação.
def analisar_comunicacao(dados):
    print("\n=== ANÁLISE DE COMUNICAÇÃO ===")

    for i, leitura in enumerate(dados):
        comunicacao = leitura[1]

        if comunicacao < 30:
            print(f"CICLO {i + 1}: ALERTA CRÍTICO: Comunicação FRACA ({comunicacao}%)")
            pontuacao_total[i] += 2
        elif comunicacao < 60:
            print(f"CICLO {i + 1}: ATENÇÃO: Comunicação MODERADA ({comunicacao}%)")
            pontuacao_total[i] += 1
        else:
            print(f"CICLO {i + 1}: Comunicação NORMAL ({comunicacao}%)")

# Analisa a bateria.
def analisar_bateria(dados):
    print("\n=== ANÁLISE DE BATERIA ===")

    for i, leitura in enumerate(dados):
        bateria = leitura[2]

        if bateria < 20:
            print(f"CICLO {i + 1}: ALERTA CRÍTICO: Bateria BAIXA ({bateria}%)")
            pontuacao_total[i] += 2
        elif bateria < 50:
            print(f"CICLO {i + 1}: ATENÇÃO: Bateria MODERADA ({bateria}%)")
            pontuacao_total[i] += 1
        else:
            print(f"CICLO {i + 1}: Bateria NORMAL ({bateria}%)")

# Analisa o nível de oxigênio.
def analisar_oxigenio(dados):
    print("\n=== ANÁLISE DE OXIGÊNIO ===")

    for i, leitura in enumerate(dados):
        oxigenio = leitura[3]

        if oxigenio < 80:
            print(f"CICLO {i + 1}: ALERTA CRÍTICO: Nível de Oxigênio BAIXO ({oxigenio}%)")
            pontuacao_total[i] += 2
        elif oxigenio < 90:
            print(f"CICLO {i + 1}: ATENÇÃO: Nível de Oxigênio MODERADO ({oxigenio}%)")
            pontuacao_total[i] += 1
        else:
            print(f"CICLO {i + 1}: Nível de Oxigênio NORMAL ({oxigenio}%)")

# Analisa a estabilidade do sistema.
def analisar_estabilidade(dados):
    print("\n=== ANÁLISE DE ESTABILIDADE ===")

    for i, leitura in enumerate(dados):
        estabilidade = leitura[4]

        if estabilidade < 40:
            print(f"CICLO {i + 1}: ALERTA CRÍTICO: Estabilidade FRACA ({estabilidade}%)")
            pontuacao_total[i] += 2
        elif estabilidade < 70:
            print(f"CICLO {i + 1}: ATENÇÃO: Estabilidade MODERADA ({estabilidade}%)")
            pontuacao_total[i] += 1
        else:
            print(f"CICLO {i + 1}: Estabilidade NORMAL ({estabilidade}%)")

# Classifica o ciclo com base na pontuação total, atribuindo categorias de "Normal", "Atenção" ou "Crítico".
def classificar_ciclo(pontuacao): 
    if pontuacao == 0:
        return "Normal"
    if pontuacao <= 2:
        return "Atenção"
    return "Crítico"

# Analisa a tendência da pontuação total ao longo dos ciclos para identificar se a situação está melhorando, piorando ou estável.
def analisar_tendencia(pontuacao_total):
    # Analisa a tendência da pontuação total ao longo dos ciclos.
    if len(pontuacao_total) < 2:
        return "Dados insuficientes para tendência"
    
    # Calcula as diferenças entre as pontuações de ciclos consecutivos para determinar a tendência geral.
    diffs = [pontuacao_total[i] - pontuacao_total[i - 1] for i in range(1, len(pontuacao_total))]
    if all(d == 0 for d in diffs):
        return "Estável"
    
    if all(d <= 0 for d in diffs) and any(d < 0 for d in diffs):
        return "Melhorando"
    
    if all(d >= 0 for d in diffs) and any(d > 0 for d in diffs):
        return "Piorando"
    
    else:
        return "Tendência instável"

# Identifica qual área (temperatura, comunicação, bateria, oxigênio ou estabilidade) está mais afetada com base na pontuação total acumulada para cada área ao longo dos ciclos.
def identificar_area_mais_afetada(dados):
    scores = [0] * len(AREAS)

    for leitura in dados:
        temperatura, comunicacao, bateria, oxigenio, estabilidade = leitura

        if temperatura < 18 or (30 < temperatura <= 35):
            scores[0] += 1
        elif temperatura > 35:
            scores[0] += 2

        if comunicacao < 30:
            scores[1] += 2
        elif comunicacao < 60:
            scores[1] += 1

        if bateria < 20:
            scores[2] += 2
        elif bateria < 50:
            scores[2] += 1

        if oxigenio < 80:
            scores[3] += 2
        elif oxigenio < 90:
            scores[3] += 1

        if estabilidade < 40:
            scores[4] += 2
        elif estabilidade < 70:
            scores[4] += 1

    max_score = max(scores)
    if max_score == 0:
        return "Nenhuma área afetada", 0

    return AREAS[scores.index(max_score)], max_score

# Gera uma recomendação final com base na pontuação total, na área mais afetada e na tendência geral da missão.
def gerar_recomendacao(pontuacao_total, area_afetada, tendencia):

    if tendencia == "Piorando":
        return f"Atenção urgente: revisar sistemas críticos, especialmente {area_afetada}."
    
    if tendencia == "Melhorando":
        return f"Continuar monitoramento e manter foco em {area_afetada}."
    
    if tendencia == "Tendência instável":
        return "Monitorar todas as variáveis de perto e validar as leituras do próximo ciclo."
    
    return "Manter vigilância e seguir os protocolos de missão."

# Gera recomendações específicas para cada ciclo com base na pontuação total e nos problemas identificados em cada área, fornecendo orientações claras para a equipe de controle da missão.
def gerar_recomendacoes_por_ciclo(dados, pontuacao_total):
    recomendacoes = []

    for i, leitura in enumerate(dados):
        temperatura, comunicacao, bateria, oxigenio, estabilidade = leitura
        classificacao = classificar_ciclo(pontuacao_total[i])
        problemas = []

        if temperatura < 18:
            problemas.append("temperatura baixa")

        elif temperatura > 35:
            problemas.append("superaquecimento")

        elif temperatura > 30:
            problemas.append("temperatura alta")

        if comunicacao < 30:
            problemas.append("comunicação fraca")
        elif comunicacao < 60:
            problemas.append("comunicação moderada")

        if bateria < 20:
            problemas.append("bateria baixa")

        elif bateria < 50:
            problemas.append("bateria moderada")

        if oxigenio < 80:
            problemas.append("oxigênio crítico")

        elif oxigenio < 90:
            problemas.append("oxigênio moderado")

        if estabilidade < 40:
            problemas.append("estabilidade fraca")

        elif estabilidade < 70:
            problemas.append("estabilidade moderada")

        if classificacao == "Normal":
            recomendacao = f"Ciclo {i+1} : manter monitoramento regular e garantir estabilidade dos sistemas."

        else:
            descricao_problemas = " e ".join(problemas) if problemas else "sinais de alerta"
            recomendacao = f"Ciclo {i+1} ({classificacao}): revisar {descricao_problemas}."

            if classificacao == "Crítico":
                recomendacao += " Ação imediata recomendada."

            else:
                recomendacao += " Atenção e acompanhamento no próximo ciclo."

        recomendacoes.append(recomendacao)

    return recomendacoes

# Gera um relatório final consolidando as análises, classificações, tendências e recomendações para a equipe de controle da missão, apresentando uma visão clara e estruturada dos resultados.
def gerar_relatorio_final(classificacoes, pontuacoes, tendencia, area_afetada, recomendacoes_por_ciclo, recomendacao):
    linhas = [
        "=== RELATÓRIO FINAL DA MISSÃO ===",
        f"Tendência geral: {tendencia}",
        f"Área mais afetada: {area_afetada}",
        "",
        "Relatório por ciclo:",
    ]

    classificacao_texto = {
        "Normal": "MISSÃO NORMAL",
        "Atenção": "MISSÃO EM ATENÇÃO",
        "Crítico": "MISSÃO CRÍTICA",
    }

    for indice, (classificacao, pontuacao, recomendacao_ciclo) in enumerate(
        zip(classificacoes, pontuacoes, recomendacoes_por_ciclo), start=1
    ):
        texto_classe = classificacao_texto.get(classificacao, classificacao.upper())
        linhas.append(f"Ciclo {indice}:")
        linhas.append(f"  Pontuação de risco do ciclo: {pontuacao}")
        linhas.append(f"  Classificação do ciclo: {texto_classe}")
        linhas.append(f"  Recomendação: {recomendacao_ciclo}")
        linhas.append("")

    linhas.append("Recomendação geral:")
    linhas.append(f"  {recomendacao}")
    linhas.append("")
    return "\n".join(linhas)

# Exibe os resultados da análise, incluindo classificações, tendências, áreas afetadas e recomendações, em um formato estruturado e fácil de entender para a equipe de controle da missão.
def exibir_resultados():
    classificacoes = [classificar_ciclo(p) for p in pontuacao_total]
    tendencia = analisar_tendencia(pontuacao_total)
    area_afetada, _ = identificar_area_mais_afetada(dados_missao)
    recomendacoes_por_ciclo = gerar_recomendacoes_por_ciclo(dados_missao, pontuacao_total)

    recomendacao = gerar_recomendacao(pontuacao_total, area_afetada, tendencia)

    return gerar_relatorio_final(
        classificacoes,
        pontuacao_total,
        tendencia,
        area_afetada,
        recomendacoes_por_ciclo,
        recomendacao,
    )


# Executa a análise completa dos dados da missão, gerando um relatório final e utilizando o modelo de linguagem para fornecer um resumo das conclusões e recomendações para a equipe de controle da missão.
def executar_analise():
    analisar_temperatura(dados_missao)
    analisar_comunicacao(dados_missao)
    analisar_bateria(dados_missao)
    analisar_oxigenio(dados_missao)
    analisar_estabilidade(dados_missao)

    relatorio = exibir_resultados()
    print()
    print(relatorio)

    resposta = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "system",
                "content": "Você é um assistente de análise de dados de missão espacial chamado Helper 001.",
            },
            {
                "role": "user",
                "content": (
                    f"Analise os seguintes dados da missão: {relatorio} "
                    "e forneça um resumo das principais conclusões e recomendações para a equipe de controle da missão."
                ),
            },
        ],
    )

    print("\n=== RELATÓRIO DO HELPER 001 ===")
    print(resposta.get('message', {}).get('content', 'Sem resposta do modelo.'))

if __name__ == "__main__":
    executar_analise()
