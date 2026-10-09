# ENGENHARIA DE PROMPTS - System prompt vs User prompt

# Zero-Shot: pedir a execução de uma tarefa sem nenhum exemplo prévio

# Few-Shot: fornecemos ao modelo alguns exmeplos minimos de referencias com o objetivo de demosntar o que esperamos como saida 

# Chain-of-Thought(cadeia de pensamento): instruir o modelo a explicitar o raciocinio passo-a-passo; esta abordagem melhora drasticamente a resposta e saida desejadas.

# 1. importar os recursos necessarios
import json

# 2. definir o padrão few-shot
prompt_few_shot = """ Voce é um analista financiero. determine se a trasnsação é suspeita. Pense passo a passo.
Exemplo 1:
Transação: R$ 50,00 no supermercado do bairro às 11:30.
Raciocinio: O valor é baixo, o local é comum e o horário é comercial
Resultado("suspeita": false, "risco": "Baixo")

Exemplo 2:
Transação: R$ 58.000,00 gastos numa loja de joias as 03:00 da manhã numa outra cidade.
Raciocinio: Valor muito elevado. Horario incomum e localização geografica diferente.
Resultado: {"suspeita": true, "risco": "Alto"}

--- TAREFA ---
Transação: R$ 12.000,00 em eletronicos às 02h15min.
Raciocinio:
"""
# simulçao do comportamento do LLM
def simular_execucao_cot(prompt: str) -> str:
    raciocinio_gerado = 'O valor de R$ 12.000,00 em eletronicos é elevado e o horario é muito estranho'
    resultado_gerado = '{"suspeita": true, "risco": Alto}'

    return f"{raciocinio_gerado}\nResultado: {resultado_gerado}"



print('====== PROMPT FEW-SHOT + CHAIN OF TOUGHT')
print(prompt_few_shot)

# exibição da resposta simulada da tarefa
print(simular_execucao_cot(prompt_few_shot))
# ---------------------------------------------------------


# 3. Modelo/Template de prompt para saida Json **** Estrita (Técnico)
def criar_prompt_extracao_json(texto_bruto: str) -> str:
    schema = {
        "nome_cliente": "string",
        "produto_mencionado": "string",
        "nivel_insatisfeito" : "int(1 a 5)"
    }

    prompt = f""" Extraia as informações  do texto do cliente e responda APENAS com um objeto JSON valido seguindo este esquema:
    {json.dumps(schema,indent=2)}
    
    Não inclua textos explicativos adicionais nem marcações de código markdown além do json

    Texto do cliente:
    "{texto_bruto}"
    """
    return prompt


# simulação do comportamento do LLM para a extração JSON
def simular_extracao_json(texto_bruto: str) -> str:
    dados = {
        "nome_cliente": "Jhony",
        "produto_mencionado": "notebook modelo 100X",
        "nivel_insatisfacao": 5
    }
    return json.dumps(dados, indent=2)

# fora da função uma nova var
texto_exemplo = 'Olá, meu nome é Jhony, Comprei o notebook modelo X100 e a tela veio danificada! Nota 5 de insatisfação'

print("\n=== PROMPT PARA A SAIDA ESTRUTURADA (JSON) ===")
print(criar_prompt_extracao_json(texto_exemplo))

print("\n=== RESPOSTA SIMULADA DO MODELO (JSON) ===")
json_resposta = simular_extracao_json(texto_exemplo)

# opção: convertendo o JSON para um dicionario python
dados_python = json.loads(json_resposta)
print(f'\n[Acesso Python] Cliente: {dados_python['nome_cliente']} | Insatisfação: {dados_python['nivel_insatisfacao']}')


