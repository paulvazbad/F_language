int x,f;
int mat[2][3];
int tictactoe[3][3][3];
int p;
function uno(){
    read(x);
    p=tictactoe[1][1][0]+mat[1][1];
}
function dos(){
    print(f);
}
function tres(){
    if(x>1){
        f = f*x;
        x =x-1;
        tres();
    }
}

main(){
    f = 1;
    uno();
    tres();
    dos();
}