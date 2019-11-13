int x,f;
int dummy;
function uno(){
    read(x);
}
function dos(){
    print(f);
}
function tres(){
    if(x>1 && dummy==5){
        f = f*x;
        x =x-1;
        tres();
    }
}

main(){
    dummy =5;
    f = 1;
    uno();
    tres();
    dos();
}