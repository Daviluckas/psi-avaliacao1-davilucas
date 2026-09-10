from flask import render_template, request
from blueprints.produtos import produtos_bp
import models


@produtos_bp.route("/")
def index():
    q = request.args.get("q", "")

    if q:
        produtos = models.buscar_por_nome(q)
    else:
        produtos = models.produtos

    return render_template(
        "produtos/index.html",
        produtos=produtos,
        q=q,
        categorias=models.todas_categorias()
    )


@produtos_bp.route("/produto/<int:produto_id>")
def ver_produto(produto_id):
    produto = models.buscar_produto(produto_id)

    if produto is None:
        return "Produto não encontrado", 404

    return render_template("produtos/index.html",produtos=[produto],q="")
