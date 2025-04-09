import sys
import random
from Memoria import MemoriaPrincipal
from Memoria import MemoriaSecundaria
from Memoria import testaMapeamento

# Parametros:
#    memoriaPrincipal: memoria Cache, a pagina solicitada deve estar na memoriaPrincipal
#    memoriaSecundaria: memoria secundaria que possui todas as paginas
#    endereco: endereco da pagina requisitada
# Retorno
#    endereco que a pagina requisitada se encontra na memoriaPrincipal
# Altere a funcao para fazer uso de todos enderecos na memoria principal
#    tente otimizar o seu mecanismo de mapeamento
#    tente otimizar o seu mecanismo de substituicao
def mapeamentoCustomizado(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria, endereco: int) -> int:
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas
    tamanhoPagina = 4  # 4 bytes por página

    # Calcula o número da pagina na memoria secundaria
    page_num = endereco // tamanhoPagina
    
    # Mapeamento direto, sem estatísticas de uso (LRU tracking)
    cache_offset = page_num % qtPaginasMemoriaPrincipal
    
    # Dados da memoria secundária
    data = memoriaSecundaria.getPagina(page_num)
    
    # Checa se os dados já estâo em cache
    if memoriaPrincipal.getPagina(cache_offset) != data:
        memoriaPrincipal.setPagina(data, cache_offset)
    
    return cache_offset

#Utilize esta funcao caso precise inicializar alguma variavel para o mapeamento =)
def inicializaMapeamento(memoriaPrincipal: MemoriaPrincipal, memoriaSecundaria: MemoriaSecundaria):
    #quantidade de paginas em cada memoria =)
    qtPaginasMemoriaPrincipal = memoriaPrincipal.qtPaginas
    qtPaginasMemoriaSecundaria = memoriaSecundaria.qtPaginas


if __name__ == '__main__':

    #executa funcao de mapeamento com 20 enderecos em modo Debug
    testaMapeamento(nEnderecos=20, 
                               nPaginasMemoriaPrincipal=8, 
                               nPaginasMemoriaSecundaria=16, 
                               debug=True, 
                               funcaoMapeamento=mapeamentoCustomizado,
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

    #executa a funcao sem modo debug
    testaMapeamento(nEnderecos=300, 
                               nPaginasMemoriaPrincipal=128, 
                               nPaginasMemoriaSecundaria=512, 
                               debug=False, 
                               funcaoMapeamento=mapeamentoCustomizado, 
                               funcaoInicializacaoMapeamento=inicializaMapeamento)

