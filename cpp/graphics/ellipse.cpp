#include <graphics.h>
#include <conio.h>

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    
    int centerX = getmaxx() / 2;
    int centerY = getmaxy() / 2;
    int radiusX = 100;
    int radiusY = 60;
    
    // Draw ellipse
    ellipse(centerX, centerY, 0, 360, radiusX, radiusY);
    
    getch();
    closegraph();
    return 0;
}