import java.util.Scanner;

public class ContaTerminal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe seu número de conta");
        int numero = scanner.nextInt();

        System.out.println("Informe seu número de agencia");
        String agencia = scanner.next();

        System.out.println("Informe nome do cliente");
        String nomeCliente = scanner.next();

        double saldo = 1450.7;

        String mensagem = String.format(
                "Olá %s, obrigado por criar uma conta em nosso banco, sua agência é %s, conta %d e seu saldo R$ %.2f já está disponível para saque.",
                nomeCliente, agencia, numero, saldo
        );

        System.out.printf(mensagem);
}}