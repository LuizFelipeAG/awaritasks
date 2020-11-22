# 1 - imports
from selenium import webdriver
from time import sleep

# 2 - parametros
URL_LINKEDIN_DS = 'https://br.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas?position=1&pageNum=0'


# 3- execucao do codigo
if __name__ == '__main__':
    # Criar uma instancia do Google Chrome pelo Selenium
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    # Acessar URL do LinkedIn
    driver.get(URL_LINKEDIN_DS)

    # pegar lista de resultados de vagas
    resultados = driver.find_elements_by_class_name('result-card')
    lista_descricoes = []
    
    # iniciar While Loop em cima de todos os resultados
    while True:
        # For loop para coletar descricoes de dados
        for r in resultados[len(lista_descricoes):]:
            r.click() # clicar na descricao
            sleep(2)
            try:             
                # pegar elemento com a descricao
                descricao = driver.find_element_by_class_name('description')
                # anexar o texto na lista_descricoes
                lista_descricoes.append(descricao.text)
            except:
                print('Erro')
                pass 
    
        resultados = driver.find_elements_by_class_name('result-card') 
               
        # Criterio de saida do While
        if len(lista_descricoes) == len(resultados):
            break

    # Salvar descricoes de vagas
    descricao_salvar = '\n'.join(lista_descricoes)
    with open('descricoes_vagas.txt', 'w', encoding='utf-8') as f:
        f.write(descricao_salvar)

    # Fechar o Google Chrome        
    driver.quit()