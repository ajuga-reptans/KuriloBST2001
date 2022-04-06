package com.company.lab3;
import java.util.*;

public class AStarState {
    /** This is a reference to the map that the A* algorithm is navigating. **/
    private Map2D map;
    private HashMap<Location, Waypoint> closeWaypoint;
    private HashMap<Location, Waypoint> openWaypoints;


    /**
     * Initialize a new state object for the A* pathfinding algorithm to use.
     **/
    public AStarState(Map2D map)
    {
        if (map == null)
            throw new NullPointerException("map cannot be null");

        this.map = map;
        this.closeWaypoint = new HashMap<Location, Waypoint>();
        this.openWaypoints = new HashMap<Location, Waypoint>();
    }

    /** Returns the map that the A* pathfinder is navigating. **/
    public Map2D getMap()
    {
        return map;
    }

    /**
     * This method scans through all open waypoints, and returns the waypoint
     * with the minimum total cost. If there are no open waypoints, this method
     * returns <code>null</code>.
     **/

    public Waypoint getMinOpenWaypoint()
    {
        Waypoint minPoint = null;
        if (!openWaypoints.isEmpty()) {
            double minCost = Double.MAX_VALUE;
            for (Waypoint CPoint : openWaypoints.values())
                if (CPoint.getTotalCost() < minCost) {
                    minCost = CPoint.getTotalCost();
                    minPoint = CPoint;
                }
        }
        return minPoint;
    }

    public boolean addOpenWaypoint(Waypoint newWP)
    {
        if (openWaypoints.containsKey(newWP.getLocation())) {
            if (newWP.getPreviousCost() < openWaypoints.get(newWP.getLocation()).getPreviousCost()) {
                openWaypoints.put(newWP.getLocation(), openWaypoints.get(newWP.getLocation()));
                return true;
            }
            return false;
        }
        else {
            openWaypoints.put(newWP.getLocation(), newWP);
            return true;
        }
    }


    /** Returns the current number of open waypoints. **/
    public int numOpenWaypoints()
    {
        return openWaypoints.size();
    }


    /**
     * This method moves the waypoint at the specified
     location from the
     * open list to the closed list.
     **/
    public void closeWaypoint(Location loc)
    {
        closeWaypoint.put(loc,openWaypoints.get(loc));
        openWaypoints.remove(loc);
    }

    /**
     * Returns true if the collection of closed waypoints contains a waypoint
     * for the specified location.
     **/
    public boolean isLocationClosed(Location loc)
    {
        return closeWaypoint.keySet().contains(loc);
    }
}
