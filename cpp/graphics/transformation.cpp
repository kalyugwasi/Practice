#include <graphics.h>
#include <conio.h>
#include <math.h>
#include <stdio.h>

void drawSquare(int x, int y, int size) {
    rectangle(x, y, x + size, y + size);
}

void translate(int &x, int &y, int tx, int ty) {
    x += tx;
    y += ty;
}

void scale(int &x, int &y, float sx, float sy, int cx, int cy) {
    x = cx + (x - cx) * sx;
    y = cy + (y - cy) * sy;
}

void rotate(int &x, int &y, float angle, int cx, int cy) {
    float rad = angle * 3.14159 / 180.0;
    int tempX = x - cx;
    int tempY = y - cy;
    x = cx + (tempX * cos(rad) - tempY * sin(rad));
    y = cy + (tempX * sin(rad) + tempY * cos(rad));
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    
    int x = 100, y = 100, size = 50;
    
    // Original square
    setcolor(WHITE);
    drawSquare(x, y, size);
    outtextxy(x, y + 80, "Original");
    
    // Translation
    int x1 = x, y1 = y;
    translate(x1, y1, 150, 0);
    setcolor(GREEN);
    drawSquare(x1, y1, size);
    outtextxy(x1, y1 + 80, "Translated");
    
    // Scaling
    int x2 = x, y2 = y;
    scale(x2, y2, 1.5, 1.5, x, y);
    setcolor(CYAN);
    drawSquare(x2, y2, size * 1.5);
    outtextxy(x2, y2 + 100, "Scaled");
    
    getch();
    closegraph();
    return 0;
}