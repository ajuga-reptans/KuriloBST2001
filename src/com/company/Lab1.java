package com.company;
import java.util.Scanner;

public class Lab1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[] coord = new double[3];
        Point3d[] p = new Point3d[3];
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                coord[j] = sc.nextDouble();
            }
            p[i] = new Point3d(coord[0], coord[1], coord[2]);
        }
        if( p[0].pointCompar(p[1]) || p[0].pointCompar(p[2]) || p[2].pointCompar(p[1]))
            System.out.println("В треугольнике не может быть две одинаковые точки");
        else
            System.out.println( (int )(computeArea(p[0], p[1], p[2]) + 1));

    }

    public static double computeArea(Point3d A, Point3d B, Point3d C){
        double a, b, c;
        a = A.distanceTo(B);
        b = B.distanceTo(C);
        c = A.distanceTo(C);
        double p = (a + b + c) / 2;
        return (Math.sqrt(p * (p - a) * (p - b) * (p - c)));
    }
}
