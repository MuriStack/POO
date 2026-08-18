package br.edu.principal;
import java.util.Scanner;

public class Switch {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Digite um número de 1 a 7:");
		int dia = sc.nextInt();
		
		//IF - ELSE IF - ELSE
		if (dia == 1) {
			System.out.println("Domingo");
		}
		else if (dia == 2) {
			System.out.println("Segunda");
		}
		else if (dia == 3) {
			System.out.println("Terça");
		}
		else {
			System.out.println("Esse dia não existe");
		}
		
		// SWITCH-CASE
		switch(dia) {
		case 1:
			System.out.println("Domingo");
			break;
			
		case 2:
			System.out.println("Segunda");
			break;
			
		case 3:
			System.out.println("Terça");
			break;
			
		default:
			System.out.println("Esse dia não existe");
		}
		
		//SWITCH-CASE MODERNO
		switch(dia) {
		case 1 -> System.out.println("Domingo");
		
		case 2 -> System.out.println("Segunda");
		
		case 3 -> System.out.println("Terça");
		
		case 4 -> System.out.println("Esse dia não existe");
		}
		

	}

}
