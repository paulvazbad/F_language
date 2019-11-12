int x,f;
function uno(){
    read(x);
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