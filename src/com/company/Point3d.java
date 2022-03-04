package com.company;

public class Point3d {
    private double xCoord;
    private double yCoord;
    private double zCoord;

    public Point3d ( double x, double y, double z) {
        xCoord = x;
        yCoord = y;
        zCoord = z;
    }

    public Point3d () {
        this(0, 0, 0);
    }

    public double getX () {
        return xCoord;
    }

    public double getY () {
        return yCoord;
    }

    public double getZ () {
        return zCoord;
    }

    public void setX (double val) {
        xCoord = val;
    }

    public void setY (double val) {
        yCoord = val;
    }

    public void setZ (double val) {
        zCoord = val;
    }

    public boolean pointCompar ( Point3d P) {
        if (xCoord == P.getX() && yCoord == P.getY() && zCoord == P.getZ())
            return true;
        else
            return false;
    }

    public double distanceTo ( Point3d P ) {
        double S = Math.sqrt( Math.pow( (xCoord - P.getX()), 2 )  + Math.pow( (yCoord - P.getY()), 2 ) + Math.pow( (zCoord - P.getZ()), 2 ) );
        return (Math.round(S * 100.0) / 100.0);
    }

}

