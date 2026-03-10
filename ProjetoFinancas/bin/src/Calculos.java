package src;

import java.util.ArrayList;
public class Calculos extends Valores{

    public float valorRestante() {
        float valorTotalDespesas = 0;
        float valorTotalReceitas = 0;
        for (float despesa : despesas.values()) {
            valorTotalDespesas += despesa;
        }
        for (float receita : receitas.values()) {
            valorTotalReceitas += receita;
        }
        return (valorTotalReceitas - valorTotalDespesas);
    }

    public static void main(String[] args) {
        Valores valores = new Valores();
        Calculos calculo = new Calculos();

        valores.menu();
    }
}