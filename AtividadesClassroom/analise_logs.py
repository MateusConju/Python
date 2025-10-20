def analisar_logs(logs):
    """Analisa logs de API e retorna métricas"""
    from collections import Counter

    # Contadores
    contador_metodos = Counter()
    contador_endpoints = Counter()
    contador_usuarios = Counter()
    total_erros = 0

    # Gerador: processa linha a linha (eficiente)
    for linha in (l.strip() for l in logs if l.strip()):
        timestamp, metodo, endpoint, status, tempo, user_id = linha.split("|")

        contador_metodos[metodo] += 1
        contador_endpoints[endpoint] += 1
        contador_usuarios[user_id] += 1

        if int(status) >= 400:
            total_erros += 1

    # Monta o dicionário de métricas
    metricas = {
        "total_requisicoes": sum(contador_metodos.values()),
        "por_metodo": dict(contador_metodos),
        "total_erros": total_erros,
        "endpoint_mais_acessado": contador_endpoints.most_common(1)[0][0] if contador_endpoints else None,
        "usuario_mais_ativo": contador_usuarios.most_common(1)[0][0] if contador_usuarios else None
    }

    return metricas

logs = [ 
 "2024-10-11 10:23:45|GET|/api/products/123|200|150ms|user_456", 
 "2024-10-11 10:23:46|POST|/api/orders|201|300ms|user_789", 
 "2024-10-11 10:23:47|GET|/api/products/456|404|50ms|user_456",
 "2024-10-11 10:23:48|GET|/api/users/789|200|100ms|user_123", 
 "2024-10-11 10:23:49|DELETE|/api/orders/999|500|500ms|user_789", 
]

resultado = analisar_logs(logs)
print(resultado)
