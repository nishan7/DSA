/*
#### Name:  Encapsulation
Link: [link]()

1) Hiding members of a class
3) That couldn't be changed or interferred with
2) That can be accessed using objects, using getter and setter methods

*/

class Staff{
    private String incharge;
    String  class_name  = "staff";

    void setter(String name){
        incharge = name;
    }

    String getter(){
        return incharge;
    }

}

class Encapsulation{
    public static void main(String[] args){
        Staff s = new Staff();
        s.setter("Nishan");

        // System.out.println(s.incharge);  // Staff.incharge is not visible

        System.out.println(s.getter());

    }
}