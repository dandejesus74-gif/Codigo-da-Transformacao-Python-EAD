import requests

def buscar_filme(nome_filme, api_key):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={nome_filme}&language=pt-PT"
    
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        
        dados = resposta.json()
        resultados = dados.get("results", [])
        
        if not resultados:
            print("Nenhum filme encontrado.")
            return
        
        filme = resultados[0]
        titulo = filme.get("title")
        sinopse = filme.get("overview", "Sinopse não disponível.")
        
        print(f"Título: {titulo}")
        print(f"Sinopse: {sinopse}")

    except requests.exceptions.RequestException as erro:
        print(f"Erro na requisição: {erro}")

# Exemplo de utilização:
API_KEY_TMDB = "SUA_CHAVE_TMDB_AQUI"
buscar_filme("Inception", API_KEY_TMDB)