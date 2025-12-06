#include <stdio.h>
#include <graphics.h>
#include <math.h>

int main() {
    int gd = DETECT, gm;
    int x1, y1, x2, y2, x3, y3;
    int nx1, ny1, nx2, ny2, nx3, ny3;
    int choice;
    int tx, ty, sx, sy, angle;
    float rad;

    initgraph(&gd, &gm, " ");

    printf("Enter triangle coordinates: ");
    scanf("%d %d %d %d %d %d", &x1, &y1, &x2, &y2, &x3, &y3);

    setcolor(WHITE);
    line(x1, y1, x2, y2);
    line(x2, y2, x3, y3);
    line(x3, y3, x1, y1);

    printf("\n1. Translation\n2. Rotation\n3. Scaling\n4. Exit\nEnter choice: ");
    scanf("%d", &choice);

    switch (choice) {
        case 1:
            printf("Enter translation (tx ty): ");
            scanf("%d %d", &tx, &ty);
            nx1 = x1 + tx; ny1 = y1 + ty;
            nx2 = x2 + tx; ny2 = y2 + ty;
            nx3 = x3 + tx; ny3 = y3 + ty;
            break;
        case 2:
            printf("Enter rotation angle in degrees: ");
            scanf("%d", &angle);
            rad = angle * M_PI / 180.0;
            nx1 = round(x1 * cos(rad) - y1 * sin(rad)); ny1 = round(x1 * sin(rad) + y1 * cos(rad));
            nx2 = round(x2 * cos(rad) - y2 * sin(rad)); ny2 = round(x2 * sin(rad) + y2 * cos(rad));
            nx3 = round(x3 * cos(rad) - y3 * sin(rad)); ny3 = round(x3 * sin(rad) + y3 * cos(rad));
            break;
        case 3:
            printf("Enter scaling (sx sy): ");
            scanf("%d %d", &sx, &sy);
            nx1 = x1 * sx; ny1 = y1 * sy;
            nx2 = x2 * sx; ny2 = y2 * sy;
            nx3 = x3 * sx; ny3 = y3 * sy;
            break;
        default:
            closegraph();
            return 0;
    }

    setcolor(YELLOW);
    line(nx1, ny1, nx2, ny2);
    line(nx2, ny2, nx3, ny3);
    line(nx3, ny3, nx1, ny1);

    getch();
    closegraph();
    return 0;
}