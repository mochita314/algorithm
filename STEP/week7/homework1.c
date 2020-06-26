#include <stdio.h>
#include <stdlib.h>

int main(void){

    int n;

    printf("%s","行列のサイズを入力してください:");
    scanf("%d",&n);

    int A[n][n];
    int B[n][n];

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            A[i][j] = rand() % 10 + 1;
            B[i][j] = rand() % 10 + 1;
        }
    }

    int C[n][n];

    
    return 0;

}