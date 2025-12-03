#include <stdio.h>
#include <conio.h>
#include <graphics.h>
#include <math.h>

void circlepoint(int x, int y, int xc, int yc)
{
    putpixel(x + xc, y + yc, WHITE);
    putpixel(y + xc, x + yc, WHITE);
    putpixel(-x + xc, y + yc, WHITE);
    putpixel(-y + xc, x + yc, WHITE);
    putpixel(-x + xc, -y + yc, WHITE);
    putpixel(-y + xc, -x + yc, WHITE);
    putpixel(x + xc, -y + yc, WHITE);
    putpixel(y + xc, -x + yc, WHITE);
}

int main()
{
    int driver = DETECT, mode;
    initgraph(&driver, &mode, "");

    int x = 0, y, d, r, xc, yc;

    int x1 = getmaxx() / 2;
    int y1 = getmaxy() / 2;

    line(x1, 0, x1, 2 * y1);
    line(0, y1, 2 * x1, y1);

    printf("Enter radius: ");
    scanf("%d", &r);

    printf("Enter center coordinates: ");
    scanf("%d %d", &xc, &yc);

    xc = xc + x1;
    yc = yc + y1;

    y = r;
    d = 1 - r;

    while (x <= y)
    {
        circlepoint(x, y, xc, yc);

        if (d < 0)
            d += 2 * x + 3;
        else
        {
            d += 2 * (x - y) + 5;
            y--;
        }
        x++;
    }

    getch();
    closegraph();
    return 0;
}