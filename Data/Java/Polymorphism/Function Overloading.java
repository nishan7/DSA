/*
#### Name:  Polymorphism
Link: [link]()

#### Sub_question_name: Function Overloading 
Link: [link]()


Polymorphism means multiple forms


To do same task in different ways according to context

Function overloading, Function Overriding

*/

class Numbers{
    // Changing them to static also works well    
    int sum(int a, int b){
        return a+b;
    }

    double sum(double a, double  b){
        return a+b;
    }
    
    public static void main(String[] args){
        Numbers  p   = new Numbers();
        System.out.println(p.sum(1,2));
        System.out.println(p.sum(1.2,2.5));

    }
}