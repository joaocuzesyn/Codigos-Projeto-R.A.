#codigo feito com ajuda do Gemini e Chat GPT- Primeira versao da historia com escolhas(teste)

# Dicionário contendo os capítulos, textos descritivos e opções de escolha
CAPITULOS = {
    1: {
        "titulo": "Capítulo 1 — O Chamado",
        "texto": (
            "Às 03h17, seu terminal emite um alerta silencioso.\n"
            "Uma mensagem desconhecida aparece na tela:\n"
            "\"PHANTOM, eles apagaram os arquivos, mas esqueceram de apagar a verdade. "
            "O ORÁCULO não falhou. Você tem 72 horas. Não confie na NEXUS.\"\n\n"
            "O que você deseja fazer?"
        ),
        "opcoes": {
            1: "Investigar as coordenadas do antigo centro de dados enviado na mensagem.",
            2: "Tentar rastrear a origem da mensagem criptografada na rede.",
        },
        "proximo": {
            1: 2,  # Vai para o Capítulo/Cena 2
            2: 2,  # Por enquanto, ambos levam à cena seguinte para manter o fluxo
        }
    },
    2: {
        "titulo": "Capítulo 1 — O Centro de Dados",
        "texto": (
            "Você chega ao centro de dados abandonado. As portas estão abertas.\n"
            "No chão, pegadas recentes. Junto aos servidores centrais, "
            "você encontra Dante Moreau vasculhando os terminais de acesso."
        ),
        "opcoes": {
            1: "Confrontar Dante diretamente e exigir explicações.",
            2: "Observar escondido para descobrir o que ele procura nos arquivos.",
        },
        "proximo": {
            1: 3,
            2: 3,
        }
    }
}

def exibir_capitulo(numero_capitulo):
    """
    Exibe o título, o texto do capítulo atual e retorna as opções de escolha.
    """
    if numero_capitulo in CAPITULOS:
        cap = CAPITULOS[numero_capitulo]
        print(f"\n{'='*50}")
        print(f" {cap['titulo']} ")
        print(f"{'='*50}\n")
        print(cap["texto"])
        print("\nEscolhas disponíveis:")
        for chave, descricao in cap["opcoes"].items():
            print(f"[{chave}] {descricao}")
        return cap["opcoes"]
    else:
        print("\n[Fim da História] Você concluiu o conteúdo disponível desta versão.")
        return None

def processar_escolha(numero_capitulo, escolha):
    """
    Processa a escolha do jogador e retorna o próximo capítulo correspondente.
    """
    cap = CAPITULOS.get(numero_capitulo)
    if cap and escolha in cap["proximo"]:
        proximo_cap = cap["proximo"][escolha]
        return proximo_cap
    else:
        print("\n[Erro] Escolha inválida para este capítulo.")
        return numero_capitulo

#codigo retornado para o usuario
def main():
    """
    Função principal que controla o fluxo de execução do jogo.
    """
    capitulo_atual = 1
    
    while capitulo_atual in CAPITULOS:
        opcoes = exibir_capitulo(capitulo_atual)
        
        if opcoes is None:
            break
            
        try:
            escolha_usuario = int(input("\nDigite o número da sua escolha: "))
            capitulo_atual = processar_escolha(capitulo_atual, escolha_usuario)
        except ValueError:
            print("\n[Erro] Por favor, digite apenas um número válido correspondente à escolha.")

    # Exibe o encerramento se passar do último capítulo
    if capitulo_atual not in CAPITULOS:
        exibir_capitulo(capitulo_atual)

# Executa o jogo se o arquivo for rodado diretamente
if __name__ == "__main__":
    main()