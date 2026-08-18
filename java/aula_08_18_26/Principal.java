package br.edu.principal;
import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		
		String situacao;
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Digite o seu nome:");
		String nome = sc.next();
		
		System.out.println("Digite sua primeira nota:");
		double n1 = sc.nextDouble();
		
		System.out.println("Digite sua segunda nota:");
		double n2 = sc.nextDouble();
		
		double media = (n1+n2)/2;
		
		if (media >=6) {
			situacao = "Aprovado";
			System.out.println("Nome: " + nome + " | Média: " + media + " | Situacação: " + situacao);
		}
		else {
			if (media >= 3) {
				situacao = "Em recuperação";
				System.out.println("Situação: " + situacao);
				
				System.out.println("Digite a nota da AF:");
				double af = sc.nextDouble();
				
				double mf = (af + media) / 2;
				
				if (mf >= 5) {
					situacao = "Aprovado em recuperação";
					System.out.println("Nome: " + nome + " | Média final: " + mf + " | Situacação: " + situacao);
				}
				else {
					situacao = "HUAHUAHUAHAHAHA";
					System.out.println("Situação: " + situacao);
					System.out.println("Nome: " + nome + " | Média final: " + mf + " | Situacação: " + situacao);
				}
			}
			else {
				situacao = "Reprovado";
				System.out.println("Nome: " + nome + " | Média: " + media + " | Situacação: " + situacao);
			}
		}
	}
}