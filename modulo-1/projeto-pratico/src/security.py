# arquivo/modulo de segurança e conformidade com LGPD

import hashlib # lib/modulo/biblioteca nativo python usado, principalmente, para o acesso a funções de criptografica; por exemplo, esta recurso nos oferece algoritmos como: SHA-256, MD5 -> utilizados para criar assinaturas unicas en irreversiveis para dados criptografodos

from cryptography.fernet import Fernet # Fernet, é uma classe do pacote criptogrhapy; esta classe nos da possibilidade de implementar criptografia simétrica(significa que: a mesma chave usada para criptografar deve ser usada para descriptografar algum dado)

CHAVE_MESTRA = b'8P_xR-4W5-0-aD1sP_m0K8G3y_L4Q1s2D3f4G5h6J7k='# aqui, temos a definição da CHAVE SIMPÉTRICA global - no formato de bytes(o uso dom prefixo 'b' - nos da esta informação ). É importante observamos que esta chave precisa, necessariamente, ser no formato de Base64 de 32 bytes - isso é necessario para o pleno funcionamento da classe Fernet. Aqui, temos o segredo do funcionamento de criptografia e descriptografia de dados reversiveis.

# esta função tornar o dado de cpf do cliente/usuario anonimo; significa que: uma vez criptogrado, não será possivel descriptografar, ou seja, uma vez que "escondermos" o cpf não será possivel lê-lo novamente.
def anonimizar_cpf(cpf: str) -> str:
    if not cpf: # verificação se o parametro cpf está vazio; se estiver o retorno é None; 
        return None
    return hashlib.sha256(cpf.strip().encode('utf-8')).hexdigest() # e se não estiver vazio: 
'''
    a) cpf.strip(): aqui, estamos removendo possiveis "SUJEIRAS" DOS DADOS OBTIDOS; fazendo da função strip() que remove espaços em branco 

    b) encode('utf-8'): aqui, estamos aplicando um processo simples de conversão da strign cpf num objeto de nytes nop formato UTF-8 - esta é um recurso necessario para o funcionamento de hashlib

    c) hashlib.sha256(..): aqui, estmaos passando os bytes para o algoritmo de criptografia SHA-256, dessa forma podemos gerar o hash

    d) hexdigest(): aqui, aplicamos, a partir da função, a conversão do hash numa string de texto - no formato hexdecimal(64 caracteres); assim , nossa função pode retornar a string desejada.
'''
# aqui, estamos, tambem, criptografando o emial do usuario/cliente; mas, com o uso da função decode() podemos descriptografa-lo e ler o email inserido no sistema.
def criptografar_email(email: str) -> str:
    if not email: # verificação se o parametro email está vazio; se estiver o retorno é None; 
        return None
    cipher = Fernet(CHAVE_MESTRA) # aqui, temos uma instancia - a partir da classe Fernet; portanto, temos o objeto cypher sendo composto pela constante CHAVE_MESTRA; dessa forma o objeto cypher será usado para operações de criptografia.


    
    '''
    email.encode('utf-8'): aqui, estamos aplicando um processo simples de conversão da string email num objeto de bytes no formato UTF-8 - esta é um recurso necessario para o funcionamento de hashlib

    cipher.encrypt(..): aqui, temos a criptografia dos bytes do email usando a chave -Fernet 

    decode('utf-8'): aqui, temos a função de conversão dos bytes criptografados de volta para uma string de texto legivel para que seja possivel facilitar o armazenamento.
    '''
    return cipher.encrypt(email.encode('utf-8')).decode('utf-8')
