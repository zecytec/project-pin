from pathlib import Path
from runpy import run_path
from fakepinterest import app

caminho_banco = Path('instance/comunidade.db')

if not caminho_banco.exists():
    print('criando db')
    run_path('criar_banco.py')

if __name__ == '__main__':
    app.run(debug=True)

    