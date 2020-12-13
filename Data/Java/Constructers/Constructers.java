/*

#### Name:  Constructers
Link: [link]()

*/

//Rectangle
class Constructers {
    int length;
    int breadth;

    // Default Constructor
    Constructers() {
        length = 0;
        breadth = 0;
    }

    // Parameterized Constructor
    Constructers(int l, int b) {
        length = l;
        breadth = b;
    }

    // Copy Constructor
    Constructers(Constructers c) {
        length = c.length;
        breadth = c.breadth;
    }

    void print() {
        System.out.println(length + " " + breadth);
    }

    public static void main(String[] args) {
        Constructers defaultConst = new Constructers();
        defaultConst.print();

        Constructers paramConst = new Constructers(4, 5);
        paramConst.print();

        Constructers copyConst = new Constructers(paramConst);
        copyConst.print();

    }
}