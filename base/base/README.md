
As rotas estavam todas dentro do app.py.
A classe Produto estava dentro do app.py, mas deveria estar no models.py
O Blueprint de produtos foi criado, mas não estava sendo registrado no app.py
O código de busca dos produtos estava dentro da rota
O HTML dos detalhes do produto estava dentro do código Python
Estava faltando login em base.html

oq fiz: (ou tentei fazer)

O Model ficou no models.py, com a classe Produto, os produtos e as funções de busca
O Controller ficou separado nos Blueprints produtos e auth
O Blueprint produtos ficou com as rotas dos produtos
O Blueprint auth ficou com as rotas de login e logout
O url_for mudou porque as rotas agora estão dentro dos Blueprints
Antes: url_for("ver_produto")
Depois: url_for("produtos.ver_produto")
