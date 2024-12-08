#!/bin/bash
# A instrução acima indica ao sistema operacional que o script deve ser interpretado usando o Bash.
# Ela é chamada de Shebang.
echo "Programa iniciado..."

# As permissões da calculadora são alteradas.
# 7 = Read (4) + Write (2) + Execute (1) = 7 para usuário.
# 4 = Read (4) para grupo.
# 4 = Read (4) para outros.
echo "Atribuindo permissões 744 para programa de calculadora..."
sudo chmod 744 calculadora.py

# Garante que python esteja instalado para execução.
# Sem isso Python pode não estar instalado, levando a um erro.
echo "Garantindo ambiente Python para execução de programa..."
sudo apt install python3

# Executa programa de calculadora.
echo "Executando programa de calculadora criado (calculadora.py)..."
python3 calculadora.py

# Finaliza script.
echo "Fim de execução de Script."
