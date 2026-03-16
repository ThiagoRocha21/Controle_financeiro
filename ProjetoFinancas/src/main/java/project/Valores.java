//ideias:
//Ajeitar as opções do menu para não dar erro
//Criar scripts do BD
    //Scripts a serem criados:
        //Adicionar Despesas
        //Adicioanr Receitas
//Adicionar uma forma de transferir esses dados para uma planilha e manter salvo para acompanhar o progresso

package project;


import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

public class Valores {

    //Mapas que vão salvar as despesas/receitas e seus valores
    static Map<String, Float> despesas = new HashMap<String, Float>();
    static Map<String, Float> receitas = new HashMap<String, Float>();

    Scanner scanner = new Scanner(System.in);

    //FUNÇÕES DE MENU::

    //Função que adiciona receitas no mapa
    public void AdicionaReceita() {
        while(true){
            System.out.println("================================");
            System.out.println("Escolha uma opção: ");
            System.out.println("1 - Digitar receita: ");
            System.out.println("2 - Sair");
            int opcao = scanner.nextInt();
            scanner.nextLine();

            if(opcao == 1){
                System.out.println("Digite o nome da receita: ");
                String nomeReceita = scanner.nextLine();

                System.out.println("Digite o valor da receita: ");
                float adicionarReceitas = scanner.nextFloat();

                receitas.put(nomeReceita, adicionarReceitas);
            }

            else if(opcao == 2){break;}

            else{
                System.out.println("Digite uma opção válida.");
                scanner.nextLine();
            }
        }
    }



    //função que adiciona despesas no mapa
    public void AdicionaDespesas() {
        while(true){
            System.out.println("================================");
            System.out.println("Escolha uma opção: ");
            System.out.println("1 - Digitar despesa: ");
            System.out.println("2 - Sair");
            int opcao = scanner.nextInt();
            scanner.nextLine();

            if(opcao == 1){
                System.out.println("Digite o nome da despesa: ");
                String nomeDespesa = scanner.nextLine();

                System.out.println("Digite o valor da despesa: ");
                float adicionarDespesas = scanner.nextFloat();

                despesas.put(nomeDespesa, adicionarDespesas);
            }

            else if(opcao == 2){break;}

            else{
                System.out.println("Digite uma opção válida.");
                scanner.nextLine();
            }
        }
    }

    //função que exibe as informações financeiras passadas
    public void informacoesDespesa(){
        System.out.println(String.format("|   %s   |", "Despesas"));
        int i = 0;
        for(Map.Entry<String, Float> despesa : despesas.entrySet()){
            String chave = despesa.getKey();
            Float valor = despesa.getValue();

            System.out.println("Despesa "+(i+1)+": "+chave+" | Valor: "+valor);
            i += 1;
        }
    }

    public void informacoesReceita(){
        System.out.println(String.format("|   %s   |", "Receitas"));
        int i = 0;
        for(Map.Entry<String, Float> receita : receitas.entrySet()){
            String chave = receita.getKey();
            Float valor = receita.getValue();

            System.out.println("Receita "+(i+1)+": "+chave+" | Valor: "+valor);
            i += 1;
        }
    }


    // menu interativo
    public void menu() {
        while (true) {
            System.out.println("================================");
            System.out.println("Escolha uma opção: ");
            System.out.println("1 - Adicioanr Despesa: ");
            System.out.println("2 - Adicionar Receitas: ");
            System.out.println("3 - Mostrar despesas: ");
            System.out.println("4 - Mostrar receitas: ");
            System.out.println("5 - Mostrar tudo: ");
            System.out.println("6 - Sair");
            int opcao = scanner.nextInt();
            scanner.nextLine();

            if (opcao == 1) {
                AdicionaDespesas();
            } else if (opcao == 2) {
                AdicionaReceita();
            } else if(opcao == 3){
                System.out.println("Opção ainda não disponível. Tente outra.");
                scanner.nextLine();
            }else if(opcao == 4){
                System.out.println("Opção ainda não disponível. Tente outra.");
                scanner.nextLine();
            }else if(opcao == 5) {
                informacoesDespesa();
                informacoesReceita();
            }else if (opcao == 6) {
                break;
            }
        }
    }



    //FUNÇÕES DO DB::


}