# Mission Control AI

Sistema em Python para simular o monitoramento de uma missão espacial experimental. O programa gera uma matriz com ciclos da missão, analisa temperatura, comunicação, bateria, oxigênio e estabilidade, calcula risco operacional e exibe um relatório final no terminal.

Foi feita também uma simulação no TinkerCad em arduino que mostra como os sensores e alarmes iriam funcionar na realidade.

## Integrantes

- Mateus Felipe Curtale Serafim - RM: 571129
- Vinicius Sanches Chiarle - RM: 568846

## O Que O Projeto Faz

O Mission Control AI simula 6 ciclos de monitoramento de uma missão espacial. Cada ciclo representa um contexto diferente da operação, como início da missão, interferência de comunicação, alerta de energia, risco operacional e tentativa de recuperação.

O sistema usa regras em Python para calcular alertas, pontuação de risco, classificação do ciclo, tendência da missão e área mais afetada. Quando o Ollama está instalado, o modelo Llama também gera uma análise complementar com base nos dados calculados pelo programa.

## Estrutura Dos Dados

A matriz principal do projeto se chama `dados_missao`.

Cada linha representa um ciclo da missão. Cada ciclo segue esta ordem:

```python
[temperatura, comunicacao, bateria, oxigenio, estabilidade]
```

## Tecnologias

- Python 3
- Biblioteca `ollama` para a análise complementar com IA
- Modelo `llama3.2:1b`
- Arduino UNO
- Linguagem C++

# Como Executar:

## Execute a simulação no TinkerCad:
https://www.tinkercad.com/things/6th50dWSHvK-gsgrilo/editel?returnTo=https%3A%2F%2Fwww.tinkercad.com%2Fdashboard&sharecode=ntjodAMqM4D1GoqJDj9dHxeZYhR5VEK6xgiyfHjwIBU

# Execute o arquivo principal:

```powershell
python mission_control_ai.py
```

# Para habilitar a IA:

```powershell
python -m pip install ollama
ollama pull llama3.2:1b
```

## Link do código no colab
https://colab.research.google.com/drive/1HpElrFFEg97cOmT68rAu_-RQGcS9mcnJ?usp=sharing

OBS: Recomendo utilizar a execução com GPU no collab, o sistema é mais estável nessa configuração.

O programa também funciona sem IA. Nesse caso, ele exibe o relatório calculado pelas regras do Python e informa que a análise complementar não foi gerada.

## Demonstração

Prints da execução

<img src="https://github.com/MateusCurtale/control_missionIA/blob/main/Captura%20de%20tela%202026-06-04%20214219.png" alt="Print de execução 01">
<img src="https://github.com/MateusCurtale/control_missionIA/blob/main/Captura%20de%20tela%202026-06-04%20214326.png" alt="Print de execução 02">


## Vídeo

https://www.linkedin.com/posts/mateus-curtale-serafim_fiap-ia-globalsoution-ugcPost-7468869698475094016-InsQ/?utm_source=share&utm_medium=member_desktop&rcm=ACoAADv3OS8BEf8mAuZIKWob44tDC1KpXSghiKg
