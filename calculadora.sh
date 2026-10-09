#!/bin/bash
# Calculadora simples em Bash
# Operações: soma, subtração, multiplicação e divisão

echo "=============================="
echo "      CALCULADORA EM BASH     "
echo "=============================="

read -p "Digite o primeiro número: " num1
read -p "Digite o segundo número: " num2

echo ""
echo "Escolha a operação:"
echo "1 - Soma (+)"
echo "2 - Subtração (-)"
echo "3 - Multiplicação (*)"
echo "4 - Divisão (/)"
read -p "Opção: " opcao

case $opcao in
  1)
    resultado=$(echo "$num1 + $num2" | bc -l)
    echo "Resultado: $num1 + $num2 = $resultado"
    ;;
  2)
    resultado=$(echo "$num1 - $num2" | bc -l)
    echo "Resultado: $num1 - $num2 = $resultado"
    ;;
  3)
    resultado=$(echo "$num1 * $num2" | bc -l)
    echo "Resultado: $num1 * $num2 = $resultado"
    ;;
  4)
    if [ "$(echo "$num2 == 0" | bc -l)" -eq 1 ]; then
      echo "Erro: não é possível dividir por zero."
    else
      resultado=$(echo "scale=2; $num1 / $num2" | bc -l)
      echo "Resultado: $num1 / $num2 = $resultado"
    fi
    ;;
  *)
    echo "Opção inválida!"
    ;;
esac
