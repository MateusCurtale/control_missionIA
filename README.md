# Mission Control AI

Sistema em Python para simular o monitoramento de uma missão espacial experimental. O programa gera uma matriz com ciclos da missão, analisa temperatura, comunicação, bateria, oxigênio e estabilidade, calcula risco operacional e exibe um relatório final no terminal.

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

## Como Executar

Execute o arquivo principal:

```powershell
python mission_control_ai.py
```

Para habilitar a IA:

```powershell
python -m pip install ollama
ollama pull llama3.2:1b
```

O programa também funciona sem IA. Nesse caso, ele exibe o relatório calculado pelas regras do Python e informa que a análise complementar não foi gerada.

## Demonstração

Prints da execução
```markdown
<img width="1880" height="867" alt="Captura de tela 2026-06-04 214219" src="https://github.com/user-attachments/assets/d8ab4d3c-d6b8-4828-ac7b-f198d19c329e" />
<img width="1915" height="872" alt="Captura de tela 2026-06-04 214326" src="https://github.com/user-attachments/assets/c3e1fc53-cc46-463b-ac78-6b303bb55791" />

```

## Vídeo

[Assistir ao vídeo de demonstração](https://link-do-video.com)
