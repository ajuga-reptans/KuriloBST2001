package com.company;
import java.util.Scanner;

 //класс для решение 2 задачи
public class Palindrome {
    //главный метод (ввод, проверка и вывод)
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        String[] words = s.split(" ");
        for(String word : words) {
            if (isPalindrome(word))
                System.out.println("Палиндром");
            else System.out.println("He Палиндром");
        }
    }
    //переворот строки
    public static String reverseString(String s){
        String a = new String();
        for(int i = s.length() - 1; i >= 0; i--) {
            a += s.charAt(i);
        }
        return a;
    }
    //Проверка на полиндромность
    public static boolean isPalindrome(String s){
        return (s.equals(reverseString(s)));
    }
}
