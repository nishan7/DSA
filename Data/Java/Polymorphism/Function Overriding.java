/*
#### Name:  Polymorphism
Link: [link]()

#### Sub_question_name: Function Overriding 
Link: [link]()

Overrides the base class method by child class

*/

class Rect {
    int l, b;

    Rect(int a, int b) {
        // System.out.println("Rect Constructor");
        this.l = a;
        this.b = b;
    }

    int area() {
        return l * b;
    }
}

class Square extends Rect {
    int l;

    Square(int a) {

        super(a, 0);
        // System.out.println("Square Constructor");
        l = a;

    }

    @Override //Optional
    int area(){
        return l * l;
    }

    public static void main(String[] args) {
        Square s = new Square(5);
        System.out.println("Square area " + s.area());

        Rect r  = new Rect(5,4);
        System.out.println("Rect Area "+r.area());
        
        Rect r2  = new Square(9);
        System.out.println("Rect Area with object of type "+r2.getClass()+ "    "+r2.area());


    }
}