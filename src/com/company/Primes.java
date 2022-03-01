package com.company;

public class Primes {

    public static void main(String[] args) {
        for(int i = 2; i <= 100; i++){
            if(isPrime(i)) {
                System.out.print(i + " ");
            }
        }
    }
    public static boolean isPrime(int n)
    {   boolean b = true;
        for(int i = 2; i < n; i++) {
            if (n % i == 0) {
                b = false;
                break;
            }
        }
        return b;
    }
}

