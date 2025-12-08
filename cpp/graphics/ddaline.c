#include <graphics.h>
#include <math.h>

int main() {
    int gd = DETECT, gm;
    int x1, y1, x2, y2;
    initgraph(&gd, &gm, "");
    printf("Enter coordinates of first point (x1,y1):");
    scanf("%d%d", &x1, &y1);
    printf("Enter coordinates of second point (x2,y2):");
    scanf("%d%d", &x2, &y2);

    float dx = x2 - x1, dy = y2 - y1;
    int steps = (fabs(dx) > fabs(dy)) ? fabs(dx) : fabs(dy);
    float xInc = dx / steps, yInc = dy / steps;
    float x = x1, y = y1;

    for (int i = 0; i <= steps; i++) {
        putpixel(round(x), round(y), RED);
        x += xInc;
        y += yInc;
    }

    getch();
    closegraph();
}
