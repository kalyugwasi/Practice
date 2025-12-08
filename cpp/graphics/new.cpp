#include <graphics.h>
#include <conio.h>
#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, " ");

    float x1, y1, x2, y2, dx, dy, steps, x_inc, y_inc, x, y;

    cout << "Enter x1 y1 : ";
    cin >> x1 >> y1;

    cout << "Enter x2 y2 : ";
    cin >> x2 >> y2;

    dx = x2 - x1;
    dy = y2 - y1;

    if (abs(dx) > abs(dy))
        steps = abs(dx);
    else
        steps = abs(dy);

    x_inc = dx / steps;
    y_inc = dy / steps;

    x = x1;
    y = y1;

    for (int i = 0; i <= steps; i++) {
        putpixel(round(x), round(y), YELLOW);
        x += x_inc;
        y += y_inc;
        delay(5);
    }

    getch();
    closegraph();
    return 0;
}