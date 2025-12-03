#include <stdio.h>
#include <conio.h>
#include <graphics.h>
#include <math.h>

void draw(int x1, int y1, int x2, int y2);

int main() {
    int x1, y1, x2, y2;
    int gdriver = DETECT, gmode;

    initgraph(&gdriver, &gmode, "");

    printf("Enter x1 y1: ");
    scanf("%d%d", &x1, &y1);

    printf("Enter x2 y2: ");
    scanf("%d%d", &x2, &y2);

    draw(x1, y1, x2, y2);

    getch();
    closegraph();
    return 0;
}

void draw(int x1, int y1, int x2, int y2) {
    float dx = x2 - x1;
    float dy = y2 - y1;
    int steps = (abs(dx) > abs(dy)) ? abs(dx) : abs(dy);

    float xInc = dx / steps;
    float yInc = dy / steps;

    float x = x1;
    float y = y1;

    for (int i = 0; i <= steps; i++) {
        putpixel(round(x), round(y), WHITE);
        x += xInc;
        y += yInc;
    }
}