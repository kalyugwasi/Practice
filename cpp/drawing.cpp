#include <graphics.h>
#include <conio.h>

int main() {
    int gd = DETECT, gm;
    char path[] = "";
    initgraph(&gd, &gm, path);
    circle(200, 200, 100);
    getch();
    closegraph();
    return 0;
}
