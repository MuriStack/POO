package br.edu.principal;
import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Digite o seu nome:");
		String nome = sc.next();
		
		System.out.println("Digite sua primeira nota:");
		double n1 = sc.nextDouble();
		
		System.out.println("Digite sua segunda nota:");
		double n2 = sc.nextDouble();
		
		double media = (n1+n2)/2;
		
		System.out.println("Nome: " + nome + " | Média: " + media);

	}

}