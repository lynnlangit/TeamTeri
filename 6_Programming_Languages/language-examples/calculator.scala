/* Create a Calculator class that has a method named add */
/* that takes two parameters, both of which are numbers. */
/* The method should return the sum of the two numbers. */

class Calculator {
    public int add(int a, int b) {
        return a + b;

    public int subtract(int a, int b) {
        return a - b;

    public int multiply(int a, int b) {
        return a * b;
    }

    public int divide(int a, int b) {
        return a / b;
    }

    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println(calc.add(1, 2));
    }

function testCalculator() {
    var calculator = new Calculator();
    if (calculator.add(1, 2) === 3) {
        console.log("Test passed");
    } else {
        console.log("Test failed");
    }
}

}