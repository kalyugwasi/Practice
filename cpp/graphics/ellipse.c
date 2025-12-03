#include <stdio.h>
#include <graphics.h>
#include <math.h>

void display(int x, int y, int xc, int yc) {
    putpixel(xc + x, yc + y, WHITE);
    putpixel(xc - x, yc + y, WHITE);
    putpixel(xc + x, yc - y, WHITE);
    putpixel(xc - x, yc - y, WHITE);
}

int main() {
    int gd = DETECT, gm;
    int rx, ry, xc, yc;
    float p1, p2, x, y;

    initgraph(&gd, &gm, "");

    printf("Enter center (xc yc): ");
    scanf("%d %d", &xc, &yc);

    printf("Enter radii (rx ry): ");
    scanf("%d %d", &rx, &ry);

    x = 0;
    y = ry;

    p1 = (ry * ry) - (rx * rx * ry) + (0.25 * rx * rx);

    while ((2 * ry * ry * x) <= (2 * rx * rx * y)) {
        display(x, y, xc, yc);
        if (p1 < 0)
            p1 += 2 * ry * ry * (x + 1) + ry * ry;
        else {
            p1 += 2 * ry * ry * (x + 1) - 2 * rx * rx * (y - 1) + ry * ry;
            y--;
        }
        x++;
    }

    p2 = (ry * ry) * (x + 0.5) * (x + 0.5) + (rx * rx) * (y - 1) * (y - 1) - (rx * rx * ry * ry);

    while (y >= 0) {
        display(x, y, xc, yc);
        if (p2 > 0)
            p2 += -2 * rx * rx * (y - 1) + rx * rx;
        else {
            p2 += 2 * ry * ry * (x + 1) - 2 * rx * rx * (y - 1) + rx * rx;
            x++;
        }
        y--;
    }

    getch();
    closegraph();
    return 0;
}