# Calculadora em Shell Script e Python

Projeto do curso **Profissão Analista de Dados (EBAC)**.
Uma calculadora simples que faz **soma, subtração, multiplicação e divisão** entre dois números, implementada de duas formas:

| Arquivo | Linguagem | Descrição |
|---|---|---|
| `calculadora.sh` | Bash (Shell Script) | Versão executável no terminal Linux |
| `calculadora.py` | Python 3 | Mesma calculadora escrita em Python |

---

## Como executar o arquivo `.sh`

### Pré-requisitos
- Linux (ou WSL no Windows / terminal do macOS)
- Programa `bc` (faz as contas com casas decimais). Se não tiver, instale:
  ```bash
  sudo apt install bc
  ```

### Passo a passo

1. **Clone o repositório** (ou baixe o arquivo `calculadora.sh`):
   ```bash
   git clone https://github.com/SEU-USUARIO/calculadora-ebac.git
   cd calculadora-ebac
   ```

2. **Dê permissão de execução** ao arquivo:
   ```bash
   chmod +x calculadora.sh
   ```

3. **Defina as permissões** (apenas o proprietário escreve; os demais só leem e executam):
   ```bash
   chmod 755 calculadora.sh
   ls -l calculadora.sh
   # -rwxr-xr-x ... calculadora.sh
   ```

4. **Execute o script**:
   ```bash
   ./calculadora.sh
   ```
   Também é possível rodar sem dar permissão de execução: `bash calculadora.sh`

### Exemplo de uso
```
==============================
      CALCULADORA EM BASH
==============================
Digite o primeiro número: 10
Digite o segundo número: 4

Escolha a operação:
1 - Soma (+)
2 - Subtração (-)
3 - Multiplicação (*)
4 - Divisão (/)
Opção: 4
Resultado: 10 / 4 = 2.50
```

### Como o script `.sh` funciona
- `#!/bin/bash` (shebang) indica que o arquivo deve ser executado pelo Bash.
- `read -p` exibe uma mensagem e guarda o que o usuário digitou em uma variável (`num1`, `num2`, `opcao`).
- `case ... esac` escolhe qual operação fazer de acordo com a opção digitada.
- `echo "..." | bc -l` envia a conta para o `bc`, que calcula com casas decimais. Na divisão, `scale=2` limita o resultado a 2 casas.
- Antes de dividir, o script verifica se o segundo número é zero e mostra uma mensagem de erro.

---

## Como executar o código em Python

### Pré-requisitos
- Python 3 instalado (`python3 --version` para conferir)

### Execução
```bash
python3 calculadora.py
```

## Explicação do código em Python

O código está organizado em **funções**, cada uma com uma responsabilidade:

### 1. Funções das operações
```python
def somar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("não é possível dividir por zero.")
    return a / b
```
- `somar`, `subtrair`, `multiplicar` e `dividir` recebem dois números e devolvem o resultado.
- `dividir` verifica se o divisor é zero e, nesse caso, **lança uma exceção** (`ZeroDivisionError`) com uma mensagem amigável.

### 2. Leitura segura dos números
```python
def ler_numero(mensagem):
    while True:
        valor = input(mensagem).replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Valor inválido. Digite um número (ex.: 10 ou 2.5).")
```
- `input()` lê o que o usuário digita (sempre como texto).
- `.replace(",", ".")` aceita números com vírgula, como `2,5`.
- `float()` converte o texto em número. Se o usuário digitar algo inválido (ex.: `abc`), o `try/except` captura o erro e pede de novo, graças ao laço `while True`.

### 3. Função principal (`main`)
```python
operacoes = {
    "1": ("+", somar),
    "2": ("-", subtrair),
    "3": ("*", multiplicar),
    "4": ("/", dividir),
}
```
- Mostra o menu e lê os dois números e a opção.
- Usa um **dicionário** que liga cada opção ao seu símbolo e à função correspondente, evitando uma longa sequência de `if/elif`.
- Se a opção não existir no dicionário, exibe `Opção inválida!`.
- Chama a função escolhida dentro de um `try/except` para tratar a divisão por zero.
- Exibe o resultado com 2 casas decimais usando f-string: `f"{resultado:.2f}"`.

### 4. Ponto de entrada
```python
if __name__ == "__main__":
    main()
```
Garante que `main()` só roda quando o arquivo é executado diretamente (e não quando ele é importado por outro script).

---

## Autor
Felipe — Projeto do curso EBAC
