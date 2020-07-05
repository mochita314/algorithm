#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void){

    int n;

    printf("%s","行列のサイズを入力してください:");
    scanf("%d",&n);

    int A[n][n];
    int B[n][n];

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            A[i][j] = rand() % 10;
            B[i][j] = rand() % 10;
        }
    }

    int C[n][n];
    double times[6];
    for(int i=0;i<6;i++){
        times[i] = 0;
    }
    double max_iter = 10;

    for(int trial=0;trial<max_iter;trial++){

        for(int time=0;time<6;time++){

            clock_t start,end;

            for(int i=0;i<n;i++){
                for(int j=0;j<n;j++){
                    C[i][j] = 0;
                }
            }

            start = clock();

            if(time==0){
                // i-k-j
                for(int i=0;i<n;i++){
                    for(int k=0;k<n;k++){
                        for(int j=0;j<n;j++){
                            C[i][j] += A[i][k]*B[k][j];
                        }
                    }
                }   
            }else if(time==1){
                // i-j-k
                for(int i=0;i<n;i++){
                    for(int j=0;j<n;j++){
                        for(int k=0;k<n;k++){
                            C[i][j] += A[i][k]*B[k][j];
                        }
                    }
                }  
            }else if(time==2){
                // k-i-j
                for(int k=0;k<n;k++){
                    for(int i=0;i<n;i++){
                        for(int j=0;j<n;j++){
                            C[i][j] += A[i][k]*B[k][j];
                        }
                    }
                }  
            }else if(time==3){
                // k-j-i
                for(int k=0;k<n;k++){
                    for(int j=0;j<n;j++){
                        for(int i=0;i<n;i++){
                            C[i][j] += A[i][k]*B[k][j];
                        }
                    }
                }  
            }else if(time==4){
                // j-i-k
                for(int j=0;j<n;j++){
                    for(int i=0;i<n;i++){
                        for(int k=0;k<n;k++){
                            C[i][j] += A[i][k]*B[k][j];
                        }
                    }
                }              
            }else{
                // j-k-i
                for(int j=0;j<n;j++){
                    for(int k=0;k<n;k++){
                        for(int i=0;i<n;i++){
                            C[i][j] += A[i][k]*B[k][j];
                        }
                    }
                }  
            }

            end = clock();
            
            times[time] += (double)(end-start)/CLOCKS_PER_SEC;
        }
    }
    

    for(int i=0;i<6;i++){
        times[i] /= max_iter;
    }

    //printf("%.8f秒かかりました\n",(double)(end-start)/CLOCKS_PER_SEC);
    printf("%s-%s-%s -> %.8f秒\n","j","k","i",times[5]);
    printf("%s-%s-%s -> %.8f秒\n","j","i","k",times[4]);
    printf("%s-%s-%s -> %.8f秒\n","k","j","i",times[3]);
    printf("%s-%s-%s -> %.8f秒\n","k","i","j",times[2]);
    printf("%s-%s-%s -> %.8f秒\n","i","j","k",times[1]);
    printf("%s-%s-%s -> %.8f秒\n","i","k","j",times[0]);
    
    return 0;

}