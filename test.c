#include <stdio.h>

int factorial(int x){
    int ans = 1;
    for(int i = 1; i <= x; i++){
        ans *= i;
    }
    return ans;
}

int count(int x){
    int counter = 0;
    while(x!=0){
        x /= 10;
        counter++;

    }
    return counter;
}



int main(){

    int inp = 0;
    scanf("%d", &inp);

    no_of_digits = count(inp);
    int digits[no_of_digits];

    for(int i = 1; i < no_of_digits, i++){
        digits[i] = inp/pow(10, i)
    }

}

