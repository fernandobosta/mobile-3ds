# Definição das variáveis (exemplos de valores para teste)
bateria_atual = 10
bola_em_jogo = True

# Processamento das condições (If / Elif / Else)
if bateria_atual < 15 and bola_em_jogo:
    print("ALERTA MÁXIMO: Bateria baixa! Substitua a bola na próxima paralisação.")

elif bateria_atual < 15 and not bola_em_jogo:
    print("Aviso: Bateria baixa. Aproveite a bola parada para trocá-la.")

else:
    print("Sistema Trionda operando normalmente. Bateria ok.")
