import sqlite3


def init():
    con = sqlite3.connect("planos.db")
    return con

def criar(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS movie(name, duracao,video, descricao,link, planos)")

def inserir(cur,nome, duracao, imagem, descricao, link,plano):
    query = 'INSERT INTO planos(nome, duracao, imagem, descricao, link, plano)  VALUES(?,?,?,?,?,?)'
    cur.execute(query,(nome, duracao, imagem, descricao, link,plano))
    

def dados():
    name = input('nome do exercicio: ')
    duracao = input('qual a duração do video: ')
    video = input('o nome do video: ')
    descricao = input('breve descricao do video: ')
    #autor = input('Exercico de: ')
    link = input('link para o video de exemplo: ')
    plano = input('plano de: ')
    return (name,duracao,video,descricao,link,plano)

def atualizar(cur,name = None,duracao = None,video = None,descricao = None,link = None,plano = None):
    cur.execute("SELECT name, FROM planos ORDER BY year")
    pass

def apagar(cur, nome,plano):
    query = 'DELETE FROM planos WHERE nome == %s and plano == %s'&(nome, plano) 
    cur.execute(query)

def get(cur,nome,plano):
    query = 'SELECT FROM planos WHERE nome == %s and plano == %s'%(nome, plano) 
    exer = cur.execute(query)
    #print(exer) 
    show(exer)
def getAll(cur,plano):
    query = 'SELECT FROM planos WHERE plano == %s'% plano
    exer = cur.execute(query)
    show(exer)

def show(exer):
    print(exer)


def main():


    con = init()
    cur = con.cursor()
    #criar(cur)
    op = input('menu:\n1-Inserir dados\n2-Atualizar\n3-Apagar\n4-Buscar\n')
    op = int(op)
    if op == 1:
        nome,duracao,video,descricao,link,plano = dados()
        inserir(cur ,nome,duracao,video,descricao,link,plano)
        con.commit()
    elif op == 2:
        atualizar()
    elif op == 3:
        nome = input('nome do exercicio: ')
        plano = input('plano de: ')
        apagar(cur,nome,plano)
        con.commit()
    elif op == 4:
        opr =input('1-ver apenas um exercício\n2-ver o plano completo\n')
        opr = int(opr)
        if opr == 1:
            nome = input('nome do exercicio: ')
            plano = input('plano de: ')
            get(plano= plano, nome= nome)
        elif opr == 2:
            plano = input('plano de: ')
            getAll(plano)

    

if __name__ == '__main__':
    main()