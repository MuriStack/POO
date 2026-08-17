package br.edu.principal;
import java.util.Scanner;

public class Exercicio {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Digite o seu nome:");
		String nome = sc.nextLine();
		
		System.out.println("Digite o número do seu endereço:");
		String numero = sc.nextLine();
		
		System.out.println("Digite o nome da sua rua:");
		String rua = sc.nextLine();
		
		System.out.println("Digite o nome do seu bairro:");
		String bairro = sc.nextLine();
		
		System.out.println("Digite o seu CEP:");
		String cep = sc.nextLine();
		
		System.out.println("Digite a sua UF:");
		String uf = sc.nextLine();
		
		System.out.println("Digite o seu CPF:");
		String cpf = sc.nextLine();
		
		System.out.println("Digite o dia que você nasceu:");
		String dia = sc.nextLine();
		
		System.out.println("Digite o mês que você nasceu:");
		String mes = sc.nextLine();
		
		System.out.println("Digite o ano que você nasceu:");
		String ano = sc.nextLine();
		
		System.out.println("Digite a sua idade");
		String idade = sc.nextLine();
		
		System.out.println("\n========================================");
        System.out.println("          DADOS CADASTRADOS             ");
        System.out.println("========================================");
        System.out.println("Nome: " + nome);
        System.out.println("CPF: " + cpf);
        System.out.println("Idade: " + idade + " anos");
        System.out.println("Data de Nascimento: " + dia + "/" + mes + "/" + ano);
        System.out.println("--- Endereço ---");
        System.out.println("Rua: " + rua + ", Nº " + numero);
        System.out.println("Bairro: " + bairro);
        System.out.println("CEP: " + cep + " | UF: " + uf);
        System.out.println("========================================");
		
	}

}
