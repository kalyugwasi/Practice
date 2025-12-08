#include <stdio.h>
#include <conio.h>
#include <graphics.h>
#include <math.h>
int main()
{
    int driver = DETECT, mode;
    initgraph(&driver, &mode, "");
    int radius;
    printf("Enter radius of circle: ");
    scanf("%d",&radius);
    circle(250, 250, radius);
    getch();
    closegraph();
}