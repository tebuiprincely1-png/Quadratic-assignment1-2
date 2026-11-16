#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    double A, B, C;

    cout << "Quadratic equation: A*x^2 + B*x + C = 0\n";
    cout << "Enter A: ";
    cin >> A;
    cout << "Enter B: ";
    cin >> B;
    cout << "Enter C: ";
    cin >> C;

    if (A == 0) {
        cout << "A cannot be 0, this is not a quadratic equation.\n";
        return 1;
    }

    double D = B * B - 4 * A * C;   // discriminant
    cout << fixed << setprecision(2);

    cout << "\n--- Analysis ---\n";
    cout << "Equation: " << A << "x^2 + " << B << "x + " << C << " = 0\n";
    cout << "Discriminant (B^2 - 4AC) = " << D << "\n";

    // Nature of the roots
    if (D > 0) {
        cout << "Nature of roots: REAL and DISTINCT (unequal)\n";
        if (D == floor(D) && sqrt(D) == floor(sqrt(D)) &&
            B == floor(B) && A == floor(A))
            cout << "The roots are also RATIONAL (D is a perfect square).\n";
        else
            cout << "The roots are IRRATIONAL.\n";
    } else if (D == 0) {
        cout << "Nature of roots: REAL and EQUAL (repeated root)\n";
    } else {
        cout << "Nature of roots: IMAGINARY (complex conjugates, no real roots)\n";
    }

    // Roots and factors
    if (D > 0) {
        double x1 = (-B + sqrt(D)) / (2 * A);
        double x2 = (-B - sqrt(D)) / (2 * A);
        cout << "\n--- Roots ---\n";
        cout << "x1 = " << x1 << "\n";
        cout << "x2 = " << x2 << "\n";
        cout << "\n--- Factors ---\n";
        cout << A << " * (x - (" << x1 << ")) * (x - (" << x2 << "))\n";
    } else if (D == 0) {
        double x = -B / (2 * A);
        cout << "\n--- Roots ---\n";
        cout << "x1 = x2 = " << x << "\n";
        cout << "\n--- Factors ---\n";
        cout << A << " * (x - (" << x << "))^2\n";
    } else {
        double real = -B / (2 * A);
        double imag = sqrt(-D) / (2 * fabs(A));
        cout << "\n--- Roots ---\n";
        cout << "x1 = " << real << " + " << imag << "i\n";
        cout << "x2 = " << real << " - " << imag << "i\n";
        cout << "\n--- Factors ---\n";
        cout << A << " * (x - (" << real << " + " << imag << "i)) * (x - ("
             << real << " - " << imag << "i))\n";
    }

    // Extra information
    cout << "\n--- Extra information ---\n";
    cout << "Sum of roots (-B/A)     = " << -B / A << "\n";
    cout << "Product of roots (C/A)  = " << C / A << "\n";
    cout << "Axis of symmetry: x = " << -B / (2 * A) << "\n";
    double vx = -B / (2 * A);
    double vy = A * vx * vx + B * vx + C;
    cout << "Vertex: (" << vx << ", " << vy << ")\n";
    cout << "Parabola opens " << (A > 0 ? "UPWARD (minimum point)" : "DOWNWARD (maximum point)") << "\n";
    cout << "y-intercept: (0, " << C << ")\n";
    if (D >= 0)
        cout << "The graph touches/crosses the x-axis at " << (D > 0 ? "two points" : "one point") << ".\n";
    else
        cout << "The graph does not cross the x-axis.\n";

    return 0;
}
