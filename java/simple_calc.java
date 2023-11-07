package com.java;

import java.util.Scanner;

class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Hi! I'm simple calculator on Java :)\nChoose the action (+, -, *, /): ");
        String ask_action = scan.nextLine();
        if (ask_action.equals("+")) {
            System.out.print("Enter the first number: ");
            float num1 = scan.nextFloat();
            System.out.print("Enter the second number: ");
            float num2 = scan.nextFloat();
            float res = num1 + num2;
            System.out.print("Result: " + res);
        } else if (ask_action.equals("-")) {
            System.out.print("Enter the first number: ");
            float num1 = scan.nextFloat();
            System.out.print("Enter the second number: ");
            float num2 = scan.nextFloat();
            float res = num1 - num2;
            System.out.print("Result: " + res);
        } else if (ask_action.equals("*")) {
            System.out.print("Enter the first number: ");
            float num1 = scan.nextFloat();
            System.out.print("Enter the second number: ");
            float num2 = scan.nextFloat();
            float res = num1 * num2;
            System.out.print("Result: " + res);
        } else if (ask_action.equals("/")) {
            System.out.print("Enter the first number: ");
            float num1 = scan.nextFloat();
            System.out.print("Enter the second number: ");
            float num2 = scan.nextFloat();
            if (num1 == 0 || num2 == 0) {
                System.out.print("Result: 0.0");
            } else {
                float res = num1 / num2;
                System.out.print("Result: " + res);
            }
        } else {
            System.out.print("This action doesn't support or you've entered wrong action :(");
        }
    }

}
