# 1. importando recursos
import tiktoken

# 2. definir uma var para receber como valor o procedimento de tokenização 
encoder = tiktoken.get_encoding('cl100k_base')
# acima, esta o encoder usado pleo GPT-4

# 3. definir uma nova var para receber como valor um determinado texto
texto = 'Engenharia de Prompts e, tambem, RAGs são dois dos principais pilares da IA Generativa'

tokens = encoder.encode(texto)

# 4. exibir o resultado do processo de tokenização
print('====== TOKENIZAÇÃO ======')
print(f'Texto original: {texto}')
print(f'Quantidade de tokens: {len(tokens)}')
print(f'IDs dos tokens: {tokens}')
print(f'Tokens decodificados individualmente:')

# loop for para iterar sobre cada token
for t in tokens:
    print(f"  ID{t} -> '{encoder.decode([t])}'")

# 5. Definir uma simulação de Grounding (Ancoragem) - com o objetivo de previnir a "alucinação"
def responder_com_grounding(pergunta: str, documento_contexto: str) -> str:
    prompt_grounding = f""" Você é um assistente estritamente factual. Portanto, responda a pergunta baseando-se EXCLUSIVAMENTE no contexto fornecido abaixo. 
    Se a informação não estiver contida no contexto, responda: "Não possuo informações suficientes para responder" 
    
    --- CONTEXTO ---
    {documento_contexto}

    --- PERGUNTA ---
    {pergunta}
    """

    # agora, temos de definira logica de resposta do modelo
    termo_busca = 'faturamento'

    # verificar se este termo compõe o contexto
    if termo_busca in documento_contexto.lower():
        #se a informação estvier dentro do contexto, extraimos aqui
        resposta = 'O faturamento foi encontrado no contexto'

    else:
        resposta = 'Não possuo informações suficientes para responder'


    return prompt_grounding, resposta

# definir as vars para receber como valor o "dialogo"

contexto_empresa = 'A empresa TechCorp foi fundada em 2018 e atua no setor de computação quântica'
pergunta_usuario = 'Qual é o faturamentro da TechCorp em 2025?'

prompt, resposta_da_regra = responder_com_grounding(pergunta_usuario, contexto_empresa)

print('=== PROMPT GROUNDING (INSTRUÇÃO) ===')
print(prompt)

print('=== RESPOSTA DA REGRA DE NEGOCIO ===')
print(resposta_da_regra)

