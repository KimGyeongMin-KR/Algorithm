#include <stdio.h>
struct time
{
   int H, M, LONG;
};

int main()
{
    struct time AL;
    int H, M;
    scanf("%d %d", &AL.H, &AL.M);
    scanf("%d", &AL.LONG);
    M = AL.M + AL.LONG;

    while(60 <= M)
    {
        AL.H += 1;
        M -= 60;
        if(24 <= AL.H)
        {
            AL.H = 0;
        }
    }
    AL.M = M;
    printf("%d %d", AL.H, AL.M);
}
