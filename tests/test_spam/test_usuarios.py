def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome = 'Pablo')
    sessao.salvar()
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()

def test_listar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome = 'Pablo'), Usuario(nome = 'Guilherme')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuario==sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()